# Developer documentation

This section is intended for contributors and internal developers.

If you want to build Kratos from scratch, please follow the instructions on the [Kratos website](https://kratosmultiphysics.github.io/Kratos/pages/Kratos/For_Users/How_To_Get_Kratos/Binaries.html).


## External developer documentation

This section contains links to the relevant external developer documentation of the GeoMechanicsApplication.

### Custom elements

[This document](https://github.com/KratosMultiphysics/Kratos/blob/master/applications/GeoMechanicsApplication/custom_elements/README.md) describes the specific finite element types that are available for geotechnical analysis. Some of these elements use so-called ["contribution calculators"](https://github.com/KratosMultiphysics/Kratos/blob/master/applications/GeoMechanicsApplication/custom_elements/contribution_calculators/README.md), to control which contributions are taken into account when the left hand side (LHS) matrix and the right hand side (RHS) vector of the element are calculated. Several of the geotechnical elements use the "Strategy" design pattern (also known as "Policy" design pattern) to gain control and configurability for the element functionality. The available policies are described [here](https://github.com/KratosMultiphysics/Kratos/blob/master/applications/GeoMechanicsApplication/custom_elements/Policies.md).


### Custom boundary conditions

[This document](https://github.com/KratosMultiphysics/Kratos/blob/master/applications/GeoMechanicsApplication/custom_conditions/README.md) presents the various boundary condition types that are available for geotechnical analysis.


### Custom geometries

[This document](https://github.com/KratosMultiphysics/Kratos/blob/master/applications/GeoMechanicsApplication/custom_geometries/README.md) presents the various U-Pw interface geometries that have been developed for geotechnical analysis. These custom geometries are used by our geotechnical U-Pw interface element types.


### Custom constitutive laws

[This document](https://github.com/KratosMultiphysics/Kratos/blob/master/applications/GeoMechanicsApplication/custom_constitutive/README.md) presents the various constitutive laws that are available for geotechnical analysis.


### Custom Strategies

[This document](https://github.com/KratosMultiphysics/Kratos/blob/master/applications/GeoMechanicsApplication/custom_strategies/schemes/README.md) describes the time integration schemes as well as a load stepping scheme that are available for geotechnical analysis. And [this document](https://github.com/KratosMultiphysics/Kratos/blob/master/applications/GeoMechanicsApplication/custom_strategies/strategies/README.md) presents a custom Newton-Raphson process for backward erosion piping.


### Custom processes

[This document](https://github.com/KratosMultiphysics/Kratos/blob/master/applications/GeoMechanicsApplication/custom_processes/README.md) describes the various processes that can be used to control the geotechnical analysis.


### Test documentation

Several geotechnical [tests](https://github.com/KratosMultiphysics/Kratos/blob/master/applications/GeoMechanicsApplication/tests/README.md) have been documented. Those that have been documented, have a dedicated `README.md` file in the corresponding test directory. Note that some tests can also produce plots depending on the shell environment in which they are run.
