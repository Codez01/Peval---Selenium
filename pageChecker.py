# ------------------------------- IMPORTS ---------------------------

from config import config
from selenium.webdriver.common.by import By
from urllib.parse import urlparse
import seleniumConfig as seleniumConfig
import reportSerializer as reportSerializer
# ------------------------------- IMPORTS ---------------------------

#---------------------- Variables --------------------
isInLambda = config["global variables"]["isInLambda"]# is the program running in Lambda?

SUCCESS = int(config["global variables"]["SUCCESS"])
NOT_VISIBLE = int(config["global variables"]["NOT_VISIBLE"])
FAILURE = int(config["global variables"]["FAILURE"])



#---------------------- Variables --------------------

def getOverallPerformance(report):# returns an object containing the overall performance of backend and front end average measured in seconds
    pyReport = report
    be_sum=0
    fe_sum=0
    for url in pyReport:
        be_sum += pyReport[url]["performance"]["be"]
        fe_sum += pyReport[url]["performance"]["fe"]

    return {"be":round(be_sum/len(pyReport) ,2) ,"fe": round(fe_sum/len(pyReport) ,2) } 

        

def pagePerformanceChecker(url):

    browserDriver = seleniumConfig.SeleniumInit(isInLambda=isInLambda)  # intialize a browser driver with options

    browserDriver.get(url)

    # ! Use Navigation Timing  API to calculate the timings that matter the most
    navigationStart = browserDriver.execute_script(
        "return window.performance.timing.navigationStart")

    # https://developer.mozilla.org/en-US/docs/Web/API/PerformanceTiming/responseStart
    responseStart = browserDriver.execute_script(
        "return window.performance.timing.responseStart")

    # https://developer.mozilla.org/en-US/docs/Web/API/PerformanceTiming/domComplete
    domComplete = browserDriver.execute_script(
        "return window.performance.timing.domComplete")

    # ! Calculate the performance
    backendPerformance_calc = responseStart - navigationStart
    frontendPerformance_calc = domComplete - responseStart

    print("URL: %s" % url)
    print("Back End: %s" % MillisecToSec(backendPerformance_calc))
    print("Front End: %s \n\n" % MillisecToSec(frontendPerformance_calc))

    browserDriver.quit()  # quite the driver --> EXIT
    
    reportSerializer.addDataToPythonReport( url=url ,data={ "performance": {"be" : MillisecToSec(backendPerformance_calc) , "fe": MillisecToSec(frontendPerformance_calc)} })


def mainPagePerformanceCheck(browserDriver, url):

    browserDriver.get(url)

    # ! Use Navigation Timing  API to calculate the timings that matter the most
    navigationStart = browserDriver.execute_script(
        "return window.performance.timing.navigationStart")

    # https://developer.mozilla.org/en-US/docs/Web/API/PerformanceTiming/responseStart
    responseStart = browserDriver.execute_script(
        "return window.performance.timing.responseStart")

    # https://developer.mozilla.org/en-US/docs/Web/API/PerformanceTiming/domComplete
    domComplete = browserDriver.execute_script(
        "return window.performance.timing.domComplete")

    # ! Calculate the performance
    backendPerformance_calc = responseStart - navigationStart
    frontendPerformance_calc = domComplete - responseStart

    print("Main Site  URL: %s" % url)
    print("Main Site Back End: %s" % MillisecToSec(backendPerformance_calc))
    print("Main Site Front End: %s \n\n" % MillisecToSec(frontendPerformance_calc))

    reportSerializer.addDataToPythonReport( url=url ,data={ "performance": {"be" : MillisecToSec(backendPerformance_calc) , "fe": MillisecToSec(frontendPerformance_calc)} })




def validateLink(url):  # checks whether the given URL is valid or not

    # if shceme and netloc are empty then it means that the url is not valid
    return True if str(urlparse(url).scheme) and str(urlparse(url).netloc) else False


# returns a list of all the links in the page
def pageRoutesFinder(browserDriver, url):

    mainPagePerformanceCheck(browserDriver, url)

    list_links = browserDriver.find_elements(
        By.TAG_NAME, 'a')  # find all a tags to filter links
    urls = {}
    for linkObj in list_links:

        link = str(linkObj.get_attribute('href'))  # get the href
        if validateLink(link):  # if the link is valid
            # add to dictionary overwrite duplicates
            urls[link] = {"results": ""}

    browserDriver.quit()  # quite the driver --> EXIT
    return urls


#---------------------- General Functions --------------------'


def MillisecToSec(millisec):  # function for converting milliseconds to seconds
    return millisec/1000


#---------------------- General Functions --------------------