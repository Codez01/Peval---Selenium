# ------------------------------- IMPORTS ---------------------------
from config import config
import sys
import boto3

# ------------ Local imports ---------------
import threadsManager as threadsManager
import seleniumConfig as seleniumConfig
import reportSerializer as reportSerializer
import pageChecker as pagechecker
import S3Manager as S3Manager
import snsManager as snsManager


# ---------------------- Variables --------------------

# is the program running in Lambda?
isInLambda = config["global variables"]["isInLambda"]
jsonFileLocation = config["jsonReportFile"]["location"]

SUCCESS = int(config["global variables"]["SUCCESS"])
NOT_VISIBLE = int(config["global variables"]["NOT_VISIBLE"])
FAILURE = int(config["global variables"]["FAILURE"])


# ------------------------- GENERAL FUNCTIONS  ----------------------

# function for retrieving the website's url from lambda's function
def getWebsiteURLFromLambda(event):
    try:
        return event["queryStringParameters"]["website"] if event['queryStringParameters']['website'] != None else FAILURE

    except:
        return FAILURE


# ****************************** MAIN ***********************************
def main():  # main function

    try:

        # intialize a browser driver with options
        browserDriver = seleniumConfig.SeleniumInit(isInLambda=isInLambda)

        urls = pagechecker.pageRoutesFinder(
            browserDriver=browserDriver,
            url=config['Example-Websites']["website1"])

        for urlKey in urls:
            threadsManager.threadHandler(
                url=urlKey, function=pagechecker.pagePerformanceChecker, arg1=urlKey)

        threadsManager.waitForThreadsToFinish()  # wait for threads to finish

        reportSerializer.writeToReportFile(pyReport=reportSerializer.GetPythonReport(
        ), jsonFileLocation=jsonFileLocation)  # prepare the report by writing data to JSON file
        browserDriver.quit()  # quite the driver --> EXIT
        sys.exit(1)

    except Exception as e:
        print(e)
        print("Unexpected error")
        browserDriver.quit()  # quite the driver --> EXIT
        sys.exit(1)

    # *************************END END END  MAIN ****************************


def lambda_handler(event, context):

    try:
        websiteURL = getWebsiteURLFromLambda(event)
        FileNameWithPath = "SitesReport/"+str(websiteURL).strip().replace(
            "/", "-")+"/report_" + reportSerializer.currDateAndTime().replace("/", "-")+".txt"

        # intialize a browser driver with options
        browserDriver = seleniumConfig.SeleniumInit(isInLambda)
    except Exception as e:
        print("Failed to create a browser Driver, ", e)
        response = {
            "statusCode": 412,
            "body": "Selenium Failed To Run.."}
        return response

    try:

        urls = pagechecker.pageRoutesFinder(
            browserDriver=browserDriver,
            url=websiteURL)

        for urlKey in urls:
            threadsManager.threadHandler(
                url=urlKey, function=pagechecker.pagePerformanceChecker, arg1=urlKey)

        threadsManager.waitForThreadsToFinish()  # wait for threads to finish

        reportSerializingStatus = reportSerializer.writeToReportFile(
            jsonFileLocation=jsonFileLocation, pyReport=reportSerializer.GetPythonReport())  # prepare the report by writing data to JSON file

        fileUploadStatus = S3Manager.UploadFileToS3(FileNameWithPath=FileNameWithPath, fileLocation=jsonFileLocation,
                                                    fileName="report_" + reportSerializer.currDateAndTime().replace("/", "-")+".txt")

        s3FileViewPath = S3Manager.pathToViewFile(
            FileNameWithPath=FileNameWithPath)

        print(s3FileViewPath)

        if fileUploadStatus == SUCCESS and reportSerializingStatus == SUCCESS:
            snsNotificationStatus = snsManager.snsPublishMsg(subject='Peval - Peroformance Evaluation Report Status',
                                                             message="Report Generated Successfully, View it here: https://peval-website.s3.amazonaws.com/html/report.html?file="+s3FileViewPath)

            if snsNotificationStatus == SUCCESS:
                response = {
                    "statusCode": 200,
                    "body": "Report Generated Successfully, View it here: https://peval-website.s3.amazonaws.com/html/report.html?file="+s3FileViewPath}

        else:
            response = {
                "statusCode": 412,
                "body": "Selenium operations were not fully completed"
            }

        browserDriver.quit()  # quite the driver --> EXIT
        return response

    except Exception as e:
        print(e)
        print("Unexpected error")
        browserDriver.quit()  # quite the driver --> EXIT
        response = {
            "statusCode": 412,
            "body": "Selenium Failed To Run.."}

        return response


if isInLambda == "false":
    main()  # run the main function if the program is not running in lambda
