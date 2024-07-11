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

3. Install the dependencies by:
```sh
pip install -r requirements.txt
```

4. Run the project using the following command:
```sh
python main.py
```

5. Run formatter:
```sh
black --check .
```

6. Run linter:
```sh
flake8 .
```

7. Run the following command to exit the virtual environment:
```sh
deactivate
```

## Running

You need to pass your ToDo tasks in [`main.py`] file, through `add_task()` function as shown below,
```sh
manager.add_task("YOUR TASK")
```

Once completed, you need to pass your completed tasks through this function,
```sh
manager.complete_task("Brush")
```