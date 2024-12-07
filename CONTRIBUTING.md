# Contributing to The Password Manager that works

Thank you for considering contributing to this project! This document will guide you through setting up your environment, understanding the tools being used, and contributing to the project. The goal is to ensure that you have a smooth development experience and can contribute easily.

---

## Libraries and Tools Used

This project uses several tools and libraries that make development easier and more organized. Below are the key ones:

### 1. **PyQt6**  
   - **Purpose**: We use **PyQt6** for building the graphical user interface (GUI) of the password manager.
   - **Why**: It is a set of Python bindings for Qt 6, a popular C++ framework for creating desktop applications.
   - **Documentation**: You can refer to the [PyQt6 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt6/) for more details on how to work with PyQt6.

### 2. **Pyenv**  
   - **Purpose**: **Pyenv** is used to manage multiple Python versions on your system. This ensures that everyone working on the project uses the same Python version.
   - **Windows Installation**:  
     If you are on Windows, you can install **pyenv-win** by running the following command in a **PowerShell** terminal:  
     ```powershell
     Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
     ```
     - **Tip**: If you encounter an `UnauthorizedAccess` error, try running PowerShell as **Administrator** and run this command:  
       ```powershell
       Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
       ```  
     - After that, you can rerun the installation command.
  
   - **Linux Installation**:  
     On Linux, install **pyenv** by running:  
     ```bash
     curl https://pyenv.run | bash
     ```

### 3. **Poetry**  
   - **Purpose**: We use **Poetry** to manage project dependencies. It simplifies dependency management and ensures that the project has the necessary libraries installed in a consistent manner.
   - **How to Install**:  
     Run the following command to install **Poetry**:  
     ```bash
     pip install poetry
     ```  
   - **Documentation**: For more details on Poetry, refer to the [Poetry Documentation](https://python-poetry.org/docs/).

### 4. **MkDocs**  
   - **Purpose**: **MkDocs** is used to create the documentation for this project. It allows us to easily maintain and generate a static site for documentation.
   - **Why**: It’s simple to set up and use, and allows for clean and easy-to-read documentation.

---

## Setting Up the Project

### 1. **Install Dependencies**  
   - This project uses **Poetry** to manage dependencies. You can install all the necessary dependencies for the project by running the following command:  
     ```bash
     poetry install
     ```
   - This will install everything needed to run the project on your machine.

### 2. **Create and Activate a Virtual Environment**  
   - Since we’re not including the virtual environment in the repository, you’ll need to create one yourself.  
   - You can use either **Poetry** or **Pyenv** for creating and managing your virtual environment. Here are the steps for using **Poetry** to create a virtual environment:
   
     - **Create a virtual environment**:  
       Run this command to create a new virtual environment:  
       ```bash
       poetry env use python
       ```

     - **Activate the virtual environment**:
       - **Windows**:  
         Navigate to the **Scripts** folder inside your `.venv` or `venv` folder and activate the environment with:  
         ```bash
         .\.venv\Scripts\activate
         ```

       - **Linux**:  
         Run this command to activate the environment:  
         ```bash
         source .venv/bin/activate
         ```

     - **Deactivating the environment**:  
       To deactivate the virtual environment, simply run:  
       ```bash
       deactivate
       ```

### 3. **Important for Windows Users**  
   - **PyQt6 Issues on Windows**:  
     If you're facing issues installing **PyQt6**, it’s most likely because you don’t have the necessary C/C++ bindings installed.  
     - You can resolve this by installing **Visual Studio Community Edition**:  
       [Download link](https://c2rsetup.officeapps.live.com/c2r/downloadVS.aspx?sku=community&channel=Release&version=VS2022&source=VSLandingPage&cid=2030:61e628e234c84c83ace9ca51a1d21f3f)
     - Once installed, ensure you add the C/C++ bindings. If you already have Visual Studio, just make sure the C/C++ plugin is installed.

---

## Workflow for Contributing

Here’s a step-by-step guide to help you contribute to the project effectively:

### 1. **Fork the Repository**  
   - Click on the **Fork** button at the top right of this repository page to create your own copy.

### 2. **Create a Branch**  
   - Always create a new branch for each feature or bug fix you want to work on.  
   For example, to create a new branch for a feature, run:  
   ```bash
   git checkout -b feature/your-feature-name
   ```

### 3. Make Your Changes

After making your changes, test your code locally to make sure everything is working as expected.

### 4. Commit Your Changes

Once you're happy with your changes, commit them to your branch with a meaningful commit message:

```bash
git commit -m "Added feature XYZ"
```


### 5. Push Your Changes

Once you're satisfied with your changes, push your branch to your forked repository using the following command:

```bash
git push origin feature/your-feature-name
```

### 6. Create a Pull Request 
After pushing your changes, go to the Pull Requests tab on GitHub and open a new pull request (PR) to merge your changes into the main repository.
Make sure to provide a detailed description of your changes in the PR.

## Important Notes
### 1. Excluding Virtual Environments from Git

  To ensure that your virtual environment is not included in the repository, add it to the .gitignore file.
  Add the following line to .gitignore:
   ``` bash
   venv/
   ```

## 3. Testing

  If you add new features, please write tests for them. You can use pytest or any other testing framework you prefer.

## 4. Feature Suggestions and Improvements

  Feel free to suggest new features or improvements! Open an issue or submit a pull request.
