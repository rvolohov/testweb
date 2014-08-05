__author__ = 'roman'

import  pytest
from selenium import webdriver
from WebInfra import *

class Test_SanityTests:
    def test_openWebPage(self):
        engine = WebEngine("chrome")
        engine.getWebPage("http://www.walla.co.il")
        engine.utils.sleep(10)
        engine.closeBrowser()

