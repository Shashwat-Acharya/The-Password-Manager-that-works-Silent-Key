# Contributing to Silent Key

Thank you for considering contributing to **Silent Key**! This guide will help you set up your environment, understand the tools used, and contribute effectively to the project.

---

## Libraries and Tools Used

This project leverages the following tools and libraries:

1. **PyQt6**: For building the GUI. Refer to the [PyQt6 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt6/).
2. **Pyenv**: For managing Python versions.  
   - [Pyenv for Windows](https://github.com/pyenv-win/pyenv-win)  
   - [Pyenv for Linux](https://github.com/pyenv/pyenv)  
3. **Poetry**: For dependency management.  
   - Install via `pip install poetry`. See the [Poetry Docs](https://python-poetry.org/docs/).
4. **MkDocs**: For project documentation. Learn more at [MkDocs](https://www.mkdocs.org/getting-started/).

---

## Getting Started

### 1. Fork and Clone the Repository
1. Fork the repository on GitHub.
2. Clone your fork:
   ```bash
   git clone https://github.com/your-username/silent-key.git
   cd silent-key
   ```

### 2. Create a Branch
Always create a new branch for your work:
```bash
git checkout -b feature/your-feature-name
```

### 3. Set Up the Development Environment
1. **Install Dependencies**:  
   Use Poetry to install the required dependencies:
   ```bash
   poetry install
   ```
2. **Create and Activate a Virtual Environment**:
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - Linux:
     ```bash
     source .venv/bin/activate
     ```

3. **PyQt6 on Windows**:  
   If you encounter installation issues, ensure you have the necessary C++ bindings:
   - Install [Visual Studio Community Edition](https://visualstudio.microsoft.com/visual-cpp-build-tools/).
   - Add the C/C++ plugin if using an existing Visual Studio installation.

---

## Contribution Guidelines

### What Can You Contribute?
- Bug fixes
- New features
- Documentation improvements
- Writing or updating tests
- Suggestions for new features via GitHub issues

### Pull Request Checklist
Before creating a pull request, ensure the following:
1. All tests pass locally.
2. Your code adheres to PEP8 style guidelines.
3. You’ve updated the documentation (if applicable).
4. Commit messages are clear and descriptive.
5. The `.venv/` directory is excluded from version control (add to `.gitignore`).

### Issue Reporting
To report a bug or request a feature:
1. Open an issue on the [GitHub Issues](https://github.com/Shashwat-Acharya/silent-key/issues) page.
2. Provide a clear description, including steps to reproduce the issue (if applicable).

---

## Testing

1. To run tests:
   ```bash
   pytest
   ```
2. If you’re adding a feature, ensure you include appropriate tests.

---

## Code Style

We follow **PEP8** standards for Python code. Use tools like `flake8` to check your code style:
```bash
pip install flake8
flake8 .
```

---

## Additional Notes

1. **Excluding Virtual Environments**:
   Ensure your virtual environment is excluded from version control. Add this line to `.gitignore`:
   ```plaintext
   .venv/
   ```

2. **Feature Suggestions**:
   We welcome suggestions for improving the project! Feel free to open an issue or submit a pull request.

---

By following these guidelines, you’ll help maintain the project’s quality and usability. Thank you for your contributions!
