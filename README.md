# Phase-3-uld-db-project
# Your CLI Application Name

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-v1.0.0-green.svg)](https://semver.org/)

Brief description of your CLI application. Explain what it does, its main features, and its intended use case.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Options](#options)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Installation
Requires Python: 3.8

-Project Repository: 
    -https://github.com/Justin3459/Phase-3-uld-db-project.git
-Dependencies:
    -sqlalchemy = "==1.4.41"
    -alembic = "*"
    -prettycli = "*"
    -simple-term-menu = "*"


Provide instructions on how to install your CLI application. Include any prerequisites or dependencies that need to be installed before using your CLI. If your application is available on package managers like npm, pip, or brew, mention it here.

## Introduction
This CLI application is used to track Unit Load Devices(ULD) once they are on a caster deck. All ULDs are marked as incomplete and once completed the user is able to change the status of the ULD. The features in this application are: List ULD, Update Status, Add ULD, and Delete ULD. This application allows the user to keep track of the status and modify ULD information.

## Features

- List ULD: Allows user to display ULDs that are currently in the database
- Add ULD: Allows user to add new ULDs to the database in the format amz(4 digit number)(ULD type)
- Delete ULD: Allows user to delete Ulds in the database
- Update ULD: Allows user to change the name, caster deck or status of a particular ULD

If a ULD is not in the current database the user will be prompted to enter a valid ULD

## Installation

1. it clone repository in the terminal
2. cd into repository
3. type pipenv install and shell in the terminal
4. run python3 cli.py to start application. If you get a ModuleNotFoundError you can run pip3 install {module name}

## Usage

Explain how to use your application. Provide examples and command-line usage if applicable. Screenshots or GIFs can be helpful here.

## Configuration

If your application requires configuration, API keys, or settings, explain how users can configure it. Provide guidance on modifying configuration files or environment variables.

## Contributing

Encourage others to contribute to your project. Outline guidelines for how they can submit bug reports, feature requests, or pull requests. Include information about coding standards, testing, and how to set up a development environment.

## License

Specify the license under which your application is distributed. For example:

This project is licensed under the [MIT License](LICENSE).