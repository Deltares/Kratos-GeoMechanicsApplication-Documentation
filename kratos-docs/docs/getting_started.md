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

### Downloading the required files

First, we need a set of input files, which consists of a model file (`.mdpa`), an analysis file (`.json`) and two material properties files (`.json`). For demonstration purposes, we will analyse the staged construction of a building pit, known as the CROW case. Create a folder where you will store the input files, e.g. `CROW_case`, and save the following files there:

- [`CROW_case_clay-sand.mdpa`](examples/crow_case/KratosCROW_7Stage_MohrCoulomb/CROW_case_clay-sand.mdpa)
- [`staged_construction.json`](examples/crow_case/KratosCROW_7Stage_MohrCoulomb/staged_construction.json)
- [`initial_materials.json`](examples/crow_case/KratosCROW_7Stage_MohrCoulomb/initial_materials.json)
- [`Mohr_Coulomb_materials.json`](examples/crow_case/KratosCROW_7Stage_MohrCoulomb/Mohr_Coulomb_materials.json)

In addition, to compare the simulation results, we will need the following set of CSV files with base line results:

- [`3_Wall_installation__base_line_wall.csv`](examples/crow_case/KratosCROW_7Stage_MohrCoulomb/3_Wall_installation__base_line_wall.csv)
- [`4_First_excavation__base_line_wall.csv`](examples/crow_case/KratosCROW_7Stage_MohrCoulomb/4_First_excavation__base_line_wall.csv)
- [`5_Anchor_installation__base_line_wall.csv`](examples/crow_case/KratosCROW_7Stage_MohrCoulomb/5_Anchor_installation__base_line_wall.csv)
- [`6_Second_excavation__base_line_wall.csv`](examples/crow_case/KratosCROW_7Stage_MohrCoulomb/6_Second_excavation__base_line_wall.csv)
- [`7_Third_excavation__base_line_wall.csv`](examples/crow_case/KratosCROW_7Stage_MohrCoulomb/7_Third_excavation__base_line_wall.csv)

Finally, we will need a Python script that runs the geomechanical analysis. [The Python script that we have prepared](examples/crow_case/KratosCROW_7Stage_MohrCoulomb/run_simulation.py) also makes plots (SVG files) that show the bending moments, shear forces, normal forces and horizontal total displacements of the sheet pile wall for the various stages. Save this script in the same folder, too.


### Running the analysis

To run the simulation from the Command Prompt, execute `python run_simulation.py`. This will produce several files, including JSON files with analysis results and SVG files with plots.
