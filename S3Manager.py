from config import config
import boto3


BUCKETNAME = config["s3"]["bucketName"]
awsRegion = config["aws region"]["region1"]

SUCCESS = int(config["global variables"]["SUCCESS"])
NOT_VISIBLE = int(config["global variables"]["NOT_VISIBLE"])
FAILURE = int(config["global variables"]["FAILURE"])


def UploadFileToS3(FileNameWithPath, fileLocation, fileName):

    try:
        s3 = boto3.resource('s3')
        s3.meta.client.upload_file(fileLocation, BUCKETNAME, FileNameWithPath, ExtraArgs={
                                   'ACL': 'public-read', 'ContentType': "text/html"})
        print(FileNameWithPath)
        return SUCCESS

    except:
        return FAILURE


def pathToViewFile(FileNameWithPath):
    try:
        s3pathUrl = "https://"+BUCKETNAME+".s3." + \
            awsRegion+".amazonaws.com/"+FileNameWithPath
        return s3pathUrl
    except:
        return FAILURE
