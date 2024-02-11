# Project Setup and Development Guide

## Prerequisites

- Python 3.x installed
- Git (optional, recommended for cloning the project)

## Getting Started

1. **Clone the Project** (if using Git):

    ```bash
    git clone https://yourprojecturl.git
    cd A01110946_A6.2
    ```

2. **Set Up a Virtual Environment**:

    For Windows:

    ```bash
    python -m venv venv
    .\\venv\\Scripts\\activate
    ```

    For Unix/MacOS:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Configuring Project Setup and Build System**:

    To ensure the project can be installed in editable mode and is recognized by tools like `pip` and `pylint`, make sure to include a `pyproject.toml` and a `setup.py` file in the root directory with the following minimal configurations:

    `pyproject.toml`

     ```toml
     [build-system]
     requires = ["setuptools>=40.6.0", "wheel"]
     build-backend = "setuptools.build_meta"
     ```

     `setup.py`

     ```python
     from setuptools import setup, find_packages

     setup(
         name="A01110946_A6.2",
         version="0.1.0",
         packages=find_packages(),
     )
     ```

    These files are crucial for installing the project in an editable state (`pip install -e .`) and ensuring that the project structure is properly recognized by Python tools.

4. **Install the Project in Editable Mode**:

    Ensure you're in the project root directory (`A01110946_A6.2`) and run:

   ```bash
   pip install -e .
   ```

    This command installs your project's package (`bookinn`) in editable mode, allowing for live changes without reinstallation.

## Running the Application

- To run your application, ensure your virtual environment is activated and use the appropriate command for your application's entry point. For example:

   ```bash
   python -m bookinn
   ```

## Running Tests

- To run tests, you can use:

   ```bash
   pytest tests/
   ```

   or, if you're using `unittest`:

   ```bash
   python -m unittest discover -s tests
   ```

## Deactivating the Virtual Environment

- When you're done, you can deactivate the virtual environment to return to your global Python environment:

   ```bash
   deactivate
   ```

## Notes

- This project is configured to prioritize package configurations defined in `pyproject.toml`. The `setup.py` file is maintained for backward compatibility.
- Always activate your project's virtual environment before developing or running the project to ensure dependencies are correctly isolated.
- Make sure to replace the content of `setup.py` and `pyproject.toml` as necessary to match your project's specific details, such as name and dependencies. This guide will help users set up the project environment correctly and ensure compatibility with development and packaging tools.
