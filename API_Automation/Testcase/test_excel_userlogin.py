#encoding: utf-8
import pytest
import requests
from API_Automation.Common.ReadExcel import ReadExcel
import  json
from API_Automation.Common.RunMethon import RunMethon
import logging
import logging.config
from os import  path
import  xlrd    #读取excel
import xlwt     #写入excel
from  xlutils.copy import copy #操作excel文件的的实用工具，如负责、分割、筛选


#---调用记录日志的配置文件-----
Con_Log_path = path.join(path.dirname(path.abspath(__file__)),'../Config/log.conf')
logging.config.fileConfig(Con_Log_path)
logging=logging.getLogger()
#---调用记录日志的配置文件-----

data_list = ReadExcel.excel_to_list('/Users/yuanyuan/PycharmProjects/pytest/API_Automation/data/test_user_data.xlsx', 'userlogin')
@pytest.mark.parametrize('casename',['test_user_login_normal01正确','test_user_login_wrong','test_user_login_normal02'])
def test_user_login_normal(casename):
    logging.info("======用户登陆功能测试=============")
    case_data = ReadExcel.get_test_data(data_list,casename)
    if not case_data:
        print('用例数据不存在')
    id=case_data.get('case_id')
    print(id)
    url=case_data.get('url') # 从字典中取数据，excel中的标题也必须是小写url
    data=case_data.get('data')# 注意字符串格式，需要用json.loads()转化为字典格式
    expect_res=case_data.get('expect_res')  # 期望数据
    res = requests.post(url=url, data=json.loads(data))
    #print("内容为：%s" %res.text)
    logging.info(res)
    if res.text == expect_res:
        print("成功")
        result='成功'
    else:
        print('失败')
        result='失败'
    #回写测试结果
    # oldwb = xlrd.open_workbook('/Users/yuanyuan/PycharmProjects/pytest/API_Automation/data/test_user_data.xlsx')#formatting_info=True
    # newwb=copy(oldwb)
    # newws=newwb.get_sheet(0)
    # newws.write(id,9,result)
    # newwb.save('/Users/yuanyuan/PycharmProjects/pytest/API_Automation/data/test_user_data.xlsx')



