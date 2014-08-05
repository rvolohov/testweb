__author__ = 'roman'

from time import gmtime,strftime
import time
import pytest
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import selenium.webdriver.support.ui as ui
import sys


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

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
    def findElement(self,findBy,val):
        if findBy == "id":
            try:
                element = self.driver.find_element_by_id(val)
                #assert element == True
                #if element:
                self.utils.logMessage("Pass","Element " + val + " found")
                #else:

                #assert element,self.utils.logMessage("Fail","Element " + val + " cannot be found")
            except NoSuchElementException:
            #    self.utils.logMessage("Fail","Element " + val + " cannot be found")
                self.utils.logMessage("Fail","Element " + val + " cannot be found")
            #    with pytest.raises(NoSuchElementException):



        elif findBy == "tbd - add other findBy":
            element = self.driver.find_element_by_id(val)
            assert element,self.utils.logMessage("Fail","Element " + val + " cannot be found")

class Utils:
    def getTimeStamp(self):
        return strftime("%H:%M:%S",gmtime())
    def logMessage(self,status,message):
        if status == "Pass":
            print bcolors.OKGREEN + Utils.getTimeStamp(self) + " PASS: " + message
        elif status == "Fail":
            #@pytest.mark.xfail()
            print bcolors.FAIL + Utils.getTimeStamp(self) + " FAIL: " + message
            #assert result.wasSuccessful(), "Suite failed"
        elif status == "Info":
            print bcolors.OKBLUE + Utils.getTimeStamp(self) + " INFO: " + message
        elif status == "Warning":
            print bcolors.WARNING + Utils.getTimeStamp(self) + " Warning: " + message
        else:
            print bcolors.FAIL + "ERROR: incorrect status"
    def sleep(self,sleepTime):
        self.logMessage("Info","Waiting " + str(sleepTime) + " sec(s)")
        time.sleep(sleepTime)