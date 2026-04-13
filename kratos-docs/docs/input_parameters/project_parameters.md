# ProjectParameter.json file description

The project parameters json-file contains as description of the input of the Kratos simulation. More information can be found on the [Kratos website](https://github.com/KratosMultiphysics/Kratos/wiki/Kratos-input-files-and-IO#3-the-project-parameters-file)

## ProjectParameter.json structure format
The strucal format of the ProjectParameter.json is described on the Kratos website:

```json
{
  "problem_data": { },
  "solver_settings": { },
  "output_processes": { },
  "processes": { }
}
```

  * **problem_data**: General settings for the Kratos run
  * **solver_settings**: Settings for the solvers, like analysis type, linear solver, etc.
  * **output_processes**: Processes to e.g. apply boundary conditions.
  * **processes**: Settings for the output 
  
Each of these sections is described below, tailored to a geomechanical analysis.

## Problem data structure format

The problem data block defines general settings for the analysis. 

```json
"problem_data": {
    "problem_name": VARIABLE_NAME,
    "start_time": -1E-06,
    "end_time": 0.0,
    "echo_level": 1,
    "parallel_type": "OpenMP",
    "number_of_threads": 1 ,
```

* **problem_name**: Name of this problem case.
* **start_time**: The start time of this stage preferably in seconds.
* **end_time**: 0.0,	The end time of this stage preferably in seconds.
* **echo_level**: Level of logging. Generally set to 1.
* **parallel_type**: Method of parallel computation. Generally set to "OpenMP".
* **number_of_threads**: Number of threads for parallel computation. Generally set to 1.
