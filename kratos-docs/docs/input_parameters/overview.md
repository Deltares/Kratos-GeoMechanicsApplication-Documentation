# Input Parameters Overview

The Geo-Mechanics Application input is composed of multiple files that work together to define a simulation.

In general:

- `ProjectParameters.json` contains the main analysis settings, solver configuration, processes, and output settings.
- `MaterialParameters.json` contains the material definitions and constitutive-law-related data used by the model.
- `Mesh.mdpa` contains the model part data, such as nodes, elements, conditions, and groups.

These files are read together during the simulation setup. The mesh provides the model structure, the material file defines the physical behavior, and the project parameters describe how the analysis is executed.

Use the pages below for the detailed description of each file:

- [ProjectParameter.json file description](project_parameters.md)
- [MaterialParameters.json file description](material_parameters.md)
- [Mesh.mdpa file description](mesh_file_description.md)
