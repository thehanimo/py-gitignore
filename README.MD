# Python Template  Repository

This is a template repository for Python projects that provides a starting point for designing and developing Python applications. It includes a basic project structure, configuration for continuous integration, static analysis, code formatting, and more. You can use this template as a foundation for your Python projects.

## Features

- **Programming Language**: Python
- **Runtime environment**: Python v3.11.x
- **Testing Framework**: unittest
- **Continuous Integration**: GitHub Actions
- **Static Analysis**: Flake8
- **Code Formatting**: Black
- **Package Manager**: pip
- **License**: MIT License

## Getting Started

To use this template for your Python project, follow these steps:

1. **Fork this repository**: Click the "Fork" button at the top right of this page to create a copy of this template repository in your GitHub account.

2. **Clone your fork**: Use `git clone` to clone the repository to your local machine:

   ```sh
   git clone https://github.com/kimonk0299/python-template.git
   ```


3. **Set up virtual environment**: 
   ```sh
   python -m venv .venv
   source .venv/bin/activate
   ```


4. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```


5. **Add your files to `src/` and unit tests to `tests/`**

6. **Format code**:
   ```sh
   black .
   ```


7. **Run static analysis**:
   ```sh
   flake8
   ```


8. **Run tests**:
   ```sh
   python -m unittest discover -s tests
   ```


9. **Push code on GitHub to run CI tests on GitHub Actions**


