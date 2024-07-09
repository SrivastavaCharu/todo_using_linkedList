# Task Manager

This is a task management application using Linked List and AWS services(S3 and SNS).
This application performs the following features. There is no GUI for this app as of now. 

## Features
- Add tasks
- View tasks
- Complete tasks
- Save tasks to AWS S3
- Notify task completion using AWS SNS

## Prerequisites
1. [Install Python](https://www.python.org/downloads/)
2. [Install pip](https://pip.pypa.io/en/stable/installation/)
3. [Install cdk](https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-python.html)

## Setup

1. Clone the repository
```sh
git clone <repo-url>
```

2. Move to the root directory and set up a virtual environment
```sh
python -m venv .venv
source .venv/bin/activate
```
This creates a virtual environment for project dependencies. A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated Python virtual environments for them. Before you can start installing or using packages in your virtual environment you'll need to activate it.

3. Install dependencies
```sh
pip install -r requirements.txt
```
This installs the necessary Python packages defined in [`requirements.txt`]

4. Run the project
```sh
python main.py
```
This starts the application.

5. Run formatter
```sh
black --check .
```
This checks the code format using `black`, ensuring consistency.

6. Run linter
```sh
flake8 .
```
Runs `flake8` to identify any stylistic or logical errors in the code.

7. To get out of the virtual environment
```sh
deactivate
```
This command deactivates the virtual environment. 