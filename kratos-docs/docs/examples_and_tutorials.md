# Examples and Tutorials

This page collects examples and tutorials for running and exploring Kratos GeoMechanics simulations.

## CROW Case: Building Pit Model with Sheetpile Wall

To run Kratos simulations for the CROW case, examples are available in Jupyter notebooks:

[Running a Kratos simulation for a sheet pile wall](https://github.com/Deltares/Kratos-GeoMechanicsApplication-Documentation/blob/main/kratos-docs/docs/examples/crow_case/kratos_crow_2stage_linear_elastic.ipynb) <br>

[Uncertainty analysis of the bending moment](https://github.com/Deltares/Kratos-GeoMechanicsApplication-Documentation/blob/main/kratos-docs/docs/examples/crow_case/uncertainty_analysis_bending_moment.ipynb) <br>


## Backwards Erosion Piping Analysis

This example demonstrates a backwards erosion piping analysis combined with a steady-state groundwater flow analysis. The input consists of three files:

- [`mesh.mdpa`](examples/piping_analysis/mesh.mdpa)
- [`MaterialParameters.json`](examples/piping_analysis/MaterialParameters.json)
- [`piping_analysis.json`](examples/piping_analysis/piping_analysis.json)

Download these files to a directory of your choice. In addition, you need to download the [Python script](examples/piping_analysis/run_simulation.py) that will run the analysis and save it to the same directory where you have put the input files. Note that the Python script contains a few additional analysis parameters, including the minimum critical head, the maximum critical head and the head increment. The adopted values have been taken from the corresponding analysis with D-Geo Flow.

To actually run the analysis, we need to have a Python virtual environment set up, where the GeoMechanicsApplication has been installed. If you don't have that available yet, please follow along the steps described in the [Getting Started](getting_started.md) section first. Assuming you have a Command Prompt with an active Python venv, you can now run the analysis with the command `python run_simulation.py`

The output of the backwards erosion piping analysis consists of a calculated critical head that has been written to the file `criticalHead.json` (which you will find in the same directory as the input files). In this example, the critical head was found to be equal to 1.1 meter.
