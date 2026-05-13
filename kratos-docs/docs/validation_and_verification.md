# Validation and Verification

Kratos GeoMechanics is validate through various unit tests, integration tests and acceptance tests.

Each of them have a certain purpose, which are explain below. These tests are run either on every change in Kratos GeoMechanics on nightly, depending on the calculation time. 

## Unit tests:
The purpose of unit testing is to verify that each unit of the software application works as intended and meets the design requirements. Unit testing typically involves writing test cases for each unit that exercise its functionality and validate its behavior in isolation from the rest of the application. A unit can be a single function, method, or class. The test cases are designed to cover a range of possible inputs and outputs and to expose any defects or errors in the unit’s implementation. Unit testing is usually automated, which allows for frequent and rapid testing during the development process. These tests are written by developers and individual tests should take milliseconds.

## Integration tests: 
The purpose of integration testing is to ensure that the various components of the application work together as intended and meet the design requirements. It also tests the interactions between different components or modules, which function correctly as a group and do not cause any unexpected behavior or errors. It also includes checking the results and the accuracy.

## System/Acceptance tests: 
System testing verifies the behavior and performance of the entire software system including all of its components and subsystems and also validates whether a software application meets the requirements and expectations of the stakeholders. The purpose of this testing is to ensure that the system meets the functional and non-functional requirements of the design and that the software application is ready for deployment and use in a production environment. It involves creating and executing test cases that validate the software system’s functionality, reliability, performance, usability, and compatibility with different environments.

Acceptance tests are physically the most realistic. These tests can be found on the [Kratos GeoMechanics website](https://github.com/KratosMultiphysics/Kratos/tree/master/applications/GeoMechanicsApplication/tests). Many of these test have human-readble documentation available about the goal of this test and can also be used for reference to set up your own simulation.