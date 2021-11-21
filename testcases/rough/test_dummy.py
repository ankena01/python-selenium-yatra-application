import pytest

from pages.Launch_Page import LaunchPage
from testcases.conftest import setup


@pytest.mark.usefixtures("setup")
def test_search_flights_by_1_stop():
    #global driver
    lp = LaunchPage(setup.driver)
    lp.search_flights("New Delhi" , "New York" , "12/11/2021" , "13/11/2021")