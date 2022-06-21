import pytest
from pages.test_launchpages import test_launchpage
from ddt import ddt, data, file_data, idata, unpack
@pytest.mark.usefixtures("setup")
# @ddt
class TestFlightResults():
    depart ="New Delhi"
    goingto= "LON"
    date="22/08/2022"
#     @data(("New Delhi" ,"LON" ,"22/08/2022"))
#     @unpack
    def test_checking(self,depart,goingto,date):
        lp = test_launchpage(self.driver)
        # lp.flight_search_result("New Delhi" ,"LON" ,"22/08/2022")
        lp.flight_search_result(self.depart,self.goingto,self.date)



        # lp.flight_search_result("New Delhi","LON","22/08/2022")


