# ProjectParameter.json file description

The project parameters json-file contains as description of the input of the Kratos simulation. More information can be found on the [Kratos website](https://github.com/KratosMultiphysics/Kratos/wiki/Kratos-input-files-and-IO#3-the-project-parameters-file).
The user is responsible for giving all material parameters a consistent set of parameters.

## ProjectParameter.json structure format
The strucal format of the ProjectParameter.json is described on the Kratos website:

```python
{
  "problem_data": { },  # (1)!
  "solver_settings": { },  # (2)!
  "output_processes": { },  # (3)!
  "processes": { }  # (4)!
}
```

1. General settings for the Kratos run. [Details](./#problem_data-block-structure-format)
2. Settings for the solvers, like analysis type, linear solver, etc. [Details](./#solver_settings-block-structure-format)
3. Processes to e.g. apply boundary conditions.
4. Settings for the output 

### problem_data block structure format

```python
"problem_data": {
  "problem_name": "DSettlement_stage0",  # (1)!
  "start_time": -1E-06,  # (2)!
  "end_time": 0.0,  # (3)!
  "echo_level": 1, # (4)!
  "parallel_type": "OpenMP",  # (5)!
  "number_of_threads": 1  # (6)!
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
      "input_type": "mdpa",
      "input_filename": "mesh"
    },
    "material_import_settings": {
      "materials_filename": "MaterialParameters.json"
    },
    "time_stepping": {
      "time_step": 1.0,
      "max_delta_time_factor": 1e9
    },
    "buffer_size": 2,
    "echo_level": 1, # (4)!
    "compute_reactions": false,
    "move_mesh_flag": false,
    "reform_dofs_at_each_step": true,
    "block_builder": true,
    "solution_type": "Steady-State-Groundwater-Flow",
    "scheme_type": "Backward_Euler",
    "reset_displacements": false,
    "newmark_beta": 0.25,
    "newmark_gamma": 0.5,
    "newmark_theta": 0.5,
    "rayleigh_m": 0.0,
    "rayleigh_k": 0.0,
    "strategy_type": "newton_raphson",
    "max_piping_iterations": 500,
    "convergence_criterion": "water_pressure_criterion",
    "water_pressure_relative_tolerance": 1.0E-4,
    "water_pressure_absolute_tolerance": 1.0E-9,
    "min_iterations": 6,
    "max_iterations": 15,
    "number_cycles": 10,
    "reduction_factor": 0.5,
    "increase_factor": 2.0,
    "calculate_reactions": true,
    "max_line_search_iterations": 5,
    "first_alpha_value": 0.5,
    "second_alpha_value": 1.0,
    "min_alpha": 0.1,
    "max_alpha": 2.0,
    "line_search_tolerance": 0.5,
    "linear_solver_settings": {
      "solver_type": "LinearSolversApplication.sparse_lu",
      "scaling": true
    },
    "problem_domain_sub_model_part_list": [
      "Soil-0",
      "Soil-1",
      "Soil-2",
      "Soil-3",
      "Soil-4",
      "Soil-5"
    ],
    "body_domain_sub_model_part_list": [
      "Soil-0",
      "Soil-1",
      "Soil-2",
      "Soil-3",
      "Soil-4",
      "Soil-5"
    ]
  },
```

1. Analysis type, here denoted as solver type: </br>
If "OpenMP": `u_pw == geomechanics_u_pw_solver == twophase`, `pw==geomechanics_pw_solver`, dynamic, scipy </br>
If "MPI": dynamic
2. Selection of model parts to use for the computation.
3. Working space dimension
4. {{ echo_level }}

# <<<<<<<<<<<< OLD BELOW HERE >>>>>>>>>>>>

# ProjectParameter.json file description

## Main ProjectParameters structure

| Parameters | Description |
| --- | --- |
| `"problem_data": {` | Problem data |
| `"problem_name": "DSettlement_stage0"` | Name of this problem case |
| `"start_time": -1E-06` | Start time of this stage in seconds |
| `"end_time": 0.0` | End time of this stage in seconds |
| `"echo_level": 1` | Level of logging |
| `"parallel_type": "OpenMP"` | Method of parallel computation |
| `"number_of_threads": 1` | Number of threads for parallel computation |
| `"solver_settings": {` | Steering parameters of the analysis |
| `"solver_type": "U_Pw"` | Analysis type (OpenMP: u_pw/geomechanics_u_pw_solver/twophase/pw/geomechanics_pw_solver/dynamic/scipy, MPI: dynamic) |
| `"model_part_name": "PorousDomain"` | Selection of model parts to use for computation |
| `"domain_size": 2` | Working space dimension |
| `"model_import_settings": { "input_type": "mdpa", "input_filename": "mesh_stage0" }` | Model input format and file |
| `"material_import_settings": { "materials_filename": "MaterialParameters.json" }` | Material parameter file |
| `"time_stepping": { ... }` | Time-stepping information |
| `"time_step"` | Initial time step size |
| `"max_delta_time_factor"` | Maximum scaling factor for next time step |
| `"minimum_allowable_value"` | Tolerance to avoid very small final time steps |
| `"buffer_size": 2` | Number of solution vectors to keep |
| `"clear_storage": false` | Solver storage behavior |
| `"compute_reactions": false` | Compute stress/internal/reaction forces |
| `"move_mesh_flag": false` | Update nodal positions with displacement |
| `"reform_dofs_at_each_step": false` | Rebuild system at each step |
| `"block_builder": true` | Builder and solver block mode |
| `"solution_type": "K0-Procedure"` | Calculation type: quasi_static, dynamic, k0_procedure, transient_groundwater_flow, steady_state_groundwater_flow |
| `"scheme_type": "Newmark"` | Time integration scheme: newmark, backward_euler |
| `"reset_displacements": true` | Reset total displacements/rotations at stage start |
| `"strategy_type": "line_search"` | Iterative strategy: newton_raphson, newton_raphson_with_piping, line_search, arc_length |
| `"convergence_criterion": "displacement_criterion"` | Convergence criterion type |
| `"water_pressure_relative_tolerance"` | Relative tolerance |
| `"water_pressure_absolute_tolerance"` | Absolute tolerance |
| `"displacement_relative_tolerance"` | Relative tolerance |
| `"displacement_absolute_tolerance"` | Absolute tolerance |
| `"residual_relative_tolerance"` | Relative tolerance |
| `"residual_absolute_tolerance"` | Absolute tolerance |
| `"min_iterations": 6` | Increase next step if converged below this iteration count |
| `"max_iterations": 15` | Maximum number of iterations |
| `"number_cycles": 100` | Maximum number of scaled-down retry cycles |
| `"reduction_factor": 0.5` | Time-step reduction factor |
| `"increase_factor": 2.0` | Time-step increase factor |
| `"desired_iterations": 4` | Arc-length parameter |
| `"max_radius_factor": 10.0` | Arc-length parameter |
| `"min_radius_factor": 0.1` | Arc-length parameter |
| `"calculate_reactions": true` | Reaction calculation toggle |
| `"max_line_search_iterations": 5` | Line-search parameter |
| `"first_alpha_value": 0.5` | Line-search parameter |
| `"second_alpha_value": 1.0` | Line-search parameter |
| `"min_alpha": 0.1` | Line-search parameter |
| `"max_alpha": 2.0` | Line-search parameter |
| `"line_search_tolerance": 0.5` | Line-search parameter |
| `"rotation_dofs": true` | Include rotational degrees of freedom |
| `"linear_solver_settings": { ... }` | Linear equation solver settings |
| `"linear_solver_settings.solver_type": "LinearSolversApplication.sparse_lu"` | Supported options include amgcl, bicgstab, cg, sparse_lu, sparse_qr, tfqmr and others |
| `"linear_solver_settings.scaling": true` | Solver scaling setting |
| `"problem_domain_sub_model_part_list"` | List of elements (soil, beams, anchors, interfaces) |
| `"processes_sub_model_part_list"` | List of conditions (BCs, loads, water conditions, etc.) |
| `"body_domain_sub_model_part_list"` | List of body elements |
| `"newmark_beta": 0.25` | Newmark parameter |
| `"newmark_gamma": 0.5` | Newmark parameter |
| `"newmark_theta": 0.5` | Time integration parameter for water pressure DOF |
| `"rayleigh_m": 0.0` | Mass contribution to damping |
| `"rayleigh_k": 0.0` | Stiffness contribution to damping |
| `"output_processes": {` | Post-process settings |
| `"gid_output": [...]` | Write output files for GiD postprocessor |
| `"GiDPostMode": "GiD_PostAscii"` | Write results in GiD binary or ASCII |
| `"nodal_results": [...]` | Nodal output results |
| `"gauss_point_results": [...]` | Gauss-point output results |
| `"processes": {` | Begin process lists |
| `"constraints_process_list": [...]` | Constraint process list |
| `"loads_process_list": [...]` | Load process list |
| `"auxiliar_process_list": [...]` | Auxiliary process list |

## Displacement boundary conditions process

Placed in `constraints_process_list`.

Used for displacement boundary conditions such as fixities, sliders, rollers, and hinges.

```json
{
  "python_module": "apply_vector_constraint_table_process",
  "kratos_module": "KratosMultiphysics.GeoMechanicsApplication",
  "process_name": "ApplyVectorConstraintTableProcess",
  "Parameters": {
    "model_part_name": "PorousDomain.xxx",
    "variable_name": "DISPLACEMENT",
    "active": [true, true, true],
    "is_fixed": [true, true, true],
    "value": [0.0, 0.0, 0.0],
    "table": [0, 0, 0]
  }
}
```

| Parameter | Description |
| --- | --- |
| `model_part_name` | Body part to apply the process to. `PorousDomain.` is required |
| `variable_name` | Kratos vector variable |
| `active` | Activation per vector component (X, Y, Z) |
| `is_fixed` | Fix/free per vector component (X, Y, Z) |
| `value` | Prescribed value per component |
| `table` | Time-table reference per component |

## Hydrostatic water pressure boundary conditions process

Placed in `constraints_process_list`.

Used for pore water pressure boundary conditions with hydrostatic increase in depth direction.

```json
{
  "python_module": "apply_scalar_constraint_table_process",
  "kratos_module": "KratosMultiphysics.GeoMechanicsApplication",
  "process_name": "ApplyScalarConstraintTableProcess",
  "Parameters": {
    "model_part_name": "PorousDomain.xxx",
    "variable_name": "WATER_PRESSURE",
    "is_fixed": true,
    "fluid_pressure_type": "Hydrostatic",
    "gravity_direction": 1,
    "reference_coordinate": -25.0,
    "table": 0,
    "pressure_tension_cut_off": 0.0,
    "specific_weight": 9810.0
  }
}
```

| Parameter | Description |
| --- | --- |
| `model_part_name` | Body part to apply the process to. `PorousDomain.` is required |
| `variable_name` | Kratos scalar variable |
| `is_fixed` | Dirichlet (`true`) or initial value (`false`) |
| `fluid_pressure_type` | `Hydrostatic`, `Uniform`, etc. |
| `gravity_direction` | 0, 1, 2 for X, Y, Z |
| `reference_coordinate` | Phreatic surface coordinate in gravity direction |
| `table` | Time-table reference |
| `pressure_tension_cut_off` | Threshold value to eliminate suction |
| `specific_weight` | Density of water times gravity |

## Gravity load process

Placed in `loads_process_list`.

Used for gravity/self-weight/body-acceleration loads.

```json
{
  "python_module": "apply_vector_constraint_table_process",
  "kratos_module": "KratosMultiphysics.GeoMechanicsApplication",
  "process_name": "ApplyVectorConstraintTableProcess",
  "Parameters": {
    "model_part_name": "PorousDomain.xxx",
    "variable_name": "VOLUME_ACCELERATION",
    "active": [false, true, false],
    "value": [0.0, -9.81, 0.0],
    "table": [0, 0, 0]
  }
}
```

| Parameter | Description |
| --- | --- |
| `model_part_name` | Body part to apply load conditions to |
| `variable_name` | Kratos vector variable |
| `active` | Activation per component (X, Y, Z) |
| `value` | Prescribed value per component |
| `table` | Time-table reference per component |

## K0 procedure process

Placed in `auxiliar_process_list`.

Used for K0 procedure after stress initialization.

```json
{
  "python_module": "apply_k0_procedure_process",
  "kratos_module": "KratosMultiphysics.GeoMechanicsApplication",
  "process_name": "ApplyK0ProcedureProcess",
  "Parameters": {
    "model_part_name": "PorousDomain.xxx",
    "variable_name": "CAUCHY_STRESS_TENSOR"
  }
}
```

| Parameter | Description |
| --- | --- |
| `model_part_name` | Body part to apply the K0 procedure to |
| `variable_name` | Kratos tensor variable for K0, usually `CAUCHY_STRESS_TENSOR` |

## References

More general information can be found on the Kratos website:

- https://github.com/KratosMultiphysics/Kratos/wiki/Kratos-input-files-and-IO#3-the-project-parameters-file