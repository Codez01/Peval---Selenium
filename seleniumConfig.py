# ------------------------------- IMPORTS ---------------------------
from config import config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import threadsManager as threadsManager
# ------------------------------- IMPORTS ---------------------------

#---------------------- Variables --------------------
SUCCESS = int(config["global variables"]["SUCCESS"])
NOT_VISIBLE = int(config["global variables"]["NOT_VISIBLE"])
FAILURE = int(config["global variables"]["FAILURE"])


#---------------------- Variables --------------------

# ------------------------- GENERAL FUNCTIONS  ----------------------
def SeleniumInit(isInLambda):  # functions for setting up selenium with options and driver

    options = Options()

    if(isInLambda == "true"):# if the program is running in lambda
        options = webdriver.ChromeOptions()
        options.binary_location = '/opt/headless-chromium'
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--single-process')
        return webdriver.Chrome('/opt/chromedriver', chrome_options=options)

    else: # if the program is not running in lambda  

        from webdriver_manager.chrome import ChromeDriverManager# import chrome driver 

        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--window-size=1920,1080")
        return webdriver.Chrome(ChromeDriverManager().install(), options=options)

# ------------------------- GENERAL FUNCTIONS  ----------------------
