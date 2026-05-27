import csv
import importlib
import json
import os
import sys
from pathlib import Path

import KratosMultiphysics as Kratos
from KratosMultiphysics.project import Project
import KratosMultiphysics.GeoMechanicsApplication.geo_plot_utilities as plot_utils


bending_moment_label = "BENDING_MOMENT"
shear_force_label = "SHEAR_FORCE"
normal_force_label = "AXIAL_FORCE"
horizontal_total_displacement_label = "TOTAL_DISPLACEMENT_X"

csv_field_name_node = "node"
csv_field_name_bending_moment = "bending_moment_in_Nm_per_m"
csv_field_name_shear_force = "shear_force_in_N_per_m"
csv_field_name_normal_force = "normal_force_in_N_per_m"
csv_field_name_horizontal_total_displacement = "horizontal_total_displacement_in_m"

plot_file_paths_by_result = {
    bending_moment_label: Path("bending_moments.svg"),
    shear_force_label: Path("shear_forces.svg"),
    normal_force_label: Path("normal_forces.svg"),
    horizontal_total_displacement_label: Path("horizontal_total_displacements.svg"),
}


def remove_output_and_plot_files():
    for file_path in plot_file_paths_by_result.values():
        try:
            os.remove(file_path)
        except FileNotFoundError:
            pass


def unit_to_kilo_unit(value):
    return value / 1000.0


def get_nodal_data_from_csv(csv_file_path):
    result_field_names = [
        csv_field_name_bending_moment,
        csv_field_name_shear_force,
        csv_field_name_normal_force,
        csv_field_name_horizontal_total_displacement,
    ]
    with open(csv_file_path, newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        return {
            int(row[csv_field_name_node]): {
                field_name: float(row[field_name]) for field_name in result_field_names
            }
            for row in reader
        }


def _make_data_series_list_for_all_stages(
    stage_names,
    nodes_of_sheet_pile_wall,
    result_item_label,
    transform_value=None,
    csv_field_name=None,
):
    """
    Returns a list with one item per stage. Each item is a list of one data
    series that corresponds to the result of the current simulation.
    """
    if transform_value is None:
        transform_value = lambda value: value

    y_coordinates = [node.Y for node in nodes_of_sheet_pile_wall]

    result = []
    for name in stage_names:
        stage_data_series = []

        json_output_path = Path(f"{name}__output_wall.json")
        with open(json_output_path, "r") as f:
            analysis_results = json.load(f)
        result_values = [
            transform_value(analysis_results[f"NODE_{node.Id}"][result_item_label][0])
            for node in nodes_of_sheet_pile_wall
        ]

        # Sort data points by Y coordinate
        sorted_y_coordinates, sorted_result_values = zip(
            *sorted(zip(y_coordinates, result_values))
        )

        stage_data_series.append(
            plot_utils.DataSeries(
                zip(sorted_result_values, sorted_y_coordinates),
                label="Kratos (current simulation)",
                line_style="-",
                marker=".",
            )
        )

        if csv_field_name is not None:
            nodal_data = get_nodal_data_from_csv(Path(f"{name}__base_line_wall.csv"))
            base_line_values = [
                transform_value(nodal_data[node.Id][csv_field_name])
                for node in nodes_of_sheet_pile_wall
            ]

            # Sort data points by Y coordinate
            sorted_y_coordinates, sorted_base_line_values = zip(
                *sorted(zip(y_coordinates, base_line_values))
            )

            stage_data_series.append(
                plot_utils.DataSeries(
                    zip(sorted_base_line_values, sorted_y_coordinates),
                    label="Kratos (base line)",
                    line_style="-",
                    marker="1",
                )
            )

        result.append(stage_data_series)

    return result


def _make_result_plot(
    nodes_of_sheet_pile_wall,
    result_item_label,
    xlabel,
    transform_value=None,
    csv_field_name=None,
):
    plot_file_path = plot_file_paths_by_result[result_item_label]

    names_of_stages_to_be_plotted = [
        "3_Wall_installation",
        "4_First_excavation",
        "5_Anchor_installation",
        "6_Second_excavation",
        "7_Third_excavation",
    ]

    plot_utils.make_sub_plots(
        _make_data_series_list_for_all_stages(
            names_of_stages_to_be_plotted,
            nodes_of_sheet_pile_wall,
            result_item_label,
            transform_value=transform_value,
            csv_field_name=csv_field_name,
        ),
        plot_file_path,
        titles=names_of_stages_to_be_plotted,
        xlabel=xlabel,
        ylabel=r"$y$ [m]",
    )


def _plot_bending_moments(nodes_of_sheet_pile_wall):
    _make_result_plot(
        nodes_of_sheet_pile_wall,
        bending_moment_label,
        "Bending moment [kNm/m]",
        transform_value=unit_to_kilo_unit,
        csv_field_name=csv_field_name_bending_moment,
    )


def _plot_shear_forces(nodes_of_sheet_pile_wall):
    _make_result_plot(
        nodes_of_sheet_pile_wall,
        shear_force_label,
        "Shear force [kN/m]",
        transform_value=unit_to_kilo_unit,
        csv_field_name=csv_field_name_shear_force,
    )


def _plot_normal_forces(nodes_of_sheet_pile_wall):
    _make_result_plot(
        nodes_of_sheet_pile_wall,
        normal_force_label,
        "Normal force [kN/m]",
        transform_value=unit_to_kilo_unit,
        csv_field_name=csv_field_name_normal_force,
    )


def _plot_horizontal_total_displacements(nodes_of_sheet_pile_wall):
    _make_result_plot(
        nodes_of_sheet_pile_wall,
        horizontal_total_displacement_label,
        "Horizontal total displacement [m]",
        csv_field_name=csv_field_name_horizontal_total_displacement,
    )


def _make_plots(model):
    print("Making plots...")

    nodes_of_sheet_pile_wall = model.GetModelPart("PorousDomain.Sheet_Pile_Wall").Nodes

    _plot_bending_moments(nodes_of_sheet_pile_wall)
    _plot_shear_forces(nodes_of_sheet_pile_wall)
    _plot_normal_forces(nodes_of_sheet_pile_wall)
    _plot_horizontal_total_displacements(nodes_of_sheet_pile_wall)


def _main():
    remove_output_and_plot_files()

    with open(Path("staged_construction.json")) as analysis_file:
        analysis_parameters = Kratos.Parameters(analysis_file.read())

    try:
        project = Project(analysis_parameters)
        orchestrator_reg_entry = Kratos.Registry[
            project.GetSettings()["orchestrator"]["name"].GetString()
        ]
        orchestrator_module = importlib.import_module(
            orchestrator_reg_entry["ModuleName"]
        )
        orchestrator_class = getattr(
            orchestrator_module, orchestrator_reg_entry["ClassName"]
        )
        orchestrator_instance = orchestrator_class(project)
        orchestrator_instance.Run()

        _make_plots(project.GetModel())

    except Exception as e:
        print(f"Error: {str(e)}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(_main())
