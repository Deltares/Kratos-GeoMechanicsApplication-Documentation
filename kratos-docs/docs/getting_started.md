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

First, we need a set of input files, which consists of a model file (`.mdpa`), an analysis file (`.json`) and a material properties file (`json`). For demonstration purposes, we will analyse the construction of a building pit, known as the CROW case.  You can find the input files [here](https://github.com/KratosMultiphysics/Kratos/tree/geo/crow/applications/GeoMechanicsApplication/tests/crow_validation). _Note that this is a work in progress and therefore the downloaded input files need to be edited manually (for now). We will fix that before the DSD._ Create a folder where you will store the modified input files, e.g. `CROW_case`, and download the following files using the above link:

- [`common/crow_validation_gid.mdpa`](https://github.com/KratosMultiphysics/Kratos/blob/geo/crow/applications/GeoMechanicsApplication/tests/crow_validation/common/crow_validation_gid.mdpa)
- [`common/staged_construction.json`](https://github.com/KratosMultiphysics/Kratos/blob/geo/crow/applications/GeoMechanicsApplication/tests/crow_validation/common/staged_construction.json)
- [`common/initial_materials.json`](https://github.com/KratosMultiphysics/Kratos/blob/geo/crow/applications/GeoMechanicsApplication/tests/crow_validation/common/initial_materials.json)

Since the analysis will be using linear elastic material models only (which won't be changed during the various stages), it is sufficient to have the `initial_materials.json` file only. For clarity, we suggest to rename it to `linear_elastic_materials.json`. Since all input files are contained in one and the same folder (contrary to the original ones), we will to update some file references as described below.

In file `staged_construction.json`, search for `"input_filename"` and modify the corresponding value `"crow_validation_gid"`. Subsequently, in the same file, find all occurrences of `"materials_filename"` (seven in total) and replace the corresponding values by `"linear_elastic_materials.json"`.

Now that we have prepared the input files, the next step is to write a Python script that can actually run the simulation.

```py
import sys
from pathlib import Path

import KratosMultiphysics as Kratos
from KratosMultiphysics.project import Project

def _main():
    with open(Path("staged_construction.json")) as analysis_file:
        analysis_parameters = Kratos.Parameters(analysis_file.read())

    try:
        project = Project(analysis_parameters)
        orchestrator_reg_entry = Kratos.Registry[project.GetSettings()["orchestrator"]["name"].GetString()]
        orchestrator_module = importlib.import_module(orchestrator_reg_entry["ModuleName"])
        orchestrator_class = getattr(orchestrator_module, orchestrator_reg_entry["ClassName"])
        orchestrator_instance = orchestrator_class(project)
        orchestrator_instance.Run()
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(_main())
```
