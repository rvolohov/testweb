__author__ = 'roman'

import  pytest
from selenium import webdriver
from WebInfra import *

class Test_SanityTests:
    engine = WebEngine("firefox")
    def test_pretest(self):
        #engine = WebEngine("firefox")
        print "Pretest..."
    def test_openWebPage(self):
        self.engine.getWebPage("http://www.cnn.com")
        self.engine.utils.sleep(5)
    def test_searchForElement_fail(self):
        self.engine.findElement("id","hr-search")
        self.engine.utils.sleep(5)
    def test_searchForElement_pass(self):
        self.engine.findElement("id","hdr-search")
        self.engine.utils.sleep(5)
    def test_postTest(self):
        self.engine.closeBrowser()
