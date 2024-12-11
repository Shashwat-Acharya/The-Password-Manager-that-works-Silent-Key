# Silent Key

## Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Development](#development)
  - [Virtual Environment](#virtual-environment)
  - [Dependency Management](#dependency-management)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## About the Project
"Silent Key" is a user-friendly and efficient tool designed to securely store, manage, and generate strong passwords. Built using modern Python tools and libraries, the project prioritizes ease of use, scalability, and security.

## Features
- Securely store and manage passwords.
- Generate strong, random passwords.
- User-friendly graphical interface built with PyQt6.
- Cross-platform compatibility (Windows/Linux).

## Installation

### Prerequisites
1. **Python (>= 3.8)**: Ensure Python is installed. Use [pyenv](https://github.com/pyenv/pyenv) for version management.
   - Windows users can use [pyenv-win](https://github.com/pyenv-win/pyenv-win).
2. **Dependency Manager**: This project uses Poetry for dependency management.
   - Install Poetry using:
     ```bash
     pip install poetry
     ```
3. **C++ Bindings (Windows Only)**: For PyQt6, install Visual Studio with C++ bindings.
   - [Download Visual Studio Community Edition](https://visualstudio.microsoft.com/visual-cpp-build-tools/).

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/Shashwat-Acharya/The-Password-Manager-that-works.git
   cd The-Password-Manager-that-works
   ```
2. Install dependencies:
   ```bash
   poetry install
   ```
3. Create a virtual environment (if not using Poetry's built-in virtualenv):
   ```bash
   python -m venv .venv
   ```
   Activate it:
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - Linux:
     ```bash
     source .venv/bin/activate
     ```
4. Run the application:
   ```bash
   python main.py
   ```

---

## Usage
- Launch the application.
- Create a master password to secure your vault.
- Add, delete, or update saved passwords.
- Use the built-in generator to create strong passwords.

---

## Development

### Virtual Environment
1. Ensure the virtual environment is excluded from version control by adding it to `.gitignore`:
   ```plaintext
   .venv/
   ```
2. Activate the virtual environment:
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - Linux:
     ```bash
     source .venv/bin/activate
     ```

### Dependency Management
- Use Poetry to add new dependencies:
  ```bash
  poetry add <package-name>
  ```
- Update the `pyproject.toml` file automatically by adding dependencies.

---

## Contributing
Contributions are welcome! Follow these steps to contribute:
1. Fork the repository.
2. Clone your forked repository:
   ```bash
   git clone https://github.com/your-username/The-Password-Manager-that-works.git
   ```
3. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
4. Commit your changes with a meaningful message:
   ```bash
   git commit -m "Add feature: feature-name"
   ```
5. Push your branch:
   ```bash
   git push origin feature-name
   ```
6. Create a pull request to the main repository.

For more detailed contribution guidelines, please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file.

---

## License
This project is licensed under the **GNU General Public License v3.0**. Additional terms include:
- Redistribution (modified or unmodified) requires explicit permission or a royalty payment of $10 per sale.
- The project name must remain unchanged.

For more details, see the [LICENSE](LICENSE) file.

---

## Acknowledgements
- [PyQt6 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt6/)
- [Pyenv](https://github.com/pyenv/pyenv)
- [Poetry](https://python-poetry.org/docs/)
- [MkDocs](https://www.mkdocs.org/)

---
Thank you for using **Silent Key**!
