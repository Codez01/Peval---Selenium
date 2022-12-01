#---------------------- IMPORTS ----------------------
import threading
import time
import sys
from config import config
#---------------------- IMPORTS ----------------------


#---------------------- Variables --------------------
SUCCESS = int(config["global variables"]["SUCCESS"])
NOT_VISIBLE = int(config["global variables"]["NOT_VISIBLE"])
FAILURE = int(config["global variables"]["FAILURE"])

THREADS_SUPPORT = int(config["threads"]["threadsSupport"])# take the threads number from config
threadsList = []# list that will hold the threads stopped / running
#---------------------- Variables --------------------


#---------------------- Functions --------------------

# returns SUCCESS if there is an available thread, Failure otherwise
def isThreadAvailable(threadsList):
    #Wait all threads to finish.
    for index,thread in enumerate(threadsList):
        if not thread.is_alive():
            threadsList.pop(index)
            
    return SUCCESS if len(threadsList) < THREADS_SUPPORT else FAILURE


def threadHandler(url , function , arg1):  # handles the threads and the results

    try:

        # if there isn't an available thread
        while isThreadAvailable(threadsList) == FAILURE: time.sleep(2)# wait if there is a failure

        thread = threading.Thread(target=function, args=(arg1,)) # create a thread
        thread.start()# start thread
        threadsList.append(thread)# append thread to list
        print("Thread started for %s" % url)

    except:

        print("Threads Unexpected Error")
        sys.exit(1)

def waitForThreadsToFinish(): # wait for all threads to finish
    try:
        for thread in threadsList:
            thread.join()
    except:
        raise("Unable To Wait For Threads To Finish.")        


#---------------------- Functions --------------------
