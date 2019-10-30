import configparser
import pytest
import logging

# # 先构建一个对象
config = configparser.ConfigParser()
# #class  TestCreatIni():
@pytest.fixture()
def create_Config():
    config.add_section("qa-test")
    config.add_section("hostsuffix")
    # 在新增的section下加key-value键值对
    config.set("qa-test","user","zhouyuan")
    config.set("qa-test","host","api.douban.com")
    config.set("hostsuffix","hotshowmovie","/v2/movie/in_theaters?")
    config.set("hostsuffix","moviesearch","/v2/movie/search?")

    #写入文件
    with open('/Users/yuanyuan/PycharmProjects/pytest/API_Automation/Config/config.ini', 'w') as configfile:
        config.write(configfile)
    print('开始添加config数据')


@pytest.mark.usefixtures("create_Config")
def get_hostConfig():
     config.read("/Users/yuanyuan/PycharmProjects/pytest/API_Automation/Config/config.ini")
     #获取它的所有section
     #sections = config.sections()
     hostconfig=config.get('qa-test','host')
     #print('\n--------------------\n',db)
     return hostconfig
'''
    # 获取section下所有的options
    for sec in sections:
        options = config.options(sec)
        print(options)

    # 根据sections和options获取对应的value值
    for sec in sections:
        for option in config.options(sec):
            print("[%s] %s=%s " % (sec, option, config.get(sec, option)))
'''
#@pytest.mark.usefixtures("create_Config")
def get_hotshowmovie():
    config.read("config.ini")
    hotshowmovie = config.get('hostsuffix','hotshowmovie')
    print(hotshowmovie)
    return hotshowmovie

def get_moviesearch():
    config.read("config.ini")
    moviesearch=config.get("hostsuffix","moviesearch")
    return moviesearch


