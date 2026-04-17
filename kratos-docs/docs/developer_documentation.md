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
