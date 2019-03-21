import pytest
import allure
from API_Automation.Common import Request as br
from API_Automation.Config import  Config

class TestBasic():
    #@allure.feature('测试1')
    #获取 广州2条和上海1条的热映电影
    @pytest.mark.parametrize("das", [{'city': '广州','count':2}, {'city':'上海','count':1}])
    def test_douban_hotshowmovie1(self,das):
        host=Config.get_hostConfig()
        hotshowmoviedata=Config.get_hotshowmovie()
        url='https://'+host+data
        getResponse = br.checkGetSubject(url, das)
    #获取某一部电影信息
    @pytest.mark.parametrize("das", [{'q': '神秘巨星','start':0,'count':2}])
    def test_search_movies(self,das):
        host = Config.get_hostConfig()
        moviesearchdata = Config.get_moviesearch()
        url = 'https://' + host + moviesearchdata
        getResponse = br.checkGetSubject(url, das)



