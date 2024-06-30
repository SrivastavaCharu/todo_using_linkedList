import aws_cdk as cdk
from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3,
    aws_sns as sns,
)
from constructs import Construct


class TodoCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        s3.Bucket(
            self, "TaskBucket", versioned=True, removal_policy=cdk.RemovalPolicy.DESTROY
        )

        sns.Topic(self, "TaskTopic", display_name="My ToDo Task Topic")
