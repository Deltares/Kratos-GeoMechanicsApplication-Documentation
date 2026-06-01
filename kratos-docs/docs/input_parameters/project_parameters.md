# ProjectParameter.json file description
Here, the structural format of the ProjectParameter.json is described and the meaning of the parameters is explained.

By clicking on an annotation (1) the user is provided more detailed information about a property.
{ .annotate }

1. Here more information about an annotation can be found.

## ProjectParameter.json structure format
On the top level the project parameter file has an `orchestrator` that executes different `stages` sequentially.
```json
{
  "orchestrator": {
	"name": "Orchestrators.KratosMultiphysics.SequentialOrchestrator", //(1)!
    "settings": { } //(2)!
  },
  "stages": {
	"stage_1": { //(3)!
		"stage_preprocess": { }, //(4)!
		"stage_settings": { } // (5)!
	}
  }
}
```

1. Name of the orchestrator used to run the simulation. </br>
Type: string. </br>
Allowed values: `Orchestrators.KratosMultiphysics.SequentialOrchestrator`
2. Settings for the orchestrator. [Details](#orchestrator-settings-block-structure-format).
3. Stage names as defined in the "execution list". [Details](#orchestrator-settings-block-structure-format).
4. Operations executed before the stage begins. For example importing a model from a file and (de)activation of model parts. [Details](#stage-preprocess-block-structure-format).
5. Settings for the current stage. [Details](#stage-settings-block-structure-format).
### Orchestrator settings block structure format
```json
"settings": { 
	"echo_level": 0, //(1)!
	"execution_list": [ ], //(2)!
	"load_from_checkpoint": null, //(3)!
	"stage_checkpoints": false //(4)!
}
```

1. {{ echo_level }}
2. List of stage names in execution order. Type: array of strings.
3. Checkpoint to load the simulation from. Type: string or null.
4. Enable or disable saving checkpoints per stage. Type: boolean.
### Stage preprocess block structure format
```json
"stage_preprocess": { 
	"modelers": [ //(1)!
		{
			"name": "Modelers.KratosMultiphysics.ImportMDPAModeler", //(2)!
			"Parameters": {
				"input_filename": "my_mesh_file", //(3)!
				"model_part_name": "PorousDomain" //(4)!
			}
		}
	],
	"operations": [ //(5)!
		{
			"name": "Operations.KratosMultiphysics.GeoMechanicsApplication.DeactivateModelPartOperation", //(6)!
			"Parameters": { 
				"model_part_name_list": [ //(7)!
					"PorousDomain.Right_Soil",
					"PorousDomain.Left_Soil"
				] 
			}
		}
	]
}
```

1. List of modelers performing preprocessing tasks such as importing a mesh file or setting up a geometry. Type: array of objects.
2. Name of the modeler. Type: string. </br> 
Allowed values: `Modelers.KratosMultiphysics.ImportMDPAModeler`.
3. Path to (relative or absolute) the model file (.mdpa). Type: string. Note: do not put .mdpa at the end of the filename.
4. {{ overarching_model_part_name }}
5. List of operations performing preprocessing tasks such as activating and deactivating model parts. Type: array of objects.
6. Name of the operation. Type: string. Allowed values: "...DeactivateModelPartOperation", "...ActivateModelPartOperation"
7. List of model parts that need to be activated or deactivated. Type: array of strings. Allowed values: Each entry should start with the above defined overarching model part name, followed by the sub-part name as defined in the mesh file.
### Stage settings block structure format
```json
"stage_settings": {
	"analysis_stage": "Stages.KratosMultiphysics.GeoMechanicsApplication.GeoMechanicsAnalysis", //(1)!
	"problem_data": { },  //(2)!
	"solver_settings": { },  //(3)!
	"processes": { }  //(4)!
	"output_processes": { },  //(5)!
}
```

1. The kind of analysis stage used for the simulation. Type: string. Allowed values: `Stages.KratosMultiphysics.GeoMechanicsApplication.GeoMechanicsAnalysis`.
2. General settings for the Kratos run. [Details](#problem-data-block-structure-format)
3. Settings for the solvers, like analysis type, linear solver, etc. [Details](#solver-settings-block-structure-format)
4. Processes to e.g. apply boundary conditions. [Details](#processes-block-structure-format)
5. Settings for the output. [Details](#output-processes-block-structure-format).

#### Problem data block structure format

```json
"problem_data": {
  "problem_name": "stage_1",  //(1)!
  "start_time": 0.0,  //(2)!
  "end_time": 0.1,  //(3)!
  "echo_level": 1, //(4)!
  "parallel_type": "OpenMP",  //(5)!
  "number_of_threads": 1  //(6)!
}
```

1. Descriptive name of the problem or stage. Type: string. [Details](#orchestrator-settings-block-structure-format).
2. The start time of this stage. Type: float. Can also be negative.
3. The end time of this stage. Type: float. Can also be negative, but must be greater than the start time.
4. {{ echo_level }}
5. Method of parallel computation. Type: string. Allowed values: `OpenMP`.
6. Number of threads for parallel computation. Type: integer. Default = 1.

#### Solver settings block structure format
```json
"solver_settings": {
    "solver_type": "U_Pw",  //(1)!
    "model_part_name": "PorousDomain",  //(2)!
    "domain_size": 2,  //(3)!
    "model_import_settings": {
      "input_type": "mdpa",  //(4)!
      "input_filename": "mesh"  //(5)!
    },
    "material_import_settings": {
      "materials_filename": "MaterialParameters.json"  //(6)!
    },
    "time_stepping": {  //(7)!
      "time_step": 1.0,  //(8)!
      "max_delta_time_factor": 1.0E+09,  //(9)!
	  "minimum_allowable_value": 1.0E-03  //(10)!
    },
    "buffer_size": 2,  //(11)!
    "echo_level": 1, //(12)!
	"clear_storage": false,  //(13)!
    "compute_reactions": false, //(14)!
    "move_mesh_flag": false, //(15)!
    "reform_dofs_at_each_step": true, //(16)!
    "block_builder": true, //(17)!
    "solution_type": "static", //(18)!
    "scheme_type": "newmark", //(19)!
    "reset_displacements": false, //(20)!
	"strategy_type": "line_search", //(21)!
	"convergence_criterion": "displacement_criterion", //(22)!
	"displacement_relative_tolerance": 1.0E-04, //(23)!
    "displacement_absolute_tolerance": 1.0E-09, //(24)!
    "water_pressure_relative_tolerance": 1.0E-04, //(25)!
    "water_pressure_absolute_tolerance": 1.0E-09, //(26)!
	"residual_relative_tolerance": 1.0E-04, //(27)!
    "residual_absolute_tolerance": 1.0E-09, //(28)!
	"min_iterations": 6, //(29)!
    "max_iterations": 15, //(30)!
    "number_cycles": 10, //(31)!
    "reduction_factor": 0.5, //(32)!
    "increase_factor": 2.0, //(33)!
	"desired_iterations": 4, //(34)!
	"max_radius_factor": 10.0, //(35)!
	"min_radius_factor": 0.1, //(36)!
	"max_line_search_iterations": 5, //(37)!
	"first_alpha_value": 0.5, //(38)!
	"second_alpha_value": 1.0, //(39)!
	"min_alpha": 0.1, //(40)!
	"max_alpha": 2.0, //(41)!
	"line_search_tolerance": 0.5, //(42)!
	"rotation_dofs": true, //(43)!
	"linear_solver_settings": { //(44)!
      "solver_type": "LinearSolversApplication.sparse_lu", //(45)!
      "scaling": true //(46)!
    },
	"problem_domain_sub_model_part_list": [ ],  //(47)!
	"body_domain_sub_model_part_list": [ ],  //(48)!
	"newmark_beta": 0.25,   //(49)!
    "newmark_gamma": 0.5,   //(50)!
    "newmark_theta": 0.5,   //(51)!
    "rayleigh_m": 0.0,   //(52)!
    "rayleigh_k": 0.0,  //(53)!
	"max_piping_iterations": 500  //(54)!
  }
```

1. Analysis type. Type: string. </br> Allowed values: `U_Pw == geomechanics_U_Pw_solver`, `Pw == geomechanics_pw_solver`, `T == geomechanics_T_solver`.
2. {{ overarching_model_part_name }}
3. Working space dimension. Type: integer. Allowed values: 2 for 2D and 3 for 3D.
4. Format of the model input file. Type: string. </br> Allowed values: `mdpa` or `use_input_model_part`. 
</br> Note: When the `ImportMDPAModeler` is used in in [modelers](#stage-preprocess-block-structure-format) section, here the input_type should be `use_input_model_part` to avoid reading the input file more than once.
5. Name of the model input file. Type: string. Only necessary when input_type is set to `mdpa`.
6. Path to the material parameter file. Type: string.
7. Settings for time stepping.
8. Initial time step size. Type: float.
9. Maximum scaling factor for next time step. Type: float.
10. Tolerance to avoid very small time steps. Type: float.
11. Number of solution vectors to keep for time integration scheme. Type: integer. Here: always 2 (current and previous solutions).
12. {{ echo_level }}
13. Solver storage behaviour. Type: boolean.
14. Function to compute stress/internal/reaction forces. Type: boolean.
15. Update nodal positions with displacement for a geometrically non-linear analysis. Type: boolean.
16. Function to rebuild the system with its degrees of freedom at each step. Type: boolean.
17. Implementation detail of Kratos. Type: boolean. Here: always true.
18. Calculation type. Type: string. Allowed values: `static`, `quasi_static`, `dynamic`, `transient_groundwater_flow`, `steady_state_groundwater_flow`.
19. Time integration scheme. Type: string. Allowed values: `newmark`, `backward_euler`.
20. Function to reset total displacements/rotations at stage start. Type: boolean.
21. Iterative strategy. Type: string. Allowed values: `newton_raphson`, `newton_raphson_with_piping`, `linear`, `line_search`.
22. Convergence criterion type. Type: string. Allowed values: `displacement_criterion`, `water_pressure_criterion`, `residual_criterion`, `temperature_criterion` and `or_criterion`.
23. Relative tolerance for displacement convergence criterion. Type = float.
24. Absolute tolerance for displacement convergence criterion. Type = float.
25. Relative tolerance for water pressure convergence criterion. Type = float.
26. Absolute tolerance for water pressure convergence criterion. Type = float.
27. Relative tolerance for residual force convergence criterion. Type = float.
28. Absolute tolerance for residual force convergence criterion. Type = float.
29. Amount of iterations below which the next time step is scaled up. Type: integer.
30. Maximum amount of iterations per step. If not converged within this value, the time step will be repeated using a smaller time increment. Type: integer.
31. Maximum number of scaled-down retry cycles. Type: integer.
32. Reduction factor for the time step. Type: float.
33. Increase factor for the time step. Type: float.
34. Desired minimum number of iterations for arc-length control. Type: integer.
35. Maximum radius factor for arc-length control. Type: float.
36. Minimum radius factor for arc-length control. Type: float.
38. Maximum number of iterations for line search. Type: integer.
39. First guess for alpha in line search. Type: float.
40. Second guess for alpha in line search. Type: float.
41. Minimum allowed value for alpha in line search. Type: float.
42. Maximum allowed value for alpha in line search. Type: float.
43. Search tolerance in line search. Type: float.
44. Include rotational degrees of freedom. Type: boolean.
45. Linear equation solver settings.
46. Type of linear equation solver. Type: string. Allowed values: `amgcl`, `sparse_lu`, `skyline_lu_factorization`.
47. Solver scaling toggle. Type: boolean.
48. List of model parts. Type: array of strings.
50. List of model parts. Type: array of strings.
51. Newmark time integration parameter $\beta$ used for displacement and rotation degrees of freedom. Type: float.
52. Newmark time integration parameter $\gamma$ used for displacement and rotation degrees of freedom. Type: float.
53. Newmark time integration parameter $\theta$ used for water pressure degrees of freedom. Type: float.
54. Rayleigh damping factor for the mass matrix contribution to the damping matrix. Type: float.
55. Rayleigh damping factor for the stiffness matrix contribution to the damping matrix. Type: float.
56. Maximum number of piping iterations. Type: integer.

#### Processes block structure format
```json
"processes": {
    "constraints_process_list": [ ], //(1)!
    "loads_process_list": [ ], //(2)!
    "auxiliary_process_list": [ ], //(3)!
	"json_output": [ ] //(4)!
}
```

1. List of constraints and boundary conditions. </br>
 Type: array of objects. [Details](#constraints-process-list-block-structure-format)
2. List of loads such as forces and pressures. </br> 
Type: array of objects. [Details](#loads-process-list-block-structure-format)
3. List of auxiliary processes, such as the k0 procedure. </br>
Type: array of objects. [Details](#auxiliary-process-list-block-structure-format)
4. Process to output data in a json format. </br> 
Type: array of objects. [Details](#json-output-list-block-structure-format)

##### Constraints process list block structure format
Constraint processes are used for constraints and boundary conditions in for example the displacement or the water pressure.
Constraint processes can be either vector (e.g. displacement) or scalar (e.g. pressure), depending on the variable being constrained.
Here, an example for a displacement constraint is shown.

```json
{
  "python_module": "apply_vector_constraint_table_process", //(1)!
  "kratos_module": "KratosMultiphysics.GeoMechanicsApplication", //(2)!
  "process_name": "ApplyVectorConstraintTableProcess",
  "Parameters": {
    "model_part_name": "PorousDomain.xxx", //(4)!
    "variable_name": "DISPLACEMENT", //(5)!
    "active": [true, false, false], //(6)!
    "is_fixed": [true, false, false], //(7)!
    "value": [0.0, 0.0, 0.0], //(8)!
    "table": [0, 0, 0] //(9)!
  }
}
```

1. Name of the python module. Type: string. Allowed values: `apply_vector_constraint_table_process`, `apply_scalar_constraint_table_process`, etc..
2. Name of the Kratos application containing the python module. Type: string.
3. Name of the process class. Type: string.
4. {{ model_part_name }}
5. {{ variable_name }}
6. {{ active }}
7. {{ is_fixed }}
8. {{ value }}
9. {{ table }}

And here, an example for a water pressure constraint is shown.

```json
{
  "python_module": "apply_scalar_constraint_table_process", //(1)!
  "kratos_module": "KratosMultiphysics.GeoMechanicsApplication", //(2)!
  "process_name": "ApplyScalarConstraintTableProcess", //(3)!
  "Parameters": {
    "model_part_name": "PorousDomain", //(4)!
    "variable_name": "WATER_PRESSURE", //(5)!
    "is_fixed": true, //(6)!
    "table": 0, //(7)!
    "fluid_pressure_type": "Hydrostatic", //(8)!
    "gravity_direction": 1, //(9)!
    "reference_coordinate": -25.0, //(10)!
    "specific_weight": 1.0E+05, //(11)!
    "pressure_tension_cut_off": 0.0 //(12)!
  }
}
```

1. Name of the python module. Type: string. Allowed values: `apply_vector_constraint_table_process`, `apply_scalar_constraint_table_process`, etc..
2. Name of the Kratos application containing the python module. Type: string.
3. Name of the process class. Type: string.
4. {{ model_part_name }}
5. {{ variable_name }}
6. Defines whether the value is fixed. Type: boolean. Dirichlet = `true`, initial value = `false`.
7. Table ID for time-dependent values. Type: integer.
8. Type of fluid pressure constraint used. Type: string. Allowed values: `Hydrostatic`, `Uniform`, `Interpolate_Line`, `Phreatic_Line`, `Phreatic_Multi_Line`, `Phreatic_Surface`.
9. Direction of gravity. Type: integer. Allowed values: 0, 1, 2 for X, Y, Z.
10. Reference coordinate for the phreatic level in the gravity direction. Type: float. 
11. Specific weight of water. Type: float.
12. Cut-off value to prevent negative pressure (suction). Type: float.


##### Loads process list block structure format
Load processes are used for applying external forces and pressures such as gravity.
An example is given here.

```json
{
  "python_module": "apply_vector_constraint_table_process", //(1)!
  "kratos_module": "KratosMultiphysics.GeoMechanicsApplication", //(2)!
  "process_name": "ApplyVectorConstraintTableProcess", //(3)!
  "Parameters": {
    "model_part_name": "PorousDomain", //(4)!
    "variable_name": "VOLUME_ACCELERATION", //(5)!
    "active": [false, true, false], //(6)!
    "value": [0.0, -9.81, 0.0], //(7)!
    "table": [0, 0, 0] //(8)!
  }
}
```

1. Name of the python module. Type: string. Allowed values: `apply_vector_constraint_table_process`, `apply_scalar_constraint_table_process`, etc..
2. Name of the Kratos application containing the python module. Type: string.
3. Name of the process class. Type: string.
4. {{ model_part_name }}
5. {{ variable_name }}
6. {{ active }}
7. {{ value }}
8. {{ table }}

##### Auxiliary process list block structure format
As an example of an auxiliary process, the K0 procedure is shown here. The K0 procedure is used to initialize the horizontal stresses in a soil profile from a given vertical stress profile.

```json
{
  "python_module": "apply_k0_procedure_process", //(1)!
  "kratos_module": "KratosMultiphysics.GeoMechanicsApplication", //(2)!
  "process_name": "ApplyK0ProcedureProcess", //(3)!
  "Parameters": { 
    "model_part_name": "PorousDomain", //(4)!
    "variable_name": "CAUCHY_STRESS_TENSOR", //(5)!
	"use_standard_procedure": true //(6)!
  }
}
```

1. Name of the python module. Type: string. Allowed values: `apply_vector_constraint_table_process`, `apply_scalar_constraint_table_process`, etc..
2. Name of the Kratos application containing the python module. Type: string.
3. Name of the process class. Type: string.
4. {{ model_part_name }}
5. {{ variable_name }}
6. Parameter . Type: boolean. Default value: .

##### Json output list block structure format
```json
{
	"python_module": "json_output_process", //(1)!
	"kratos_module": "KratosMultiphysics", //(2)!
	"process_name": "JsonOutputProcess", //(3)!
	"Parameters": {
		"model_part_name": "PorousDomain.Slave_side", //(4)!
		"output_file_name": "3_Wall_installation_interface_output.json", //(5)!
		"output_variables": ["GEO_EFFECTIVE_TRACTION_VECTOR"], //(6)!
		"gauss_points_output_variables": [], //(7)!
		"time_frequency": 0.9999999999 //(8)!
	}
}
```

1. Name of the python module. Type: string.
2. Name of the Kratos application containing the python module. Type: string.
3. Name of the process class. Type: string.
4. {{ model_part_name }}
5. Name of the output file. Type: string. Note: .json should be included at the end of the file name.
6. List of nodal result variables to output. Type: array of strings.
7. List of Gauss point (integration point) result variables to output. Type: array of strings.
8. Time frequency of documenting data in the output json. Type: float.

#### Output processes block structure format
```json
"output_processes": {
    "gid_output": [	 
	    "python_module": "gid_output_process", //(1)!
        "kratos_module": "KratosMultiphysics", //(2)!
        "process_name": "GiDOutputProcess", //(3)!
		"Parameters": {
		    "model_part_name": "PorousDomain.porous_computational_model_part", //(4)!
		    "output_name": "mesh", //(5)!
		    "postprocess_parameters": {
				"result_file_configuration": {
				  "gidpost_flags": {
					"WriteDeformedMeshFlag": "WriteUndeformed", //(6)!
					"WriteConditionsFlag": "WriteElementsOnly", //(7)!
					"GiDPostMode": "GiD_PostAscii", //(8)!
					"MultiFileFlag": "SingleFile" //(9)!
				  },
				  "file_label": "step", //(10)!
				  "output_control_type": "step", //(11)!
				  "output_interval": 1, //(12)!
				  "body_output": true, //(13)!
				  "node_output": false, //(14)!
				  "skin_output": false, //(15)!
				  "nodal_results": [ ],  //(16)!
				  "gauss_point_results": [ ]  //(17)!
				}
			}
		}
	]
}
```

1. Name of the python module. Type: string. Allowed values: `apply_vector_constraint_table_process`, `apply_scalar_constraint_table_process`, etc..
2. Name of the Kratos application containing the python module. Type: string.
3. Name of the process class. Type: string.
4. {{ model_part_name }}
5. Base name of the output files. Type: string.
6. Flag controlling whether the deformed or undeformed mesh is written. Type: string. Allowed values: `WriteUndeformed`, `WriteDeformed`.
7. Flag controlling whether conditions are written. Type: string. Allowed values: `WriteConditions`, `WriteElementsOnly`.
8. Output format used by GiD. Controls whether results are written in ASCII or binary format. Type = string. Allowed values: `GiD_PostAscii`, `GiD_PostBinary`.
9. Flag controlling whether output is written to a single file or multiple files. Type: string. Allowed values: `SingleFile`, `MultipleFiles`.
10. Label type used for indexing in the output files. Type: string. Allowed values: `step`, `time`.
11. Defines whether output is written based on step count or simulation time. Type: string. Allowed values: `step`, `time`.
12. Interval between outputs in steps or time units based on the output_control_type. Type: integer or float.
13. Enable or disable writing of body (element) output. Type: boolean.
14. Enable or disable writing of node output. Type: boolean.
15. Enable or disable writing of skin (model boundary) output. Type: boolean.
16. List of nodal result variables to output. Type: array of strings. </br> (e.g. "DISPLACEMENT",
                                            "TOTAL_DISPLACEMENT",
                                            "WATER_PRESSURE",
                                            "REACTION")
17. List of Gauss point (integration point) result variables to output. Type: array of strings. </br> (e.g. "CAUCHY_STRESS_TENSOR",
                                            "TOTAL_STRESS_TENSOR",
                                            "ENGINEERING_STRAIN_TENSOR")