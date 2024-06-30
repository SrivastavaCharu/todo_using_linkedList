from task_manager.manage_task import TaskManager


def main():
    print("Entered main")
    try:
        bucket_name = "todocdkstack-taskbucketfec5f2d0-sfypu5ca2fq2"
        sns_topic_arn = (
            "arn:aws:sns:ap-northeast-1:392575048301:TodoCdkStack-"
            "TaskTopic85B90E1D-qNJKMFMVS4P0"
        )
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
