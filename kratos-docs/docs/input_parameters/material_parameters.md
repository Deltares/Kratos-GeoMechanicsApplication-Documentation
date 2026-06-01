# MaterialParameters.json file description

The material parameters json-file contains descriptions of several material models and their properties which can be adopted by a Kratos simulation. 
The user is responsible for giving all material parameters a consistent set of parameters.

By clicking on an annotation (1) the user is provided more detailed information about a property.
{ .annotate }

1. Here more information about an annotation can be found.


The structural format of the MaterialParameters.json is as follows:

```json
{
  "properties": [ //(1)!
    {
      "model_part_name": "PorousDomain.Soil-0", //(2)!
      "properties_id": 0, //(3)!
      "Material": { //(4)!
        "constitutive_law": { //(5)!
          "name": "GeoLinearElasticPlaneStrain2DLaw" //(6)!
        },
        "Variables": { } //(7)!
      }
    }
  ]
}
```

1. Start of the properties list.
2. Name of the model part to which this material will be assigned. Type: string.
3. Unique ID of this material. Type: integer.
4. Start of the material description.
5. Definition of the constitutive law.
6. Name of the soil constitutive law. Type: string. Supported names include [`GeoLinearElasticPlaneStrain2DLaw`](#incremental-linear-elastic-law-for-plane-strain-models),  [`SmallStrainUDSM2DPlaneStrainLaw`](#constitutive-law-smallstrainudsm2dplanestrainlaw)
7. Material properties relevant for the current constitutive law.

When a project needs various materials, multiple items can be added to the properties list, each having its own unique ID and possibly varying constitutive laws and/or material properties.

For geomechanical materials, the "Variables" section consists of three parts:

1. `GEO_DRAINAGE_TYPE`: {{ geo_drainage_type }} Details can be found [here](#drainage-types).
2. [Material properties of the soil skeleton](#material-properties-of-the-soil-skeleton).
3. A description of the groundwater flow. This includes the [permeability](#permeability) and a [retention law](#retention-laws).


## Drainage types

At present, the GeoMechanicsApplication supports two drainage types:

1. **Fully coupled.** When this type is selected, the simulation will solve for the displacement field as well as the pore water pressure field in a coupled manner. In other words, the displacement field affects the pore water pressure field and vice versa.
2. **Keeping the pore water pressure field constant.** When this type is selected, the simulation will solve for the displacement  field only. The pore water pressure field is kept constant, i.e. the pore water pressure degrees of freedom remain unchanged. Only the effect of the pore water pressure field on the displacement field is taken into account for the coupling.


## Material properties of the soil skeleton

```json
{
    "YOUNG_MODULUS": 1.0E+05, //(1)!
    "POISSON_RATIO": 0.25, //(2)!
    "POROSITY": 0.45, //(3)!
    "DENSITY_SOLID": 1.83486e+03, //(4)!
    "DENSITY_WATER": 1.01937e+03, //(5)!
    "BULK_MODULUS_SOLID": 1.0e+10, //(6)!
    "BULK_MODULUS_FLUID": 2.2e+09 //(7)!
    
}
```

1. {{ youngs_modulus }}
2. {{ poissons_ratio }}
3. {{ porosity }}
4. {{ density_solid }}
5. {{ density_water }}
6. {{ bulk_modulus_solid }}
7. {{ bulk_modulus_fluid }}


## Permeability

The permeability describes the groundwater flow in the pores.

```json
{
  "PERMEABILITY_XX": 7.0E-11, //(1)!
  "PERMEABILITY_YY": 7.0E-11, //(2)!
  "PERMEABILITY_XY": 0.0, //(3)!
  "PERMEABILITY_ZZ": 7.0E-11, //(4)!
  "PERMEABILITY_YZ": 0.0, //(5)!
  "PERMEABILITY_ZX": 0.0, //(6)!
  "DYNAMIC_VISCOSITY": 0.0013, //(7)!
  "PERMEABILITY_CHANGE_INVERSE_FACTOR": 0.0 //(8)!
}
```

1. {{ permeability_xx }}
2. {{ permeability_yy }}
3. {{ permeability_xy }}
4. {{ permeability_zz }}
5. {{ permeability_yz }}
6. {{ permeability_zx }}
7. {{ dynamic_viscosity }}
8. {{ permeability_change_inverse_factor }}


## Retention laws

A retention law determines the pressure-dependent relative conductivity and storage capacity. The GeoMechanicsApplication supports several ways to describe this behavior by supplying one of the following strings for the setting `"RETENTION_LAW"`:

- `"SaturatedLaw"`
- `"SaturatedBelowPhreaticLevelLaw"`
- `"VanGenuchtenLaw"`


### Fully saturated

For a fully saturated retention law, the relative permeability is always equal to 1.0, and the storage capacity equals 0.0. The saturation always equals the specified value.

```json
{
    "RETENTION_LAW": "SaturatedLaw",
    "SATURATED_SATURATION": 1.0 //(1)!
}
```

1. {{ saturated_saturation }}


### Saturated below the phreatic level

Below the phreatic level, the pores are assumed to be fully saturated as for the case of a fully saturated retention law. Above the phreatic level, there remains some pore water content indicated by a residual saturation as well as a minimum relative permeability.

```json
{
    "RETENTION_LAW": "SaturatedBelowPhreaticLevelLaw",
    "SATURATED_SATURATION": 1.0, //(1)!
    "RESIDUAL_SATURATION": 0.1, //(2)!
    "MINIMUM_RELATIVE_PERMEABILITY": 1.0E-04 //(3)!
}
```

1. {{ saturated_saturation_with_minimum_value }}
2. {{ residual_saturation }}
3. {{ minimum_relative_permeability }}


### Retention law according to Van Genuchten

This retention law adopts the formulation proposed by Van Genuchten.

```json
{
    "RETENTION_LAW": "VanGenuchtenLaw",
    "SATURATED_SATURATION": 1.0, //(1)!
    "RESIDUAL_SATURATION": 0.1, //(2)!
    "MINIMUM_RELATIVE_PERMEABILITY": 1.0E-04, //(3)!
    "VAN_GENUCHTEN_AIR_ENTRY_PRESSURE": 2.561, //(4)!
    "VAN_GENUCHTEN_GN": 1.377, //(5)!
    "VAN_GENUCHTEN_GL": 1.25 //(6)!
}
```

1. {{ saturated_saturation_with_minimum_value }}
2. {{ residual_saturation }}
3. {{ minimum_relative_permeability }}
4. Air entry pressure (e.g. in Pa). Type: float. Range: (0.0, ->.
5. Parameter GN. Type: float. Range: (0.0, ->.
6. Parameter GL. Type: float. Range: (0.0, ->.


## Incremental linear elastic law for plane strain models

`GeoLinearElasticPlaneStrain2DLaw` is an incremental linear elastic constitutive law that is to be used by plane strain models only. It supports the following set of material properties.

```json
{
  "GEO_DRAINAGE_TYPE": "CONSTANT_PW_FIELD", //(1)!
  "YOUNG_MODULUS": 10000.0, //(2)!
  "POISSON_RATIO": 0.2, //(3)!
  "DENSITY_SOLID": 2650.0, //(4)!
  "DENSITY_WATER": 1000.0, //(5)!
  "POROSITY": 0.3, //(6)!
  "BULK_MODULUS_SOLID": 1.0E+10, //(7)!
  "BULK_MODULUS_FLUID": 2.2E+09, //(8)!
  "PERMEABILITY_XX": 6.901970778117567E-11, //(9)!
  "PERMEABILITY_YY": 6.901970778117567E-11, //(10)!
  "PERMEABILITY_XY": 0, //(11)!
  "PERMEABILITY_CHANGE_INVERSE_FACTOR": 0, //(12)!
  "DYNAMIC_VISCOSITY": 0.0013, //(13)!
  "K0_MAIN_DIRECTION": 1, //(14)!
  "K0_NC": 0, //(15)!
  "INDEX_OF_UMAT_PHI_PARAMETER": 1, //(16)!
  "K0_VALUE_XX": 0, //(17)!
  "K0_VALUE_YY": 0, //(18)!
  "K0_VALUE_ZZ": 0, //(19)!
  "OCR": 1.3, //((20)!
  "POISSON_UNLOADING_RELOADING": 0.3 , //((21)!
  "BIOT_COEFFICIENT": 1, //(22)!
  "RETENTION_LAW": "SaturatedLaw", //(23)!
  "SATURATED_SATURATION": 1 //(24)!
  "RESIDUAL_SATURATION": 0 //(25)!
  "VAN_GENUCHTEN_AIR_ENTRY_PRESSURE": 0 //(26)!
  "VAN_GENUCHTEN_GN": 0 //(27)!
  "VAN_GENUCHTEN_GL": 0 //(28)!
  "MINIMUM_RELATIVE_PERMEABILITY": 0 //(29)!
  "Tables": {} //(30)!
}
```

1. {{ geo_drainage_type }}
2. {{ youngs_modulus }}
3. {{ poissons_ratio }}
4. {{ density_solid }}
5. {{ density_water }}
6. {{ porosity }}
7. {{ bulk_modulus_solid }}
8. {{ bulk_modulus_fluid }}
9. {{ permeability_xx }}
10. {{ permeability_yy }}
11. {{ permeability_xy }}
12. {{ permeability_change_inverse_factor }}
13. {{ dynamic_viscosity }} 
14. Input `0` for X, `1` for Y, and `2` for Z direction. Direction (v) from which stress in perpendicular directions (h) is derived: `sigma_hh = K0 * sigma_vv`
15. K0 value for normal consolidation
16. The index of phi in the UMAT parameters
17. K0 value in the XX direction
18. K0 value in the YY direction
19. K0 value in the ZZ direction
20. (Optional) Over consolidation ratio
21. (Optional) Poisson's ratio under unloading and reloading
22. {{ biot_coefficient }}
23. {{ retention_law }}
24. {{ saturated_saturation }}
25. {{ residual_saturation }}
26. Coefficient for Van Genuchten curve
27. Coefficient for Van Genuchten curve
28. Coefficient for Van Genuchten curve
29. {{ minimum_relative_permeability }}
30. Optional tables

## Constitutive law: SmallStrainUDSM2DPlaneStrainLaw

When `SmallStrainUDSM2DPlaneStrainLaw` is set as the name of the constitutive law, the structural format `Variables`-block is as follows:

```json
{
  "IGNORE_UNDRAINED": false, //(1)!
  "DENSITY_SOLID": 2650, //(2)!
  "DENSITY_WATER": 1000, //(3)!
  "POROSITY": 0.3, //(4)!
  "BULK_MODULUS_SOLID": 20000000000, //(5)!
  "BULK_MODULUS_FLUID": 2200000000, //(6)!
  "PERMEABILITY_XX": 6.901970778117567E-11, //(7)!
  "PERMEABILITY_YY": 6.901970778117567E-11, //(8)!
  "PERMEABILITY_XY": 0, //(9)!
  "PERMEABILITY_CHANGE_INVERSE_FACTOR": 0, //(10)!
  "DYNAMIC_VISCOSITY": 0.0013, //(11)!
  "BIOT_COEFFICIENT": 1, //(12)!
  "RETENTION_LAW": "SaturatedLaw", //(13)!
  "SATURATED_SATURATION": 1 //(14)!
  "RESIDUAL_SATURATION": 0 //(15)!
  "MINIMUM_RELATIVE_PERMEABILITY": 0 //(16)!
  "UDSM_NAME": "UDSM.dll", //(17)!
  "UDSM_NUMBER": 1, //(18)!
  "IS_FORTRAN_UDSM": true, //(19)!
  "UMAT_PARAMETERS": [ ], //(20)!
  "USE_HENCKY_STRAIN": false,  //(21)!
  "Tables": {} //(22)!
}
```

1. {{ ignore_undrained }}
2. {{ density_solid }}
3. {{ density_water }}
4. {{ porosity }}
5. {{ bulk_modulus_solid }}
6. {{ bulk_modulus_fluid }}
7. {{ permeability_xx }}
8. {{ permeability_yy }}
9. {{ permeability_xy }}
10. {{ permeability_change_inverse_factor }}
11. {{ dynamic_viscosity }}
12. {{ biot_coefficient }}
13. {{ retention_law }}
14. {{ saturated_saturation }}
15. {{ residual_saturation }}
16. {{ minimum_relative_permeability }}
17. Name of the UDSM (`.dll`) soil file. For various commonly used soil models see [Details](#umat-parameters-format)
18. Set to 1
19. Set `true` if the UDSM file is in Fortran
20. The umat parameters. For various commonly used soil models see [Details](#umat-parameters-format)
21. If `true`: use Hencky strain measure (natural/logarithmic strain). Should be used together with `move_mesh_flag` [solver setting block of the ProjectParameters.json](project_parameters.md#solver_settings-block-structure-format) and have the same value
22. Optional tables

### UMAT parameters format

Here are the input parameters described for some soil models that are commonly used within Deltares. See [Soil Models](../theory/soil_models.md) for more background about how to obtain and use them.

#### abc-Isotache natural strain: `UDSM.dll`

For abc-Isotache natural strain soil model, `UDSM.dll`, the following parameters are expected:

| Parameters | Description |
| --- | --- |
| `a` | modified natural swelling index |
| `b` | modified natural compression index |
| `c` | modified natural secondary compression constant |
| `t` | time = 1.0 |
| `OCR` | overconsolidation ratio |

#### Mohr-Coulomb model: `MohrCoulomb64.dll`

For Mohr-Coulomb model in `MohrCoulomb64.dll`, the following parameters are expected:

| Parameters | Description |
| --- | --- |
| `E` | Young's modulus (kN/m^2^) | 
| `Nu` | Poisson's ratio unloading/reloading | 
| `C` | cohesion (kN/m^2^) | 
| `Phi` | friction angle (°) | 
| `Psi` | dilation angle (°) |
| `Tens` | allowable tensile stress (kN/m^2^) |
| `Yield` | yield function index (1 for Mohr-Coulomb) | 
| `Nu_undr` | undrained Poisson's ratio |

#### Mohr-Coulomb model: `example64.dll`

For Mohr-Coulomb model in `example64.dll`, the following parameters are expected:

| Parameters | Description |
| --- | --- |
| `G` | shear modulus (kN/m^2^) | 
| `Nu` | Poisson's ratio unloading/reloading | 
| `C` | cohesion (kN/m^2^) | 
| `Phi` | friction angle (°) | 
| `Psi` | dilatancy angle (°) |
| `Tens` | allowable tensile stress (kN/m^2^) |
