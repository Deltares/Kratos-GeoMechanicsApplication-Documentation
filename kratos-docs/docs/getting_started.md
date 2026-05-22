# Getting Started

This section assumes that you are working on a Windows system.


## Installing Kratos

To follow along with this tutorial, please make sure that you have a recent Python version (3.11 up to and including 3.14) installed on your system.  When you don't have Python installed yet, please download the latest Python installer from the [official Python website](https://www.python.org/) and follow the on-screen instructions to install it.


### Setting up and activating a Python venv

It is generally recommended to install the GeoMechanicsApplication in a [Python virtual environment](https://docs.python.org/3/glossary.html#term-virtual-environment) (or "venv", for short). To create and activate such an environment, please carry out the following steps:

- Open a Command Prompt.
- Double-check whether Python is available by executing `python --version`.  In this way, you can also verify which Python version you are using.
- Create a folder where you would like to install the GeoMechanicsApplication, e.g. `mkdir GeoMechanicsApplication`.
- Change the current working directory to this new folder: `cd GeoMechanicsApplication`.
- Create a new Python venv: `python -m venv .venv`. Optionally, when you have multiple Python versions installed, you may want to use the [Python launcher](https://docs.python.org/3/using/windows.html#python-launcher-for-windows-deprecated) to indicate which Python version you would like to use. For instance, if you would like to use Python 3.12, execute the following command: `py -3.12 -m venv .venv`.
- Activate the Python venv: `.venv\Scripts\activate`.


### Using pypi

KratosGeoMechanicsApplication can be installed via pypi. The latest release (currently version 10.4.2) can be downloaded and installed from [the pypi website](https://pypi.org/project/KratosGeoMechanicsApplication/). In the Command Prompt, execute `pip install KratosGeoMechanicsApplication`.


### Using Python wheels

More recent versions of the main-development branch can be obtained by sending an e-mail to the Kratos team. In that case, please mention which Python version you are using. Once you have received the appropriate `zip` archive, proceed as follows:

- Extract the archive in the `GeoMechanicsApplication` folder that you have created earlier on. This results in a new subdirectory named `wheels`, which contains the `.whl` files.
- Change the current working directory to this new subdirectory: `cd wheels`.
- Install the Python wheels by executing the Windows batch script: `.\install`.
- Install an additional required Python package: `pip install matplotlib`.

### Building Kratos from scratch

If you want to compile Kratos as well, see the instructions on the [Kratos website](https://kratosmultiphysics.github.io/Kratos/pages/Kratos/For_Users/How_To_Get_Kratos/Binaries.html).


## Running a Kratos simulation

Once Kratos has been installed, we can proceed as follows to run the first geomechanical analysis.

### Downloading and preparing the input files

First, we need a set of input files, which consists of a model file (`.mdpa`), an analysis file (`.json`) and two material properties files (`.json`). For demonstration purposes, we will analyse the staged construction of a building pit, known as the CROW case. Create a folder where you will store the input files, e.g. `CROW_case`, and save the following files there:

- [`CROW_case_clay-sand.mdpa`](examples/crow_case/KratosCROW_7Stage_MohrCoulomb/CROW_case_clay-sand.mdpa)
- [`staged_construction.json`](examples/crow_case/KratosCROW_7Stage_MohrCoulomb/staged_construction.json)
- [`initial_materials.json`](examples/crow_case/KratosCROW_7Stage_MohrCoulomb/initial_materials.json)
- [`Mohr_Coulomb_materials.json`](examples/crow_case/KratosCROW_7Stage_MohrCoulomb/Mohr_Coulomb_materials.json)

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

Save the above Python code in a file that is located in the same folder as the input files, e.g. `run_simulation.py`. Then, you can run the simulation from the Command Prompt by executing `python run_simulation.py`.
