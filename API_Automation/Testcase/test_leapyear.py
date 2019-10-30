
from API_Automation.Common import is_leap_year
import pytest
import unittest

class TestTeapYear():
    is_leap=[4,40,400,1200,1996,2996]
    is_not_leap=[1,100,500,1000,1999,7000]
    is_valueerror=[0,-4,-100,-400,-2000,-1966]
    is_typeerror=['/',2.56,'-1','d','三岁',' ']

    @pytest.fixture(params=is_leap)
    def is_leap(self, request):
        return request.param



    @pytest.fixture(params=is_valueerror)
    def is_valueerror(self, request):
        return request.param

    @pytest.fixture(params=is_typeerror)
    def is_typeerror(self, request):
        return request.param

    def test_is_leap(self,is_leap):
        assert is_leap_year.is_leap_year(is_leap)==True

    def test_is_valueerror(self,is_valueerror):
        with pytest.raises(ValueError):
            is_leap_year.is_leap_year(is_valueerror)

    def test_is_typeerror(self,is_typeerror):
        with pytest.raises(TypeError):
            is_leap_year.is_leap_year(is_typeerror)

    @pytest.mark.parametrize('year', is_not_leap)
    def test_is_not_leap(self, year):
        assert is_leap_year.is_leap_year(year) == False

