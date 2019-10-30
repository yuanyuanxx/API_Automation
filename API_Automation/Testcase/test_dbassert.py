# -*- coding:utf-8 -*-

# import sys,os
# print('打印开始')
# print(sys.path)
# sys.path.append('/Users/yuanyuan/PycharmProjects/pytest/API_Automation/Common')
#

# from API_Automation.Common import dbselect
#
#
# import pytest
#
# def test_getuser(db):
#     users=dbselect.select_user(db)
#     print(len(users))
#     assert len(users)==13


import pytest

# class App(object):
#     def __init__(self,smtp_connection):
#         self.smtp_connection = smtp_connection
#
# @pytest.fixture(scope="module")
# def app(smtp_connection):
#     return App(smtp_connection)
#
# def test_smtp_connection_exists(app):
#     assert app.smtp_connection

@pytest.mark.parametrize("test_input,expected",[("3+5",8),
pytest.param("6*9",42,marks=pytest.mark.xfail),
])
def test_eval(test_input,expected):
    assert eval(test_input) == expected