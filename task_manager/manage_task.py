from .linked_list import LinkedList
from .aws_integration import AWSIntegration
import json

class TaskManager:
    def __init__(self, bucket_name, sns_topic_Arn):
        self.task_list = LinkedList()
        self.aws = AWSIntegration(bucket_name, sns_topic_Arn)

    def add_task(self, task):
        self.task_list.add_task(task)
        self.save_tasks()

    def view_task(self):
        return self.task_list.view_task()
    
    def complete_task(self, task):
        if self.task_list.complete_task(task):
            self.save_tasks()
            self.notify_complete(task)
            return True
        return False

    def save_tasks(self):
        tasks = self.view_task()
        tasks_json = json.dumps(tasks)
        self.aws.save_to_s3('tasks.json', tasks_json)

    def notify_complete(self, task):
        message = f'Task "{task}" has been completed'
        self.aws.send_sns_msg(message)