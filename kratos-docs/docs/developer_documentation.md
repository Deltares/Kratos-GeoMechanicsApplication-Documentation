# Developer Documentation

For contributors and internal developers. Build instructions, testing, contribution workflow, and maybe some notes on structure as well. Rather than repeating what’s documented in the Kratos repository, we may provide links to the relevant pages there. This page may serve as an entry point for the developer documentation that is maintained in the Kratos repository.


## Build Instructions

This section explains how to build the GeoMechanicsApplication (which is part of KRATOS Multiphysics) on your machine.  The shell commands presented in this documentation assume Window's Command Prompt.  When building on a different platform (e.g. Linux), please make sure to execute equivalent shell commands.


### Prerequisites

To build the GeoMechanicsApplication on your machine, the following packages need to be installed:

- [Git](https://git-scm.com/)
- [CMake](https://cmake.org/).  Please, download the latest **CMake 3** version, since Kratos does not support CMake version 4 yet.
- A C++ compiler.  For instance, on Windows [Microsoft Visual Studio](https://visualstudio.microsoft.com/) would be a natural choice.  On Linux systems, you may opt for [GCC](https://gcc.gnu.org/) or [Clang](https://clang.llvm.org/).
- A recent version of [Python 3](https://www.python.org/).
- A recent version of the [Boost library](https://www.boost.org/).  Since building the GeoMechanicsApplication requires the C++20 standard, we need at least version 1.75.

Optionally, you may want to use [Ninja](https://ninja-build.org/) as your build system.  On Windows, we have found that Ninja builds software significantly faster than MSBuild does, so you may want to give it a try.  Ninja is also available on Linux platforms.

Subsequently, you will need to clone the KRATOS repository to your machine.  First, change the current working directory to the location where you would like to have the KRATOS repository.  Let's say this location is stored in an environment variable named `KRATOS_REPO_PARENT_DIR`.

```sh
cd %KRATOS_REPO_PARENT_DIR%
git clone https://github.com/KratosMultiphysics/Kratos.git
```

You are advised to set up a dedicated Python `venv` for your KRATOS build:

```sh
cd Kratos
python -m venv .venv
.\.venv\Scripts\activate
```

Then update `pip` and install a few additional Python packages:

```sh
python -m pip install --upgrade pip
python -m pip install matplotlib
python -m pip install numpy
python -m pip install parameterized
python -m pip install pefile
python -m pip install platformdirs
```

When all of the above is in-place, we can actually start to build the application as explained in the next section.


### Building the GeoMechanicsApplication

The instructions given in this section assume a Windows platform with a Visual Studio Professional compiler.  First, you need to launch a Command Prompt, navigate to the `Tools` directory of the Visual Studio installation, and run the `VsDevCmd.bat` script:

```sh
.\VsDevCmd.bat -arch=amd64
```

The following table shows the absolute paths to the `Tools` directory for two recent versions of Visual Studio Professional.

| MS VS Version | Default MS VS tools directory |
|---------------|-------------------------------|
| Visual Studio 2022 | `C:\Program Files\Microsoft Visual Studio\2022\Professional\Common7\Tools` |
| Visual Studio 2026 | `C:\Program Files\Microsoft Visual Studio\18\Professional\Common7\Tools` |

Then we set the following two environment variables that define the compilers that we would like to use:

```sh
set CC=cl.exe
set CXX=cl.exe
```

Next, we need to set some more environment variables to make sure that CMake can be run successfully:

```sh
set BOOST_ROOT=C:\Users\Bob\boost_1_86_0
```

Here, `BOOST_ROOT` should be set to the top-level directory where you have extracted Boost to.  This directory contains amongst others the Boost license file, `INSTALL`, and `README.md`.

Once the Command Prompt has been properly set up, we can configure the build by executing the following command:

```sh
cmake ^
    -S <source_dir> ^
    -B <build_dir> ^
    -G Ninja ^
    -DCMAKE_BUILD_TYPE=Debug ^
    -DUSE_EIGEN_MKL=OFF ^
    -DKRATOS_GENERATE_PYTHON_STUBS=ON ^
    -DCMAKE_EXPORT_COMPILE_COMMANDS=ON ^
    -DKRATOS_SHARED_MEMORY_PARALLELIZATION=None ^
    -DCMAKE_UNITY_BUILD=OFF ^
    -DCMAKE_C_COMPILER=%CC% ^
    -DCMAKE_CXX_COMPILER=%CXX%
```


## External Developer Documentation

This section contains links to the relevant external developer documentation of the GeoMechanicsApplication.

### Custom Elements

[This document](https://github.com/KratosMultiphysics/Kratos/blob/master/applications/GeoMechanicsApplication/custom_elements/README.md) describes the specific finite element types that are available for geotechnical analysis.  Some of these elements use so-called ["contribution calculators"](https://github.com/KratosMultiphysics/Kratos/blob/master/applications/GeoMechanicsApplication/custom_elements/contribution_calculators/README.md), to control which contributions are taken into account when the left hand side (LHS) matrix and the right hand side (RHS) vector of the element are calculated.  Several of the geotechnical elements use the "Strategy" design pattern (also known as "Policy" design pattern) to gain control and configurability for the element functionality.  The available policies are described [here](https://github.com/KratosMultiphysics/Kratos/blob/master/applications/GeoMechanicsApplication/custom_elements/Policies.md).


### Custom Boundary Conditions

[This document](https://github.com/KratosMultiphysics/Kratos/blob/master/applications/GeoMechanicsApplication/custom_conditions/README.md) presents the various boundary condition types that are available for geotechnical analysis.


### Custom Geometries

[This document](https://github.com/KratosMultiphysics/Kratos/blob/master/applications/GeoMechanicsApplication/custom_geometries/README.md) presents the various U-Pw interface geometries that have been developed for geotechnical analysis.  These custom geometries are used by our geotechnical U-Pw interface element types.


### Custom Constitutive Laws

[This document](https://github.com/KratosMultiphysics/Kratos/blob/master/applications/GeoMechanicsApplication/custom_constitutive/README.md) presents the various constitutive laws that are available for geotechnical analysis.


### Custom Strategies

[This document](https://github.com/KratosMultiphysics/Kratos/blob/master/applications/GeoMechanicsApplication/custom_strategies/schemes/README.md) describes the time integration schemes as well as a load stepping scheme that are available for geotechnical analysis.  And [this document](https://github.com/KratosMultiphysics/Kratos/blob/master/applications/GeoMechanicsApplication/custom_strategies/strategies/README.md) presents a custom Newton-Raphson process for backward erosion piping.


### Custom Processes

[This document](https://github.com/KratosMultiphysics/Kratos/blob/master/applications/GeoMechanicsApplication/custom_processes/README.md) describes the various processes that can be used to control the geotechnical analysis.


### Test Documentation

Several geotechnical [tests](https://github.com/KratosMultiphysics/Kratos/blob/master/applications/GeoMechanicsApplication/tests/README.md) have been documented.  Those that have been documented, have a dedicated `README.md` file in the corresponding test directory.  Note that some tests can also produce plots depending on the shell environment in which they are run.
