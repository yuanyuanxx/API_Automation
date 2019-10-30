#encoding: utf-8
import pytest
import requests
from API_Automation.Common.ReadExcel import ReadExcel
import  json
from API_Automation.Common.RunMethon import RunMethon
import logging
import logging.config
from os import  path

#---调用记录日志的配置文件-----
#Con_Log_path = path.join(path.dirname(path.abspath(__file__)),'../Config/log.conf')
Con_Log_path = path.join(path.dirname(path.abspath(__file__)),'../Config/log.conf')
logging.config.fileConfig(Con_Log_path)
logging=logging.getLogger()
#---调用记录日志的配置文件-----

data_list = ReadExcel.excel_to_list('/Users/yuanyuan/PycharmProjects/pytest/API_Automation/data/test_user_data.xlsx', 'userlogin')
@pytest.mark.parametrize('casename',['test_user_login_normal01','test_user_login_wrong','test_user_login_normal02'])
def test_user_login_normal(casename):
    logging.info("======用户登陆功能测试=============")
    case_data = ReadExcel.get_test_data(data_list,casename)
    if not case_data:
        print('用例数据不存在')
    url=case_data.get('url') # 从字典中取数据，excel中的标题也必须是小写url
    data=case_data.get('data')# 注意字符串格式，需要用json.loads()转化为字典格式
    expect_res=case_data.get('expect_res')  # 期望数据
    #res=RunMethon.post_moethon(url=url, data=json.loads(data))
    res = requests.post(url=url, data=json.loads(data))
    result=str(res.text)
    logging.info(result)
    assert res.text in expect_res

# @pytest.mark.parametrize('casename',['test_user_reg_exist'])
# def test_user_reg_normal(casename):
#     case_data = ReadExcel.get_test_data(data_list, casename)
#     if not case_data:
#         print("用例数据不存在")
#     url = case_data.get('url')
#     data=json.loads(case_data.get('data')) # 转为字典，需要取里面的name进行数据库检查
#     expect_res=json.loads(case_data.get('expect_res'))# 转为字典，断言时直接断言两个字典是否相等
#     name=data.get("name")
#     res=requests.post(url=url,data=data)
#     # 环境检查
#     if check_user(name):
#         del_user(name)
#     # 发送请求
#     res = requests.post(url=url, json=data)  # 用data=data 传字符串也可以
#     # 响应断言（整体断言）
#     self.assertDictEqual(res.json(), expect_res)
#     # 数据库断言
#     self.assertTrue(check_user(name))
#     # 环境清理（由于注册接口向数据库写入了用户信息）
#     del_user(name)

