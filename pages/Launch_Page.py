from pages.search_flights_results_page import SearchFlighResults
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base.base_driver import BaseDriver
from utilities.utils import Utils
import time
import logging

class LaunchPage(BaseDriver):

#################### Constructor ####################

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

#################### Locators or Object Repository ####################

    DEPART_FROM_FIELD = "//input[@id='BE_flight_origin_city']"
    GOING_TO_FIELD = "//input[@id='BE_flight_arrival_city']"
    ALL_CITIES = "//div[@class='viewport']//div[1]/li"
    DEPART_DATE_FIELD = "//input[@id='BE_flight_origin_date']"
    ARRIVAL_DATE_FIELD = "//input[@id='BE_flight_arrival_date']"
    ALL_DATES = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    SEARCH_FIELD = "#BE_flight_flsearch_btn[value='Search Flights']"

####################  PAGE ACTIONS ####################
    # Get title

    def get_title_launchpage(self,title):
        return self.get_title(title)

    # Get URL

    def get_url_launchpage(self,url):
        return self.get_url(url)


    # Departure Location

    def departfrom(self, departlocation):
        #print(f"Departure location : {departlocation}")
        Utils.custom_logger(logging.INFO).info(f"Departure location : {departlocation}")
        depart_from = self.do_click(By.XPATH , self.DEPART_FROM_FIELD)
        depart_from.click()
        depart_from.send_keys(departlocation)
        time.sleep(3)
        depart_from.send_keys(Keys.ENTER)

    def going_to(self , goingtolocation):
        # Arrival Location
        
        #print(f"Arrival location : {goingtolocation}")
        Utils.custom_logger(logging.INFO).info(f"Arrival location : {goingtolocation}")
        going_to = self.do_click(By.XPATH , self.GOING_TO_FIELD)
        going_to.click()
        going_to.send_keys(goingtolocation)
        search_results = self.get_list_of_elements(By.XPATH , self.ALL_CITIES)
        print("Total search results" , len(search_results))
        for result in search_results:
            if "New York (JFK)" in result.text:
                result.click()
                time.sleep(5)
                break
    
        # Select Departure Date
    def select_depart_date(self , depart_date):
        #print(f"Departure date : {depart_date}")
        Utils.custom_logger(logging.INFO).info(f"Departure date : {depart_date}")
        departure_date_field = self.do_click(By.XPATH , self.DEPART_DATE_FIELD)
        departure_date_field.click()
        self.do_click(By.ID , depart_date).click()
        time.sleep(3)
        

        # Select Arrival Date
    def select_return_date(self , return_date):
        #print(f"Return date: {return_date}")
        Utils.custom_logger(logging.INFO).info(f"Return date: {return_date}")
        arrival_date_field = self.do_click(By.XPATH , self.ARRIVAL_DATE_FIELD)
        arrival_date_field.click()
        arrival_date = self.get_list_of_elements(By.XPATH , self.ALL_DATES)
        for date in arrival_date:
            if date.get_attribute("data-date") == return_date:
                date.click()
                time.sleep(3)
                break


        # Click Search Button
    def clicksearch(self):
        print("Search button clicked")
        Utils.custom_logger(logging.INFO).info("Search button clicked")
        self.do_click(By.CSS_SELECTOR , self.SEARCH_FIELD).click()
        time.sleep(10)    

        # Search Flights

    def search_flights(self , departlocation , goingtolocation , depart_date , return_date):
        self.departfrom(departlocation)
        self.going_to(goingtolocation)
        self.select_depart_date(depart_date)
        self.select_return_date(return_date) 
        self.clicksearch()   

        # Create an object for next page 
        return SearchFlighResults(self.driver)
        


