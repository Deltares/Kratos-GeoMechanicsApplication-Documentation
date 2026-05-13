# User Documentation

This section provides an overview of the user-facing documentation and links to the detailed reference pages.

## Input Parameters

The Geo-Mechanics Application input is typically distributed over multiple files. Together, these files define the model geometry, the materials, and the simulation settings.

In general:

- `ProjectParameters.json` contains the main analysis settings, solver configuration, processes, and output settings.
- `MaterialParameters.json` contains the material definitions and constitutive-law-related data used by the model.
- `Mesh.mdpa` contains the model part data, such as nodes, elements, conditions, and groups.

These files are read together during the simulation setup. The mesh provides the model structure, the material file defines the physical behavior, and the project parameters describe how the analysis is executed.

## User Documentation Index

Use the pages below for the detailed description of each file.

- [ProjectParameter.json file description](input_parameters/project_parameters.md)
- [MaterialParameters.json file description](input_parameters/material_parameters.md)
- [Mesh.mdpa file description](input_parameters/mesh_file_description.md)