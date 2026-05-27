# MaterialParameters.json file description

The material parameters json-file contains as description of all the materials and there properties of the Kratos simulation. 
The user is responsible for giving all material parameters a consistent set of parameters.

By clicking on an annotation (1) the user is provided more detailed information about a property.
{ .annotate }

1. Here more information about an annotation can be found.

## MaterialParameters.json structure format
The strucal format of the MaterialParameters.json is as follows:

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
    },
}
```

1. Start of the properties list
2. Name of the material
3. ID number assigned to your material
4. Start of material description
5. Define soil constitutive law
6. The name of soil constitutive law e.g. [`GeoLinearElasticPlaneStrain2DLaw`](#constitutive-law-geolinearelasticplanestrain2dlaw) [`SmallStrainUDSM2DPlaneStrainLaw`](#constitutive-law-smallstrainudsm2dplanestrainlaw)
7. Begin of material variables

For multiple material in one project, multiple item can be added to the properties list, each having there own unique id and possibility varying constitutive laws or material properties.
For various constitutive laws, there properties (variable sections) are defined below.

## Constitutive law: GeoLinearElasticPlaneStrain2DLaw

When `GeoLinearElasticPlaneStrain2DLaw` is set as the name of the constitutive law, the strucal format `Variables`-block is as follows:

```json
{
  "IGNORE_UNDRAINED": false, //(1)!
  "YOUNG_MODULUS": 10000, //(2)!
  "POISSON_RATIO": 0.2, //(3)!
  "DENSITY_SOLID": 2650, //(4)!
  "DENSITY_WATER": 1000, //(5)!
  "POROSITY": 0.3, //(6)!
  "BULK_MODULUS_SOLID": 20000000000, //(7)!
  "BULK_MODULUS_FLUID": 2200000000, //(8)!
  "PERMEABILITY_XX": 6.901970778117567E-11, //(9)!
  "PERMEABILITY_YY": 6.901970778117567E-11, //(10)!
  "PERMEABILITY_XY": 0, //(11)!
  "PERMEABILITY_CHANGE_INVERSE_FACTOR": 0, //(12)!
  "DYNAMIC_VISCOSITY": 0.0013, //(13)!
  "THICKNESS": 1,
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

1. {{ ignore_undrained }}
2. Young Modulus (Pa)
3. Poisson Ratio
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

When `SmallStrainUDSM2DPlaneStrainLaw` is set as the name of the constitutive law, the strucal format `Variables`-block is as follows:

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
  "USE_HENCKY_STRAIN": false  //(21)!
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

Here are the input parameters described for some soil models that are commonly used within Deltares. See [Soil Models](../theory/soil_models.md) for more background about the soil models that how to use and obtain them.

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
| `Psi` | dilation angle (°) |
| `Tens` | allowable tensile stress (kN/m^2^) |
