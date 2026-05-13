# Getting Started

## Installing Kratos

### Using pypi

KratosGeoMechanicsApplication can be installed via pypi. The latest release (currently version 10.4.0) can be downloaded from [the pypi website](https://pypi.org/project/KratosGeoMechanicsApplication/). This page also contains instructions on how to install it using `pip`.

### Using Python wheels

More recent versions of the main-development branch can be obtained by sending a mail to the Kratos team.

### Building Kratos from scratch

If you want to compile Kratos as well, see the instructions on the [Kratos website](https://kratosmultiphysics.github.io/Kratos/pages/Kratos/For_Users/How_To_Get_Kratos/Binaries.html).


## Running a Kratos simulation

Once Kratos has been installed, we can proceed as follows to run the first geomechanical analysis.

### Downloading and preparing the input files

First, we need a set of input files, which consists of a model file (`.mdpa`), an analysis file (`.json`) and a material properties file (`.json`). For demonstration purposes, we will analyse the staged construction of a building pit, known as the CROW case. Create a folder where you will store the input files, e.g. `CROW_case`, and save the following files there:

- [`crow_validation_gid.mdpa`](../CROW_case_input/crow_validation_gid.mdpa)
- [`staged_construction.json`](../CROW_case_input/staged_construction.json)
- [`linear_elastic_materials.json`](../CROW_case_input/linear_elastic_materials.json)

Now that we have the input files in-place, the next step is to write a Python script that can actually run the simulation.

```py
import importlib
import sys
from pathlib import Path

import KratosMultiphysics as Kratos
from KratosMultiphysics.project import Project
import KratosMultiphysics.GeoMechanicsApplication.geo_plot_utilities as plot_utils


def _generate_plots():
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

        _generate_plots()

    except Exception as e:
        print(f"Error: {str(e)}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(_main())
```
