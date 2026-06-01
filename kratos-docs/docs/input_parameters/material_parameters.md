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
6. Name of the soil constitutive law. Type: string. Supported names include [`GeoLinearElasticPlaneStrain2DLaw`](#incremental-linear-elastic-law-for-plane-strain-models), [`GeoMohrCoulombWithTensionCutOff2D`](#mohr-coulomb-with-tension-cut-off-for-plane-strain-models) and [`SmallStrainUDSM2DPlaneStrainLaw`](#constitutive-law-smallstrainudsm2dplanestrainlaw)
7. Material properties relevant for the current constitutive law.

When a project needs various materials, multiple items can be added to the properties list, each having its own unique ID and possibly varying constitutive laws and/or material properties.

For geomechanical materials, the "Variables" section consists of three parts:

1. `GEO_DRAINAGE_TYPE`: {{ geo_drainage_type }} Details can be found [here](#drainage-types).
2. [General material properties of the soil](#general-material-properties-of-the-soil).
3. A description of the groundwater flow. This includes the [permeability](#permeability) and a [retention law](#retention-laws).


## Drainage types

At present, the GeoMechanicsApplication supports two drainage types:

1. **Fully coupled.** When this type is selected, the simulation will solve for the displacement field as well as the pore water pressure field in a coupled manner. In other words, the displacement field affects the pore water pressure field and vice versa.
2. **Keeping the pore water pressure field constant.** When this type is selected, the simulation will solve for the displacement  field only. The pore water pressure field is kept constant, i.e. the pore water pressure degrees of freedom remain unchanged. Only the effect of the pore water pressure field on the displacement field is taken into account for the coupling.


## General material properties of the soil

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


## Horizontal stress state initialization

For the initialization of an in-situ stress field, the $K_0$ procedure derives the horizontal effective stresses from a field of vertical effective stresses. To distinguish between the vertical and horizontal stress fields, we need to know the direction of gravity. Furthermore, we need additional input that details how the horizontal stress field is calculated from the vertical one. This can be specified in one of several ways:

- Direct input of $K_{0}^{\mathrm{nc}}$ as described [here](#direct-specification-of-k_0mathrmnc).
- Derivation of the $K_{0}$ value from the friction angle as described [here](#derivation-of-k_0mathrmnc-from-the-friction-angle).
- Direct specification of directional $K_{0}$ values as described [here](#direct-specification-of-directional-k_0-coefficients).


### Direct specification of $K_0^{\mathrm{nc}}$

```json
{
    "K0_MAIN_DIRECTION": 1, //(1)!
    "K0_NC": 0.62 //(2)!
}
```

1. {{ k0_main_direction }}
2. $K_{0}^{\mathrm{nc}}$: coefficient for normally consolidated soil. Type: float. Range: [0.0, ->.


### Derivation of $K_0^{\mathrm{nc}}$ from the friction angle

The $K_0^{\mathrm{nc}}$ can be derived from the friction angle as follows:

$$K_0^{nc} = 1.0 - \sin \phi$$

```json
{
    "K0_MAIN_DIRECTION": 1, //(1)!
    "GEO_FRICTION_ANGLE": 30.0 //(2)!
}
```

1. {{ k0_main_direction }}
2. {{ geo_friction_angle }}


### Direct specification of directional $K_0$ coefficients

```json
{
    "K0_MAIN_DIRECTION": 1, //(1)!
    "K0_VALUE_XX": 0.5, //(2)!
    "K0_VALUE_YY": 1.0, //(3)!
    "K0_VALUE_ZZ": 0.5 //(4)!
}
```

1. {{ k0_main_direction }}
2. {{ k0_value_xx }}
3. {{ k0_value_yy }}
4. {{ k0_value_zz }}


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

`GeoLinearElasticPlaneStrain2DLaw` is an incremental linear elastic constitutive law that is to be used by plane strain models only. It does not require any additional input compared to what was described at the top of this page.


## Mohr-Coulomb with tension cut-off for plane strain models

`GeoMohrCoulombWithTensionCutOff2D` is a Mohr-Coulomb plastic constitutive law that is to be used by plane strain models only. In addition to the input described at the top of this page, the following input is needed for the shear yield surface and tension cut-off.

```json
{
    "GEO_COHESION": 3.0e+03, //(1)!
    "GEO_FRICTION_ANGLE": 22.5, //(2)!
    "GEO_DILATANCY_ANGLE": 0.0, //(3)!
    "GEO_TENSILE_STRENGTH": 7.24263e+03 //(4)!
}
```

1. {{ geo_cohesion }}
2. {{ geo_friction_angle }}
3. {{ geo_dilatancy_angle }}
4. {{ geo_tensile_strength }}


## User-defined soil model (UDSM) for plane strain models

`SmallStrainUDSM2DPlaneStrainLaw` is a user-defined material model for plane strain models only. In addition to the input described at the top of this page, the following input is needed.

```json
{
  "UDSM_NAME": "UDSM.dll", //(1)!
  "UDSM_NUMBER": 1, //(2)!
  "IS_FORTRAN_UDSM": true, //(3)!
  "UMAT_PARAMETERS": [ ] //(4)!
  "USE_HENCKY_STRAIN": false  //(5)!
}
```

1. Path to the UDSM file (`.dll`). For various commonly used soil models see [Details](#umat-parameters-format). Type: string.
2. Material model ID in the UDSM. Type: integer.
3. Set to `true` if the UDSM file was written in FORTRAN. Type: boolean.
4. The UMAT parameters: an array of values. For various commonly used soil models see [Details](#umat-parameters-format)
5. If `true`, use Hencky strain measure (natural/logarithmic strain). Should be used together with `move_mesh_flag` [solver setting block of the ProjectParameters.json](project_parameters.md#solver_settings-block-structure-format) and have the same value. Type: boolean.


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
