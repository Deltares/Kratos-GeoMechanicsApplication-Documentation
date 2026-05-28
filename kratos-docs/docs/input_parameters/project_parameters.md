# ProjectParameter.json file description
Here, the structural format of the ProjectParameter.json is described, and the meaning of the parameters is explained.

By clicking on an annotation (1) the user is provided more detailed information about a property.
{ .annotate }

1. Here more information about an annotation can be found.

## ProjectParameter.json structure format

```json
{
  "orchestrator": {
	"name": "Orchestrators.KratosMultiphysics.SequentialOrchestrator", //(1)!
    "settings": { } //(2)!
  },
  "stages": {
	"Stage_1": { //(3)!
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
4. Processes executed before the stage begins. For example importing a model from a file and (de)activation of model parts. [Details](#stage-preprocess-block-structure-format).
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
4. Name of the overarching model part. Type: string.
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
2. General settings for the Kratos run. [Details](#problem_data-block-structure-format)
3. Settings for the solvers, like analysis type, linear solver, etc. [Details](#solver_settings-block-structure-format)
4. Processes to e.g. apply boundary conditions. [Details](#processes-block-structure-format)
5. Settings for the output. [Details](#output_processes-block-structure-format).

### problem_data block structure format

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

1. Name of the problem or stage. Type: string. Matches the stage names as defined in the "execution list". [Details](#Orchestrator-settings-block-structure-format).
2. The start time of this stage. Type: float. Can also be negative.
3. The end time of this stage. Type: float. Can also be negative, but must be greater than tehe starttime.
4. Level of logging. Type: integer.
5. Method of parallel computation. Type: string. Allowed values: "OpenMP".
6. Number of threads for parallel computation. Default = 1.

### solver_settings block structure format
```json
"solver_settings": {
    "solver_type": "UPw",  //(1)!
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
      "max_delta_time_factor": 1E+09  //(9)!
	  "minimum_allowable_value": 1E-03  //(10)!
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
	"displacement_relative_tolerance": 1.0E-4, //(23)!
    "displacement_absolute_tolerance": 1.0E-9, //(24)!
    "water_pressure_relative_tolerance": 1.0E-4, //(25)!
    "water_pressure_absolute_tolerance": 1.0E-9, //(26)!
	"residual_relative_tolerance": 1.0E-4, //(27)!
    "residual_absolute_tolerance": 1.0E-9, //(28)!
	"min_iterations": 6, //(29)!
    "max_iterations": 15, //(30)!
    "number_cycles": 10, //(31)!
    "reduction_factor": 0.5, //(32)!
    "increase_factor": 2.0, //(33)!
	"desired_iterations": 4, //(34)!
	"max_radius_factor": 10.0 //(35)!
	"min_radius_factor": 0.1 //(36)!
	"calculate_reactions": true, //(37)!
	"max_line_search_iterations": 5, //(38)!
	"first_alpha_value": 0.5, //(39)!
	"second_alpha_value": 1.0, //(40)!
	"min_alpha": 0.1, //(41)!
	"max_alpha": 2.0, //(42)!
	"line_search_tolerance": 0.5, //(43)!
	"rotation_dofs": true, //(44)!
	"linear_solver_settings": { //(45)!
      "solver_type": "LinearSolversApplication.sparse_lu", //(46)!
      "scaling": true //(47)!
    },
	"problem_domain_sub_model_part_list": [ ],  //(48)!
	"processes_sub_model_part_list": [ ],  //(49)!
	"body_domain_sub_model_part_list": [ ],  //(50)!
	"newmark_beta": 0.25,   //(51)!
    "newmark_gamma": 0.5,   //(52)!
    "newmark_theta": 0.5,   //(53)!
    "rayleigh_m": 0.0,   //(54)!
    "rayleigh_k": 0.0,  //(55)!
	"max_piping_iterations": 500,  //(56)!
  },
```

1. Analysis type, here denoted as solver type: </br>
If "OpenMP": `U_Pw == geomechanics_U_Pw_solver`, `Pw==geomechanics_pw_solver`, `T==geomechanics_T_solver` </br>
2. Name of the model part selected for the computation. Type: string.
3. Working space dimension. Type: integer, e.g. 2 for 2D and 3 for 3D.
4. Format of the model input file. Type: string.
5. Name of the model input file. Type: string.
6. Material parameter file.
7. Information about the time-stepping.
8. Initial time step size.
9. Maximum scaling factor for next time step.
10. Tolerance to avoid very small time steps.
11. Number of solution vectors to keep. Type: integer. Here: always 2.
12. Level of logging. Type: integer.
13. Solver storage behaviour. Type: boolean.
14. Function to compute stress/internal/reaction forces. Type: boolean.
15. Update nodal positions with displacement. Type: boolean.
16. Function to rebuild the system with its degrees of freedom at each step. Type: boolean.
17. Implementation detail of Kratos. Type: boolean. Here: always true.
18. Calculation type. Type: string. Allowed values: `static`, `quasi_static`, `dynamic`, `transient_groundwater_flow`, `steady_state_groundwater_flow`.
19. Time integration scheme. Type: string. Allowed values: `newmark`, `backward_euler`
20. Function to reset total displacements/rotations at stage start. Type: boolean.
21. Iterative strategy. Type: string. Allowed values: `newton_raphson`, `newton_raphson_with_piping`, `linear`, `line_search`
22. Convergence criterion type. Type: string. Allowed values: `displacement_criterion`, `water_pressure_criterion`, `residual_criterion`
23. Relative tolerance for displacement convergence criterion. Type = float.
24. Absolute tolerance for displacement convergence criterion. Type = float.
25. Relative tolerance for water pressure convergence criterion. Type = float.
26. Absolute tolerance for water pressure convergence criterion. Type = float.
27. Relative tolerance for residual force convergence criterion. Type = float.
28. Absolute tolerance for residual force convergence criterion. Type = float.
29. Minimum amount of simulation iterations. If converged below this iteration count the simulation will continue. Type: integer.
30. Maximum amount of simulation iterations. If not converged above this value, the simulation will give an error saying it did not converge. Type: integer.
31. Maximum number of scaled-down retry cycles.
32. Time-step reduction factor.
33. Time-step increase factor.
34. Arc-length parameter.
35. Arc-length parameter.
36. Arc-length parameter.
37. Reaction calculation toggle.
38. Line-search parameter.
39. Line-search parameter.
40. Line-search parameter.
41. Line-search parameter.
42. Line-search parameter.
43. Line-search parameter.
44. Include rotational degrees of freedom.
45. Linear equation solver settings.
46. Supported options include `amgcl`, `bicgstab`, `cg`, `sparse_lu`, `sparse_qr`, `tfqmr` and others
47. Solver scaling toggle
48. List of elements e.g. soil, beams, anchors, and interfaces
49. List of conditions e.g. boundary conditions, loads, water conditions and etc.
50. List of elements e.g. soils, beams, anchors
51. GN22 Average constant acceleration (Middle point rule) is obtained by setting $\gamma$ = 0.5 and $\beta$ = 0.25
52. GN22 Average constant acceleration (Middle point rule) is obtained by setting $\gamma$ = 0.5 and $\beta$ = 0.25
53. GN11 used for the time integration of the water pressure D.O.F.
54. Factor for the mass matrix contribution to the damping matrix
55. Factor for the stiffness matrix contribution to the damping matrix
56. Maximum number of piping iterations

### processes block structure format
```json
"processes": {
    "constraints_process_list": [ ], //(1)!
    "loads_process_list": [ ], //(2)!
    "auxiliary_process_list": [ ] //(3)!
  },
"output_processes": { } //(4)!
```

1. List of constraint processes applied during the simulation. Defines boundary conditions and constraints imposed on the model. </br>
 Type: array of objects. [Details](#constraints_process_list-block-structure-format)
2. List of load processes applied during the simulation. Defines external loads such as forces and pressures. </br> 
Type: array of objects. [Details](#loads_process_list-block-structure-format)
3. List of auxiliary processes used during the simulation. Defines additional processes that support the simulation, such as the k0 procedure. </br>
Type: array of objects. [Details](#auxiliar_process_list-block-structure-format)
4. Output process configuration. Defines processes responsible for writing simulation results. [Details](#output_processes-block-structure-format)

#### constraints_process_list block structure format

Displacement boundary conditions processes are used for displacement boundary conditions such as fixities, sliders, rollers, and hinges.

```json
{
  "python_module": "apply_vector_constraint_table_process",
  "kratos_module": "KratosMultiphysics.GeoMechanicsApplication",
  "process_name": "ApplyVectorConstraintTableProcess",
  "Parameters": {
    "model_part_name": "PorousDomain.xxx", //(1)!
    "variable_name": "DISPLACEMENT", //(2)!
    "active": [true, true, true], //(3)!
    "is_fixed": [true, true, true], //(4)!
    "value": [0.0, 0.0, 0.0], //(5)!
    "table": [0, 0, 0] //(6)!
  }
}
```

1. {{ model_part_name }}
2. {{ variable_name }}
3. {{ active }}
4. {{ is_fixed }}
5. {{ value }}
6. {{ table }}

Hydrostatic water pressure boundary conditions process are used for pore water pressure boundary conditions with hydrostatic increase in depth direction.

```json
{
  "python_module": "apply_scalar_constraint_table_process",
  "kratos_module": "KratosMultiphysics.GeoMechanicsApplication",
  "process_name": "ApplyScalarConstraintTableProcess",
  "Parameters": {
    "model_part_name": "PorousDomain.xxx", //(1)!
    "variable_name": "WATER_PRESSURE", //(2)!
    "is_fixed": true, //(3)!
    "fluid_pressure_type": "Hydrostatic", //(5)!
    "gravity_direction": 1, //(4)!
    "reference_coordinate": -25.0, //(6)!
    "table": 0, //(7)!
    "pressure_tension_cut_off": 0.0, //(8)!
    "specific_weight": 9810.0 //(9)!
  }
}
```

1. {{ model_part_name }}
2. {{ variable_name }}
3. Dirichlet (`true`) or initial value (`false`)
4. `Hydrostatic`, `Uniform`, etc.
5. 0, 1, 2 for X, Y, Z
6. Phreatic surface coordinate in gravity direction
7. {{ table }}
8. Threshold value to eliminate suction
9. Density of water times gravity


#### loads_process_list block structure format
Gravity load process are used for gravity/self-weight/body-acceleration loads.

```json
{
  "python_module": "apply_vector_constraint_table_process",
  "kratos_module": "KratosMultiphysics.GeoMechanicsApplication",
  "process_name": "ApplyVectorConstraintTableProcess",
  "Parameters": {
    "model_part_name": "PorousDomain.xxx", //(1)!
    "variable_name": "VOLUME_ACCELERATION", //(2)!
    "active": [false, true, false], //(3)!
    "value": [0.0, -9.81, 0.0], //(4)!
    "table": [0, 0, 0] //(5)!
  }
}
```

1. {{ model_part_name }}
2. {{ variable_name }}
3. {{ active }}
4. {{ value }}
5. {{ table }}

#### auxiliar_process_list block structure format
As an example of an auxiliary process, the K0 procedure showed here. The K0 procedure is used to initialize the horizontal stresses in a soil profile from a given vertical stress profile.

```json
{
  "python_module": "apply_k0_procedure_process",
  "kratos_module": "KratosMultiphysics.GeoMechanicsApplication",
  "process_name": "ApplyK0ProcedureProcess",
  "Parameters": {
    "model_part_name_list": "PorousDomain.xxx", //(1)!
    "variable_name": "CAUCHY_STRESS_TENSOR", //(2)!
	"use_standard_procedure": true //(3)!
  }
}
```

1. List of model parts that are taken into account in the given process. Type: array of strings. Allowed values: Each entry should start with the above defined model part name, followed by the sub-part name as defined in the mesh file. </br>
Note: This can also be a single model part and can then be noted as "model_part_name".
2. Kratos tensor variable that is influenced by the process. (e.g. for k0_procedure usually `CAUCHY_STRESS_TENSOR`)
3. Parameter . Type: boolean. Default value: .

### output_processes block structure format
```json
"output_processes": {
    "gid_output": [	 //(1)!
	    "python_module": "gid_output_process",
        "kratos_module": "KratosMultiphysics",
        "process_name": "GiDOutputProcess",
		"Parameters": {
		    "model_part_name": "PorousDomain.porous_computational_model_part",
		    "output_name": "mesh",
		    "postprocess_parameters": {
				"result_file_configuration": {
				  "gidpost_flags": {
					"WriteDeformedMeshFlag": "WriteUndeformed",
					"WriteConditionsFlag": "WriteElementsOnly",
					"GiDPostMode": "GiD_PostAscii", //(2)!
					"MultiFileFlag": "SingleFile"
				  },
				  "file_label": "step",
				  "output_control_type": "step",
				  "output_interval": 1,
				  "body_output": true,
				  "node_output": false,
				  "skin_output": false,
				  "nodal_results": [ ],  //(3)!
				  "gauss_point_results": [ ]  //(4)!
				}
			}
		}
	]
}
```

1. List of GiD output processes. Type: array of objects.
2. Output format used by GiD. Controls whether results are written in ASCII or binary format. Type = string. Allowed values: "GiD_PostAscii", "GiD_PostBinary".
3. List of nodal result variables to output. Type: array of strings. </br> (e.g. "DISPLACEMENT",
                                            "TOTAL_DISPLACEMENT",
                                            "WATER_PRESSURE",
                                            "REACTION")
4. List of Gauss point (integration point) result variables to output. Type: array of strings. </br> (e.g. "CAUCHY_STRESS_TENSOR",
                                            "TOTAL_STRESS_TENSOR",
                                            "ENGINEERING_STRAIN_TENSOR")