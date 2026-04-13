# MaterialParameters.json file description

The material parameters json-file contains as description of the input of the Kratos simulation.

The strucal format of the ProjectParameter.json is described on the Kratos website:

```json
{
  "properties": [
    "properties_id": 0,
    "model_part_name": "PorousDomain.Soil-0",
    "Material": {
        "constitutive_law": {
          "name": "Constitutive_law_name"
        },
		"Variables": { }
  ]
}
```

  * **properties_id**: ID number assigned to your material.
  * **model_part_name**: Name of your material.
  * **Material**: The material description.
  * **name**: the name of soil constitutive law.
  * **Variables**: The material parameters. For material that are often used in geomechanical applications, the structural format described in more detail below.

## Structure format for LinearElasticPlaneStrainK02DLaw

For a *LinearElasticPlaneStrainK02DLaw* material the following properties should be defined:

* **IGNORE_UNDRAINED**: If "true": Keeps all the pressure field unchanged
* **YOUNG_MODULUS**: Young Modulus (kPa)
* **POISSON_RATIO**: Poisson Ratio
* **DENSITY_SOLID**: The density of soil (kg/m<sup>3</sup>) or (mg/m<sup>3</sup> \= g/cm(m<sup>3</sup>)) as non-porous material.
* **DENSITY_WATER**: The density of water, input: "1000" (kg/m<sup>3</sup>) or "1" (Mg/m<sup>3</sup> \= g/cm<sup>3</sup>)
* **POROSITY**: Porosity ratio
* **BULK_MODULUS_SOLID**: The measure of the decrease in solid volume with an increase in pressure (N/m<sup>2</sup>)
* **BULK_MODULUS_FLUID**: The measure of the decrease in fluid volume with an increase in pressure (N/m<sup>2</sup>), for water input: 2.2x10<sup>9</sup>
* **PERMEABILITY_XX**: Intrinsic permeability in the XX direction (m<sup>2</sup>)
* **PERMEABILITY_YY**: Intrinsic permeability in the YY direction (m<sup>2</sup>)
* **PERMEABILITY_XY**: Intrinsic permeability in the XY direction (m<sup>2</sup>)
* **PERMEABILITY_CHANGE_INVERSE_FACTOR* **: If > 0 the permeability will be updated depending on the volumetric strain.
* **DYNAMIC_VISCOSITY**: Dynamic Viscosity (kg/m.s)
* **THICKNESS**:
* **K0_MAIN_DIRECTION**: Input "0" for the X direction, "1" for the Y direction, and "2" for the Z direction
* **K0_VALUE_XX**: K0 value in the XX direction
* **K0_VALUE_YY**: K0 value in the YY direction
* **K0_VALUE_ZZ**": K0 value in the ZZ direction
* BIOT_COEFFICIENT**: Biot alpha coefficient
* **RETENTION_LAW**: Water retention law, "SaturatedLaw", "VanGenuchtenLaw" and "SaturatedBelowPheraticLevelLaw"
* **SATURATED_SATURATION**: Maximum pore fill by water, between 0 and 1, higher than RESIDUAL_SATURATION.
* **RESIDUAL_SATURATION**: The minimum pore fill trapped in the soil, between 0 and 1, lower than SATURATED_SATURATION.
* **VAN_GENUCHTEN_AIR_ENTRY_PRESSURE**: Coefficient for Van Genuchten curve
* **"VAN_GENUCHTEN_GN**: Coefficient for Van Genuchten curve
* **VAN_GENUCHTEN_GL**: Coefficient for Van Genuchten curve
* **MINIMUM_RELATIVE_PERMEABILITY**: Minimum relative permeability
