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

names_of_stages_to_be_plotted = [
    "3_Wall_installation",
    "4_First_excavation",
    "5_Anchor_installation",
    "6_Second_excavation",
    "7_Third_excavation",
]


def json_output_file_path_for_stage(stage_name):
    return Path(f"{stage_name}__output_wall.json")


def remove_output_and_plot_files():
    for file_path in [
        json_output_file_path_for_stage(name) for name in names_of_stages_to_be_plotted
    ] + list(plot_file_paths_by_result.values()):
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


def make_data_series_sorted_by_y_coordinate(
    y_coordinates, result_values, label, line_style, marker
):
    sorted_y_coordinates, sorted_result_values = zip(
        *sorted(zip(y_coordinates, result_values))
    )

    return plot_utils.DataSeries(
        zip(sorted_result_values, sorted_y_coordinates),
        label=label,
        line_style=line_style,
        marker=marker,
    )


def make_sorted_data_series_from_analysis_output(
    stage_name,
    y_coordinates,
    nodes_of_sheet_pile_wall,
    result_item_label,
    transform_value,
):
    with open(json_output_file_path_for_stage(stage_name), "r") as f:
        analysis_results = json.load(f)

    result_values = [
        transform_value(analysis_results[f"NODE_{node.Id}"][result_item_label][0])
        for node in nodes_of_sheet_pile_wall
    ]

    return make_data_series_sorted_by_y_coordinate(
        y_coordinates,
        result_values,
        label="Kratos (current simulation)",
        line_style="-",
        marker=".",
    )


def _make_data_series_list_for_all_stages(
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
    for name in names_of_stages_to_be_plotted:
        stage_data_series = []

        try:
            stage_data_series.append(
                make_sorted_data_series_from_analysis_output(
                    name,
                    y_coordinates,
                    nodes_of_sheet_pile_wall,
                    result_item_label,
                    transform_value,
                )
            )
        except Exception as e:
            print(
                f"WARNING: no '{result_item_label}' data series for stage '{name}': {str(e)}"
            )
            continue

        if csv_field_name is not None:
            nodal_data = get_nodal_data_from_csv(Path(f"{name}__base_line_wall.csv"))
            base_line_values = [
                transform_value(nodal_data[node.Id][csv_field_name])
                for node in nodes_of_sheet_pile_wall
            ]

            stage_data_series.append(
                make_data_series_sorted_by_y_coordinate(
                    y_coordinates,
                    base_line_values,
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
    plot_utils.make_sub_plots(
        _make_data_series_list_for_all_stages(
            nodes_of_sheet_pile_wall,
            result_item_label,
            transform_value=transform_value,
            csv_field_name=csv_field_name,
        ),
        plot_file_paths_by_result[result_item_label],
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


def run_analysis(project):
    orchestrator_reg_entry = Kratos.Registry[
        project.GetSettings()["orchestrator"]["name"].GetString()
    ]
    orchestrator_module = importlib.import_module(orchestrator_reg_entry["ModuleName"])
    orchestrator_class = getattr(
        orchestrator_module, orchestrator_reg_entry["ClassName"]
    )
    orchestrator_instance = orchestrator_class(project)
    orchestrator_instance.Run()


def _main():
    exit_code = 0

    remove_output_and_plot_files()

    try:
        with open(Path("staged_construction.json")) as analysis_file:
            analysis_parameters = Kratos.Parameters(analysis_file.read())
        project = Project(analysis_parameters)
        run_analysis(project)
    except Exception as e:
        print(f"Analysis ERROR: {str(e)}")
        exit_code = 1

    try:
        _make_plots(project.GetModel())
    except Exception as e:
        print(f"Plotting ERROR: {str(e)}")
        exit_code = 2 if exit_code == 0 else exit_code

    return exit_code


if __name__ == "__main__":
    sys.exit(_main())
