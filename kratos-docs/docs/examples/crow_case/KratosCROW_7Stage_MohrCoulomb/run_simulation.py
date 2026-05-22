import importlib
import json
import sys
from pathlib import Path

import KratosMultiphysics as Kratos
from KratosMultiphysics.project import Project
import KratosMultiphysics.GeoMechanicsApplication.geo_plot_utilities as plot_utils


def _get_node_ids_of_sheet_pile_wall():
    return [
        3968,
        3982,
        3996,
        4010,
        4026,
        4036,
        4051,
        4066,
        4075,
        4090,
        4102,
        4120,
        4135,
        4148,
        4161,
        4172,
        4188,
        4204,
        4218,
        4231,
        4241,
        4256,
        4271,
        4280,
        4297,
        4308,
        4322,
        4338,
        4352,
        4361,
        4375,
        4390,
        4403,
        4415,
        4430,
        4444,
        4457,
        4470,
        4483,
        4497,
        4509,
        4522,
        4536,
        4547,
        4560,
        4571,
        4582,
        4595,
        4604,
        4614,
        4624,
        4633,
        4639,
    ]


def _get_bending_moment_data_series():
    node_ids = _get_node_ids_of_sheet_pile_wall()
    return None


def _generate_plots(model):
    print("About to generate plots")

    stages_info = {
        "initial_stage": {"end_time": -1.0, "base_name": "1_Initial_stage"},
        "null_step": {"end_time": 0.0, "base_name": "2_Null_step"},
        "wall_installation": {"end_time": 1.0, "base_name": "3_Wall_installation"},
        "first_excavation": {"end_time": 2.0, "base_name": "4_First_excavation"},
        "strut_installation": {"end_time": 3.0, "base_name": "5_Anchor_installation"},
        "second_excavation": {"end_time": 4.0, "base_name": "6_Second_excavation"},
        "third_excavation": {"end_time": 5.0, "base_name": "7_Third_excavation"},
    }

    sheet_pile_wall = model.GetModelPart("PorousDomain.Sheet_Pile_Wall")
    print(f"Model part '{sheet_pile_wall.Name}' has {len(sheet_pile_wall.Nodes)} nodes")

    y_coordinates = [node.Y for node in sheet_pile_wall.Nodes]
    for node, y in zip(sheet_pile_wall.Nodes, y_coordinates):
        print(f"Node {node.Id}: y = {y} (check: {node.Y})")

    data_series_per_stage = []
    stages_to_plot = ["wall_installation", "first_excavation", "strut_installation", "second_excavation", "third_excavation"]
    #stages_to_plot = ["wall_installation"]
    for stage_name in stages_to_plot:
        stage_data_series = []
        print(f"Retrieving bending moments of stage '{stage_name}'...")
        base_name = stages_info[stage_name]["base_name"]
        json_output_path = Path(f"{base_name}__output_wall.json")
        # print(f"Reading output from {json_output_path}...")
        with open(json_output_path, "r") as f:
            results = json.load(f)

        bending_moments = [results[f"NODE_{node.Id}"]["BENDING_MOMENT"][0] / 1000.0 for node in sheet_pile_wall.Nodes]

        sorted_y_coordinates, sorted_bending_moments = zip(*sorted(zip(y_coordinates, bending_moments)))
        stage_data_series.append(plot_utils.DataSeries(zip(sorted_bending_moments, sorted_y_coordinates), label="Kratos (current simulation)", line_style="-", marker="."))

        data_series_per_stage.append(stage_data_series)

    plot_titles = [stages_info[stage]["base_name"] for stage in stages_to_plot]
    plot_utils.make_sub_plots(data_series_per_stage, Path("bending_moments.svg"), titles=plot_titles, xlabel="Bending moment [kNm/m]", ylabel="y [m]")


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
