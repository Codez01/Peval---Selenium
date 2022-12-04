
# ------------------------------- IMPORTS ---------------------------
from config import config
import boto3
# ------------------------------- IMPORTS ---------------------------


# ---------------------- Variables --------------------
snsArn = config["sns"]["topicArn"]

SUCCESS = int(config["global variables"]["SUCCESS"])
NOT_VISIBLE = int(config["global variables"]["NOT_VISIBLE"])
FAILURE = int(config["global variables"]["FAILURE"])

# ---------------------- Variables --------------------


def snsPublishMsg(subject, message):# a function for publishing a message to sns topic
    try:
        snsClient = boto3.client('sns')
        snsClient.publish(
            TopicArn=snsArn,
            Message=message,
            Subject=subject
        )

        return SUCCESS

    except:
        return FAILURE
