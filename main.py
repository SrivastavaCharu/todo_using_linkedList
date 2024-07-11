import os
from task_manager.manage_task import TaskManager
from dotenv import load_dotenv

load_dotenv()


def main():
    try:
        bucket_name = os.getenv("BUCKET_NAME")
        sns_topic_arn = os.getenv("SNS_TOPIC_ARN")
        print(sns_topic_arn, bucket_name)
        manager = TaskManager(bucket_name, sns_topic_arn)
        manager.add_task("Brush")
        manager.add_task("Bath")
        print(manager.view_tasks())
        manager.complete_task("Brush")
        print(manager.view_tasks())
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
