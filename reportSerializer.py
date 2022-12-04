# ------------------------------- IMPORTS ---------------------------
import json
from config import config
from datetime import datetime
import pageChecker as pageChecker

# ------------------------------- IMPORTS ---------------------------
# ---------------------- Variables --------------------
SUCCESS = int(config["global variables"]["SUCCESS"])
NOT_VISIBLE = int(config["global variables"]["NOT_VISIBLE"])
FAILURE = int(config["global variables"]["FAILURE"])

# ---------------------- Variables --------------------

globalReportPyDicObject = { }

# ------------------------- GENERAL FUNCTIONS  ----------------------

def addDataToPythonReport(url, data):  # add data to the report  
    globalReportPyDicObject[url]=data
           
def GetPythonReport(): # return the python report
    return globalReportPyDicObject

def currDateAndTime():# return the current date and time
    try:
        return str(datetime.now().strftime("%d/%m/%Y-%H:%M:%S"))
    except Exception as e:
        return "Date And Time Error"


def writeToReportFile( jsonFileLocation , pyReport):# write the report to a file
    try:
        with open(jsonFileLocation , 'w+') as file:
            overall_perf = pageChecker.getOverallPerformance(report = pyReport)# get overall performance from report 
            report = {"overall_performance": overall_perf , "data" : pyReport , "date_time" : currDateAndTime()}
            file.write(json.dumps(report))
            file.close()
            return SUCCESS
            
    except Exception as e:
        print(e)
        return FAILURE

def readReportFile( jsonFileLocation ):# reads the report from a file
    try:
        with open(jsonFileLocation , 'r') as file:
            
            fileData = file.read()
            file.close()
            return fileData
            
    except Exception as e:
        print(e)
        return FAILURE




# ------------------------- GENERAL FUNCTIONS  ----------------------



