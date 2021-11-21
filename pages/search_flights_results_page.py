import time
import logging
from base.base_driver import BaseDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from utilities.utils import Utils
from testdata.test_data import Test_Data


class SearchFlighResults(BaseDriver):

    log = Utils.custom_logger(logging.DEBUG)

#################### Constructor ####################
    
    def __init__(self , driver):
        super().__init__(driver)
        self.driver = driver

#################### Locators or Object Repository ####################

    #STOP_FIELD_1 = "//p[normalize-space()='1']"
    STOP_FIELD_1 = "//p[@class='font-lightgrey bold'][normalize-space()='1']"
    STOP_FIELD_2 = "//p[@class='font-lightgrey bold'][normalize-space()='2']"
    STOP_FIELD_0 = "//p[@class='font-lightgrey bold'][normalize-space()='0']"

####################  PAGE ACTIONS ####################

    # select 1 stop
    def filter_flights_by_1_stop(self):
        self.do_click(By.XPATH , self.STOP_FIELD_1 ).click()
        
        if len(Test_Data.test_data) > 1:
            self.driver.get("https://www.yatra.com/")
            self.driver.delete_all_cookies()
            self.driver.refresh()

    def filter_flights_by_2_stop(self):
        self.do_click(By.XPATH , self.STOP_FIELD_2 ).click()
        
        if len(Test_Data.test_data) > 1:
            self.driver.get("https://www.yatra.com/")
            self.driver.delete_all_cookies()
            self.driver.refresh()


    def filter_flights_by_0_stop(self):
        self.do_click(By.XPATH , self.STOP_FIELD_0 ).click()

        if len(Test_Data.test_data) > 1:
            self.driver.get("https://www.yatra.com/")
            self.driver.delete_all_cookies()
            self.driver.refresh()



    def filter_flights_by_stop(self , by_stop):

        if by_stop == "1 Stop":
            #print("1 Stop selected")
            self.log.info("1 Stop selected")
            self.filter_flights_by_1_stop()

            
        elif by_stop == "2 Stop":
            #print("2 Stop selected")
            self.log.info("2 Stop selected")
            self.filter_flights_by_2_stop()


        elif by_stop == "Non Stop":
            #print("0 Stop selected")
            self.log.debug("0 Stop selected")
            self.filter_flights_by_0_stop()


        else:
            self.log.debug("Please provide valid filter option")


        
        #self.allstops1 = self.get_list_of_elements(By.XPATH , "//span[contains(text(),'1 Stop') or contains(text(),'Non Stop') or contains(text(),'2 Stop')]")
        #allstops1 = self.get_list_of_elements(By.XPATH , "//span[contains(text(),'1 Stop')]")
        #print(len(allstops1))
        # time.sleep(5)
        # for stop in allstops1:
        #     print("The text is : " + stop.text)
        #     assert stop.text == "1 Stop"
        #     print("assert pass")


        


    


