# Task Manager

This is a task management application using Linked List and AWS services(S3 and SNS).

## Features
- Add tasks
- View tasks
- Complete tasks
- Save tasks to AWS S3
- Notify task completion using AWS SNS

## Setup

1. Clone the repository
2. Set up a virtual environment
3. Install dependencies

```sh
git clone <repo-url>
cd task-manager
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py