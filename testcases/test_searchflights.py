# Here we will write our test cases for Home Page
import pytest
import softest
from pages.Launch_Page import LaunchPage
from pages.search_flights_results_page import SearchFlighResults
from testdata.test_data import Test_Data
import time
from ddt import ddt , data , unpack, file_data
from utilities.utils import Utils
import logging
from selenium.common.exceptions import ElementClickInterceptedException , StaleElementReferenceException , TimeoutException


@pytest.mark.usefixtures("setup")
#@ddt
class Test_Flights:
    
    #ut = Utils()
    
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        
        
    
    
    def test_title_url_check(self):
        assert self.lp.get_title_launchpage("Flight, Cheap Air Tickets , Hotels, Holiday, Trains Package Booking - Yatra.com") == True
        assert self.lp.get_url_launchpage("https://www.yatra.com/") == True
        
        #self.soft_assert(self.assertTrue , self.lp.get_title_launchpage("Flight, Cheap Air Tickets , Hotels, Holiday, Trains Package Booking - Yatra.com") , True)
        # self.soft_assert(self.assertTrue , self.lp.get_url_launchpage("https://www.yatra.com/") , True)
        # self.assert_all()

    

    # @data(("New Delhi" , "New York" , "15/11/2021" , "17/11/2021" , "1 Stop"))
    # @unpack

    #@file_data("../testdata/testdata.json")
    #@file_data('../testdata/testdata.yaml')
    
    # @data(*ut.read_data_from_excel(file_path="C:\\temp\\TestFrameWorkDemo\\testdata\\testdata.xlsx"))
    # @unpack

    # @data(*ut.read_data_from_csv(file_path="C:\\temp\\TestFrameWorkDemo\\testdata\\testdata.csv"))
    # @unpack

    #@pytest.mark.parametrize("departlocation , goingtolocation , depart_date , return_date, stops",Test_Data.test_data)
    #@pytest.mark.parametrize("departlocation , goingtolocation , depart_date , return_date, stops",Utils.read_data_from_excel('./testdata/testdata.xlsx'))
    @pytest.mark.parametrize("departlocation , goingtolocation , depart_date , return_date, stops",Utils.read_data_from_csv('./testdata/testdata.csv'))
    def test_search_flights(self,departlocation , goingtolocation , depart_date , return_date, stops):
    #def test_search_flights(self):

        # Page 1
        
        #sf = self.lp.search_flights("New Delhi" , "New York" , "15/11/2021" , "17/11/2021")
        try:
            sf = self.lp.search_flights(departlocation , goingtolocation , depart_date , return_date)
        except (ElementClickInterceptedException , TimeoutException) as e:
            Utils.custom_logger(loglevel=logging.DEBUG).exception(str(e))
        except (StaleElementReferenceException) as e:
            Utils.custom_logger(loglevel=logging.DEBUG).exception(str(e))
        except (UnboundLocalError) as e:
            Utils.custom_logger(loglevel=logging.DEBUG).exception(str(e))

        

        # Page 2
        #Page Scroll

        self.lp.page_scroll()
        try:
            sf.filter_flights_by_stop(stops)
        except (ElementClickInterceptedException,UnboundLocalError,StaleElementReferenceException) as e:
            Utils.custom_logger(loglevel = logging.DEBUG).exception(str(e))
        
        time.sleep(5)

    
    






