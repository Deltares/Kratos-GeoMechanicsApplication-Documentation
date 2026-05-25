import importlib
import json
import sys
from pathlib import Path

import KratosMultiphysics as Kratos
from KratosMultiphysics.project import Project
import KratosMultiphysics.GeoMechanicsApplication.geo_plot_utilities as plot_utils


def _make_bending_moment_data_series_list_for_all_stages(
    stage_names, nodes_of_sheet_pile_wall
):
    """
    Returns a list with one item per stage. Each item is a list of one data
    series that corresponds to the result of the current simulation.
    """
    y_coordinates = [node.Y for node in nodes_of_sheet_pile_wall]

    result = []
    for name in stage_names:
        stage_data_series = []

        json_output_path = Path(f"{name}__output_wall.json")
        with open(json_output_path, "r") as f:
            analysis_results = json.load(f)
        bending_moments = [
            analysis_results[f"NODE_{node.Id}"]["BENDING_MOMENT"][0] / 1000.0
            for node in nodes_of_sheet_pile_wall
        ]

        # Sort data points by Y coordinate
        sorted_y_coordinates, sorted_bending_moments = zip(
            *sorted(zip(y_coordinates, bending_moments))
        )

        stage_data_series.append(
            plot_utils.DataSeries(
                zip(sorted_bending_moments, sorted_y_coordinates),
                label="Kratos (current simulation)",
                line_style="-",
                marker=".",
            )
        )

        result.append(stage_data_series)

    return result


def _plot_bending_moments(nodes_of_sheet_pile_wall):
    names_of_stages_to_be_plotted = [
        "3_Wall_installation",
        "4_First_excavation",
        "5_Anchor_installation",
        "6_Second_excavation",
        "7_Third_excavation",
    ]
    bending_moment_data_series_per_stage = (
        _make_bending_moment_data_series_list_for_all_stages(
            names_of_stages_to_be_plotted, nodes_of_sheet_pile_wall
        )
    )

    plot_utils.make_sub_plots(
        bending_moment_data_series_per_stage,
        Path("bending_moments.svg"),
        titles=names_of_stages_to_be_plotted,
        xlabel="Bending moment [kNm/m]",
        ylabel="y [m]",
    )


def _generate_plots(model):
    print("About to generate plots")

    nodes_of_sheet_pile_wall = model.GetModelPart("PorousDomain.Sheet_Pile_Wall").Nodes
    _plot_bending_moments(nodes_of_sheet_pile_wall)


def _main():
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

        _generate_plots(project.GetModel())

    except Exception as e:
        print(f"Error: {str(e)}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(_main())
