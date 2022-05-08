import logging
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from base.basedriver import Basedriver
from utilities.utils import Utils

class test_launchpage(Basedriver):
    def __init__(self,driver):
        super().__init__(self)
        self.driver=driver

    depart_from="//input[@id='BE_flight_origin_city']"
    going_to="//input[@id='BE_flight_arrival_city']"
    search_city="//div[@class='viewport']//div/li"
    searchdate="//input[@id='BE_flight_origin_date']"
    all_dates="//div[@id='monthWrapper']//td[@class!='inActiveTD']"
    search_click="//input[@id='BE_flight_flsearch_btn'][contains(@value,'Search Flights')]"
    ut = Utils()
    log=ut.customer_logging(logLevel=logging.DEBUG)
    def search_departure(self):
        return self.element_to_be_clickable(By.XPATH,self.depart_from)
    def search_goingTo(self):
        return self.element_to_be_clickable(By.XPATH,self.going_to)
    def flight_search_city(self):
        return self.presence_elements(By.XPATH,self.search_city)
    def search_all_date(self):
        return self.element_to_be_clickable(By.XPATH,self.all_dates)
    def search_button(self):
        return self.element_to_be_clickable(By.XPATH,self.search_click)

    def get_depart(self,depart):
        self.search_departure().click()
        self.search_departure().send_keys(depart)
        self.search_departure().send_keys(Keys.ENTER)
    def get_goingTO(self,goingto):
        self.search_goingTo().click()
        self.search_goingTo().send_keys(goingto)
        results=self.flight_search_city()
        # print(len(results))
        self.log.debug(len(self.flight_search_city()))
        for city in results:
            if "London (LON)"in city.text:
                city.click()
                break
    def get_Date(self,date):
        self.driver.find_element(By.XPATH,self.searchdate).click()
        all_date=self.search_all_date().find_elements(By.XPATH,self.all_dates)
        # print(len(all_date))
        self.log.debug(len(all_date))
        time.sleep(3)
        for dt in all_date:
            if dt.get_attribute("data-date")==date:
                dt.click()
                time.sleep(4)
                break
    def get_click_buton(self):
        self.driver.find_element(By.XPATH,self.search_click).click()
        time.sleep(4)



    def flight_search_result(self,departloc,goingloc,search_date):
        self.get_depart(departloc)
        self.get_goingTO(goingloc)
        self.get_Date(search_date)
        self.get_click_buton()
