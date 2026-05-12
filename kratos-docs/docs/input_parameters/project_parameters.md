# ProjectParameter.json file description

The project parameters json-file contains as description of the input of the Kratos simulation. More information can be found on the [Kratos website](https://github.com/KratosMultiphysics/Kratos/wiki/Kratos-input-files-and-IO#3-the-project-parameters-file).
The user is responsible for giving all material parameters a consistent set of parameters.

## ProjectParameter.json structure format
The strucal format of the ProjectParameter.json is described on the Kratos website:

```json
{
  "problem_data": { },  // (1)!
  "solver_settings": { },  // (2)!
  "output_processes": { },  // (3)!
  "processes": { }  // (4)!
}
```

1. General settings for the Kratos run. [Details](./#problem_data-block-structure-format)
2. Settings for the solvers, like analysis type, linear solver, etc. [Details](./#solver_settings-block-structure-format)
3. Settings for the output  [Details](./#output_processes-block-structure-format)
4. Processes to e.g. apply boundary conditions.


### problem_data block structure format

```json
"problem_data": {
  "problem_name": "DSettlement_stage0",  // (1)!
  "start_time": -1E-06,  // (2)!
  "end_time": 0.0,  // (3)!
  "echo_level": 1, // (4)!
  "parallel_type": "OpenMP",  // (5)!
  "number_of_threads": 1  // (6)!
}
```

1. Name of this problem case
2. The start time of this stage in seconds
3. The end time of this stage in seconds
4. {{ echo_level }}
5. Method of parallel computation: "OpenMP"
6. Number of threads for parallel computation

### solver_settings block structure format

```python
"solver_settings": {
    "solver_type": "Pw",  # (1)!
    "model_part_name": "PorousDomain",  # (2)!
    "domain_size": 2,  # (3)!
    "model_import_settings": {
      "input_type": "mdpa",  # (4)!
      "input_filename": "mesh"  # (5)!
    },
    "material_import_settings": {
      "materials_filename": "MaterialParameters.json"  # (6)!
    },
    "time_stepping": {  # (7)!
      "time_step": 1.0,  # (8)!
      "max_delta_time_factor": 1e9  # (9)!
	  "minimum_allowable_value": 0.001  # (10)!
    },
    "buffer_size": 2,  # (11)!
    "echo_level": 1, # (12)!
	"clear_storage": false,  # (13)!
    "compute_reactions": false, # (14)!
    "move_mesh_flag": false, # (15)!
    "reform_dofs_at_each_step": true, # (16)!
    "block_builder": true, # (17)!
    "solution_type": "K0-Procedure", # (18)!
    "scheme_type": "Newmark", # (19)!
    "reset_displacements": false, # (20)!
	"strategy_type": "line_search", #(21)!
	"convergence_criterion": "displacement_criterion", #(22)!
    "water_pressure_relative_tolerance": 1.0E-4, #(23)!
    "water_pressure_absolute_tolerance": 1.0E-9, #(24)!
	"displacement_relative_tolerance": 1.0E-4, #(25)!
    "displacement_absolute_tolerance": 1.0E-9, #(26)!
	"residual_relative_tolerance": 1.0E-4, #(27)!
    "residual_absolute_tolerance": 1.0E-9, #(28)!
	"min_iterations": 6, #(29)!
    "max_iterations": 15, #(30)!
    "number_cycles": 10, #(31)!
    "reduction_factor": 0.5, #(32)!
    "increase_factor": 2.0, #(33)!
	"desired_iterations": 4, #(34)!
	"max_radius_factor": 10.0 #(35)!
	"min_radius_factor": 0.1 #(36)!
	"calculate_reactions": true, #(37)!
	"max_line_search_iterations": 5, #(38)!
	"first_alpha_value": 0.5, #(39)!
	"second_alpha_value": 1.0, #(40)!
	"min_alpha": 0.1, #(41)!
	"max_alpha": 2.0, #(42)!
	"line_search_tolerance": 0.5, #(43)!
	"rotation_dofs": true, #(44)!
	"linear_solver_settings": { #(45)!
      "solver_type": "LinearSolversApplication.sparse_lu", #(46)!
      "scaling": true #(47)!
    },
	"problem_domain_sub_model_part_list": [ ],  #(48)!
	"processes_sub_model_part_list": [ ],  #(49)!
	"body_domain_sub_model_part_list": [ ],  #(50)!
	"newmark_beta": 0.25,   #(51)!
    "newmark_gamma": 0.5,   #(52)!
    "newmark_theta": 0.5,   #(53)!
    "rayleigh_m": 0.0,   #(54)!
    "rayleigh_k": 0.0 },  #(55)!
	"max_piping_iterations": 500,  #(56)!
  },
```

1. Analysis type, here denoted as solver type: </br>
If "OpenMP": `u_pw == geomechanics_u_pw_solver == twophase`, `pw==geomechanics_pw_solver`, dynamic, scipy </br>
If "MPI": dynamic
2. Selection of model parts to use for the computation.
3. Working space dimension
4. Model input format
5. Model input file Name
6. Material parameter file
7. Time-stepping information
8. Initial time step size
9. Maximum scaling factor for next time step
10. Tolerance to avoid very small final time steps
11. Number of solution vectors to keep
12. {{ echo_level }}
13. Solver storage behavior
14. Compute stress/internal/reaction forces
15. Update nodal positions with displacement
16. Rebuild system at each step
17. Builder and solver block mode
18. Calculation type: `quasi_static`, `dynamic`, `k0_procedure`, `transient_groundwater_flow`, `steady_state_groundwater_flow`
19. Time integration scheme: `newmark`, `backward_euler`
20. Reset total displacements/rotations at stage start
21. Iterative strategy: `newton_raphson`, `newton_raphson_with_piping`, `line_search`, `arc_length`
22. Convergence criterion type: `displacement_criterion`, `water_pressure_criterion`, `residual_criterion`
23. Relative tolerance for displacement criterion
24. Absolute tolerance for displacement criterion
25. Relative tolerance for water pressure criterion
26. Absolute tolerance for water pressure criterion
27. Relative tolerance for residual force criterion
28. Absolute tolerance for residual force criterion
29. Increase next step if converged below this iteration count
30. Maximum number of iterations
31. Maximum number of scaled-down retry cycles
32. Time-step reduction factor
33. Time-step increase factor
34. Arc-length parameter
35. Arc-length parameter
36. Arc-length parameter
37. Reaction calculation toggle
38. Line-search parameter
39. Line-search parameter
40. Line-search parameter
41. Line-search parameter
42. Line-search parameter
43. Line-search parameter
44. Include rotational degrees of freedom
45. Linear equation solver settings
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

### output_processes block structure format
```python
"output_processes": {
    "gid_output": [	 #(1)!
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
                "GiDPostMode": "GiD_PostAscii", #(2)!
                "MultiFileFlag": "SingleFile"
              },
              "file_label": "step",
              "output_control_type": "step",
              "output_interval": 1,
              "body_output": true,
              "node_output": false,
              "skin_output": false,
              "nodal_results": [ ],  #(3)!
              "gauss_point_results": [ ]  #(4)!
		
	]
  },
```

1. Description of output file writer for the GiD postprocessor
2. Write results in GiD binary or ASCII
3. Nodal output results
4. Gauss-point output results

### processes block structure format
```python
"output_processes": {
    "constraints_process_list": [ ] #(1)!
    "loads_process_list": [ ] #(2)!
    "auxiliar_process_list": [ ] #(3)!
  },
```

1. Constraint process list [Details](./#constraints_process_list-block-structure-format)
2. Load process list [Details](./#loads_process_list-block-structure-format)
3. Auxiliary process list [Details](./#auxiliar_process_list-block-structure-format)

#### constraints_process_list block structure format

Displacement boundary conditions processes are used for displacement boundary conditions such as fixities, sliders, rollers, and hinges.

```python
{
  "python_module": "apply_vector_constraint_table_process",
  "kratos_module": "KratosMultiphysics.GeoMechanicsApplication",
  "process_name": "ApplyVectorConstraintTableProcess",
  "Parameters": {
    "model_part_name": "PorousDomain.xxx", #(1)!
    "variable_name": "DISPLACEMENT", #(2)!
    "active": [true, true, true], #(3)!
    "is_fixed": [true, true, true], #(4)!
    "value": [0.0, 0.0, 0.0], #(5)!
    "table": [0, 0, 0] #(6)!
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

```python
{
  "python_module": "apply_scalar_constraint_table_process",
  "kratos_module": "KratosMultiphysics.GeoMechanicsApplication",
  "process_name": "ApplyScalarConstraintTableProcess",
  "Parameters": {
    "model_part_name": "PorousDomain.xxx", #(1)!
    "variable_name": "WATER_PRESSURE", #(2)!
    "is_fixed": true, #(3)!
    "fluid_pressure_type": "Hydrostatic", #(5)!
    "gravity_direction": 1, #(4)!
    "reference_coordinate": -25.0, #(6)!
    "table": 0, #(7)!
    "pressure_tension_cut_off": 0.0, #(8)!
    "specific_weight": 9810.0 #(9)!
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

```python
{
  "python_module": "apply_vector_constraint_table_process",
  "kratos_module": "KratosMultiphysics.GeoMechanicsApplication",
  "process_name": "ApplyVectorConstraintTableProcess",
  "Parameters": {
    "model_part_name": "PorousDomain.xxx", #(1)!
    "variable_name": "VOLUME_ACCELERATION", #(2)!
    "active": [false, true, false], #(3)!
    "value": [0.0, -9.81, 0.0], #(4)!
    "table": [0, 0, 0] #(5)!
  }
}
```

1. {{ model_part_name }}
2. {{ variable_name }}
3. {{ active }}
4. {{ value }}
5. {{ table }}

#### auxiliar_process_list block structure format

K0 procedure process is used for K0 procedure after stress initialization.

```python
{
  "python_module": "apply_k0_procedure_process",
  "kratos_module": "KratosMultiphysics.GeoMechanicsApplication",
  "process_name": "ApplyK0ProcedureProcess",
  "Parameters": {
    "model_part_name": "PorousDomain.xxx", #(1)!
    "variable_name": "CAUCHY_STRESS_TENSOR" #(2)!
  }
}
```

1. {{ model_part_name }}
2. Kratos tensor variable for K0, usually `CAUCHY_STRESS_TENSOR`