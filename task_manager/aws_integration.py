import boto3
import json


class AWSIntegration:
    def __init__(self, bucket_name, sns_topic_arn):
        self.s3 = boto3.client("s3")
        self.sns = boto3.client("sns")
        self.bucket_name = bucket_name
        self.sns_topic_arn = sns_topic_arn

    def save_to_s3(self, key, data):
        self.s3.put_object(Bucket=self.bucket_name, Key=key, Body=data)

    def send_sns_msg(self, message):
        self.sns.publish(TopicArn=self.sns_topic_arn, Message=message)
