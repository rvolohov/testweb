__author__ = 'roman'

from time import gmtime,strftime
import time
import pytest
from selenium import webdriver
import sys

class WebEngine:
    def __init__(self, browserType):
        self.utils = Utils()
        self.utils.logMessage("Info","Web engine initialization...")
        self.utils.logMessage("Info","Starting Selenium WebDriver for browser " + browserType + "...")
        try:
            if browserType == "chrome":
                self.driver = webdriver.Chrome()
                self.utils.logMessage("Pass","Webdriver initialized for " + browserType)
            elif browserType == "firefox":
                self.driver = webdriver.Firefox()
                self.utils.logMessage("Pass","Webdriver initialized for " + browserType)
            else:
                self.utils.logMessage("Fail","ERROR: no webdriver type " + browserType)
        except:
            print "ERROR: Unexpected selenium webdriver error"
            e = sys.exc_info()[0]
    def getWebPage(self,url):
        self.utils.logMessage("Info","Browsing to " + url)
        self.driver.get(url)
    def closeBrowser(self):
        self.driver.close()
        self.utils.logMessage("Info","Test session closed")
class Utils:
    def getTimeStamp(self):
        return strftime("%H:%M:%S",gmtime())
    def logMessage(self,status,message):
        if status == "Pass":
            print Utils.getTimeStamp(self) + " PASS: " + message
        elif status == "Fail":
            print Utils.getTimeStamp(self) + " FAIL: " + message
        elif status == "Info":
            print Utils.getTimeStamp(self) + " INFO: " + message
        elif status == "Warning":
            print Utils.getTimeStamp(self) + " Warning: " + message
        else:
            print "ERROR: incorrect status"
    def sleep(self,sleepTime):
        self.logMessage("Info","Waiting " + str(sleepTime) + " sec(s)")
        time.sleep(sleepTime)