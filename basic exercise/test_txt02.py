import pytest
import allure

@allure.feature('测试方法1')
def test_passing():
    assert (1,2)==(1,2)
