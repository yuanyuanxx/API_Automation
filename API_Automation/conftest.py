import pymysql
import pytest
from py._xmlgen import html
from datetime import datetime


# 测试报告中加入说明列
@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))
    cells.insert(3, html.th('Time', class_='sortable time', col='time'))
    # cells.insert(1,html.th("Test_nodeid"))
    cells.pop()

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    #cells.insert(2, html.td(report.description))
    cells.insert(3, html.td(datetime.utcnow(), class_='col-time'))
    # cells.insert(1,html.td(report.nodeid))
    cells.pop()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")
#测试报告中加入说明代码
#测试报告中加入symmary处加入测试人员姓名
@pytest.mark.optionalhook
def pytest_html_results_summary(prefix,summary,postfix):
    prefix.extend([html.p('测试人：周圆')])



@pytest.fixture(scope='session')
def db():
    #打开数据库
    db=pymysql.connect(host='localhost',user='root',password='',db='Users',port=3306,
                       use_unicode=True,charset='utf8')
    #使用cursor()方法获取操作游标
    #cur=db.cursor()
    return db











