import pytest
from pages.test_launchpages import test_launchpage
# from ddt import ddt, data, file_data, idata, unpack
@pytest.mark.usefixtures("setup")
# @ddt
class Test_results():

    # @data(("New Delhi" ,"LON" ,"22/08/2022"))
    # @unpack
    def test_checking(self):
        lp = test_launchpage(self.driver)
        lp.flight_search_result("New Delhi" ,"LON" ,"22/08/2022")
        # lp.flight_search_result(depart,goingto,date)



        # lp.flight_search_result("New Delhi","LON","22/08/2022")


