# @ Author Nagendra T V, 10-04-2019
# -*- coding: utf-8 -*-
# imports
import time
import unittest
import os
from appium import webdriver
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))

class Android_Monarch_Test(unittest.TestCase):
    # Class to run tests against the Monarch app

    def setUp(self):
        # Setup for the test
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['deviceName'] = 'Android_Device'
       
        desired_caps['app'] = PATH('Monarch.apk')
         # Since the app is already installed launching it using package and activity name is not working as activity is not exposed 
        #desired_caps['appPackage'] = 'com.hillrom'
        #desired_caps['appActivity'] = 'com.hillrom.views.OnlineOfflineSelectActivity'
        desired_caps['noReset'] = True
        # To prevent app from resetting every time you launch tests
        #desired_caps['appWaitActivity'] = 'com.hillrom.views.OnlineOfflineSelectActivity'
        # Adding appWait Activity since the activity name changes as the focus shifts to the Monarch app's first page
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        # Tear down the test
        self.driver.quit()

    def test_HillRom_MonarchDemo(self):
        self.driver.implicitly_wait(30)
        # Waiting for screen to load
        try:
              self.driver.find_element_by_id("com.hillrom:id/activity_onlinedemomode_img_demo").click()
              self.driver.find_element_by_id("com.hillrom:id/activity_offline_gototherapy_btn_goto").click()
              self.driver.find_element_by_id("com.hillrom:id/activity_therapy_home_txt_freq").click()
              self.driver.find_element_by_id("com.hillrom:id/activity_therapy_home_txt_inte").click()
              self.driver.find_element_by_id("com.hillrom:id/activity_therapy_home_txt_dura").click()
              self.driver.find_element_by_id("com.hillrom:id/activity_therapy_home_btn_start").click()

             
        except Exception, e:
            print ('Failed: ' + str(e))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Android_Monarch_Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
