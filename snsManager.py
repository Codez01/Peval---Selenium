
# ------------------------------- IMPORTS ---------------------------
from config import config
import boto3
# ------------------------------- IMPORTS ---------------------------


# ---------------------- Variables --------------------
snsTopicName = config["sns"]["topicName"]

SUCCESS = int(config["global variables"]["SUCCESS"])
NOT_VISIBLE = int(config["global variables"]["NOT_VISIBLE"])
FAILURE = int(config["global variables"]["FAILURE"])

# ---------------------- Variables --------------------


def snsPublishMsg(subject, message):# a function for publishing a message to sns topic
    try:
        snsClient = boto3.client('sns')
        snsTopicArn = snsClient.create_topic(Name=snsTopicName)
        snsClient.publish(
            TopicArn=snsTopicArn,
            Message=message,
            Subject=subject
        )

        return SUCCESS

    except:
        return FAILURE
