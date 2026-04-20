# MaterialParameters.json file description

**Note: The user is responsible for giving all material parameters a consistent set of parameters.**

## Constitutive law: LinearElasticPlaneStrainK02DLaw

| Parameters | Description |
| --- | --- |
| `{ "properties": [{` | Start of the properties list |
| `"model_part_name":` | Name of your material |
| `"properties_id":` | ID number assigned to your material |
| `"Material": {` | Start of material description |
| `"constitutive_law": {` | Define soil constitutive law |
| `"name":` | Name of soil constitutive law |
| `"Variables": {` | Begin of material variables |
| `"IGNORE_UNDRAINED":` | If `true`: keeps all the pressure field unchanged |
| `"YOUNG_MODULUS":` | Young Modulus (kPa) |
| `"POISSON_RATIO":` | Poisson Ratio |
| `"DENSITY_SOLID":` | The density of soil (kg/m<sup>3</sup>) or (Mg/m<sup>3</sup> = g/cm<sup>3</sup>) as non-porous material |
| `"DENSITY_WATER":` | The density of water, input: `1000` (kg/m<sup>3</sup>) or `1` (Mg/m<sup>3</sup> = g/cm<sup>3</sup>) |
| `"POROSITY":` | Porosity ratio |
| `"BULK_MODULUS_SOLID":` | The measure of the decrease in solid volume with an increase in pressure (N/m<sup>2</sup>) |
| `"BULK_MODULUS_FLUID":` | The measure of the decrease in fluid volume with an increase in pressure (N/m<sup>2</sup>), for water input: 2.2x10<sup>9</sup> |
| `"PERMEABILITY_XX":` | Intrinsic permeability in the XX direction (m<sup>2</sup>) |
| `"PERMEABILITY_YY":` | Intrinsic permeability in the YY direction (m<sup>2</sup>) |
| `"PERMEABILITY_XY":` | Intrinsic permeability in the XY direction (m<sup>2</sup>) |
| `"PERMEABILITY_CHANGE_INVERSE_FACTOR":` | If > 0 the permeability will be updated depending on the volumetric strain |
| `"DYNAMIC_VISCOSITY":` | Dynamic viscosity (kg/m.s) |
| `"THICKNESS":` | Not specified in source document |
| `"K0_MAIN_DIRECTION":` | Input `0` for X, `1` for Y, and `2` for Z direction |
| `"K0_VALUE_XX":` | K0 value in the XX direction |
| `"K0_VALUE_YY":` | K0 value in the YY direction |
| `"K0_VALUE_ZZ":` | K0 value in the ZZ direction |
| `"BIOT_COEFFICIENT":` | Biot alpha coefficient |
| `"RETENTION_LAW":` | Water retention law: `SaturatedLaw`, `VanGenuchtenLaw`, `SaturatedBelowPheraticLevelLaw` |
| `"SATURATED_SATURATION":` | Maximum pore fill by water (0 to 1), higher than `RESIDUAL_SATURATION` |
| `"RESIDUAL_SATURATION":` | Minimum pore fill trapped in the soil (0 to 1), lower than `SATURATED_SATURATION` |
| `"VAN_GENUCHTEN_AIR_ENTRY_PRESSURE":` | Coefficient for Van Genuchten curve |
| `"VAN_GENUCHTEN_GN":` | Coefficient for Van Genuchten curve |
| `"VAN_GENUCHTEN_GL":` | Coefficient for Van Genuchten curve |
| `"MINIMUM_RELATIVE_PERMEABILITY":` | Minimum relative permeability |
| `"Tables": {}` | Optional tables |

## Constitutive law: GeoLinearElasticPlaneStrain2DLaw

### Parameters for elasticity and weight

| Parameters | Description |
| --- | --- |
| `"YOUNG_MODULUS":` | Young Modulus (kPa) or (MPa) |
| `"POISSON_RATIO":` | Poisson Ratio |
| `"DENSITY_SOLID":` | The density of soil (kg/m<sup>3</sup>) or (Mg/m<sup>3</sup> = g/cm<sup>3</sup>) as non-porous material |
| `"DENSITY_WATER":` | The density of water, input: `1000` (kg/m<sup>3</sup>) or `1` (Mg/m<sup>3</sup> = g/cm<sup>3</sup>) |
| `"POROSITY":` | Porosity ratio |

### Parameters for K0 procedure

| Parameters | Description |
| --- | --- |
| `"K0_MAIN_DIRECTION":` | Input `0` for X, `1` for Y, and `2` for Z direction. Direction (v) from which stress in perpendicular directions (h) is derived: `sigma_hh = K0 * sigma_vv` |

#### 3 alternatives for the input of the K0 value

See: https://publicwiki.deltares.nl/x/joSHDw

| Parameters | Description |
| --- | --- |
| `"K0_NC":` | K0 value for normal consolidation |
| `"INDEX_OF_UMAT_PHI_PARAMETER":` | The index of phi in the UMAT parameters |
| `"K0_VALUE_XX":` | K0 value in XX direction |
| `"K0_VALUE_YY":` | K0 value in YY direction |
| `"K0_VALUE_ZZ":` | K0 value in ZZ direction |
| `"OCR": >= 1` (optional) | Over consolidation ratio |
| `"POISSON_UNLOADING_RELOADING": (-1 to 0.5)` (optional) | Poisson's ratio under unloading and reloading |

### Parameters for water flow

| Parameters | Description |
| --- | --- |
| `"PERMEABILITY_XX":` | Intrinsic permeability in the XX direction (m<sup>2</sup>) |
| `"PERMEABILITY_YY":` | Intrinsic permeability in the YY direction (m<sup>2</sup>) |
| `"PERMEABILITY_XY":` | Intrinsic permeability in the XY direction (m<sup>2</sup>) |
| `"DYNAMIC_VISCOSITY":` | Dynamic viscosity (kg/m.s) or (kPa.s) |
| `"RETENTION_LAW":` | Water retention law: `SaturatedLaw`, `VanGenuchtenLaw`, `SaturatedBelowPheraticLevelLaw` |
| `"SATURATED_SATURATION":` | Maximum pore fill by water (0 to 1), higher than `RESIDUAL_SATURATION` |
| `"RESIDUAL_SATURATION":` | Minimum pore fill trapped in the soil (0 to 1), lower than `SATURATED_SATURATION` |
| `"VAN_GENUCHTEN_AIR_ENTRY_PRESSURE":` | Coefficient for Van Genuchten curve |
| `"VAN_GENUCHTEN_GN":` | Coefficient for Van Genuchten curve |
| `"VAN_GENUCHTEN_GL":` | Coefficient for Van Genuchten curve |
| `"MINIMUM_RELATIVE_PERMEABILITY":` | Minimum relative permeability |

### Parameters for soil-water interaction

| Parameters | Description |
| --- | --- |
| `"IGNORE_UNDRAINED":` | If `true`: keeps all the pressure field unchanged |
| `"BULK_MODULUS_SOLID":` | The measure of the decrease in solid volume with an increase in pressure (N/m<sup>2</sup>) |
| `"BULK_MODULUS_FLUID":` | The measure of the decrease in fluid volume with an increase in pressure (N/m<sup>2</sup>), for water input: 2.2x10<sup>9</sup> |
| `"BIOT_COEFFICIENT":` | Biot alpha coefficient |
| `"PERMEABILITY_CHANGE_INVERSE_FACTOR":` | If > 0 the permeability will be updated depending on the volumetric strain |
| `"THICKNESS":` | Not specified in source document |

## Constitutive law: SmallStrainUDSM2DPlaneStrainLaw

| Parameters | Description |
| --- | --- |
| `"UDSM_NAME":` | Name of the UDSM (`.dll`) soil file |
| `"UDSM_NUMBER":` | Set to `1` |
| `"IS_FORTRAN_UDSM":` | Set `true` if the UDSM file is in Fortran |
| `"UMAT_PARAMETERS"` (for abc-Isotache natural strains) | `a`: modified natural swelling index; `b`: modified natural compression index; `c`: modified natural secondary compression constant; `t`: time = 1.0; `OCR`: overconsolidation ratio |
| `"UMAT_PARAMETERS"` (for Mohr-Coulomb model in `MohrCoulomb64.dll`) | `1: E` Young's modulus (kN/m<sup>2</sup>), `2: Nu` Poisson's ratio unloading/reloading, `3: C` cohesion (kN/m<sup>2</sup>), `4: Phi` friction angle (degrees), `5: Psi` dilation angle (degrees), `6: Tens` allowable tensile stress (kN/m<sup>2</sup>), `7: Yield` yield function index (1 for Mohr-Coulomb), `8: Nu_undr` undrained Poisson's ratio |
| `"UMAT_PARAMETERS"` (for Mohr-Coulomb model in `example64.dll`) | `1: G` shear modulus (kN/m<sup>2</sup>), `2: Nu` Poisson's ratio unloading/reloading, `3: C` cohesion (kN/m<sup>2</sup>), `4: Phi` friction angle (degrees), `5: Psi` dilation angle (degrees), `6: Tens` allowable tensile stress (kN/m<sup>2</sup>) |
| `"USE_HENCKY_STRAIN":` | If `true`: use Hencky strain measure (natural/logarithmic strain). Should be used together with `move_mesh_flag` in ProjectParameters.json and have the same value |
