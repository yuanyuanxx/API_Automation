import pytest

a=[2,5,4]
def  test_main():
    assert 4 in a

#运行模块中，测试类里面的某个方法  pytest  basic\ exercise/test_txt02.py::test_sum
#当前目录下执行用例并生成报告：basic exercise yuanyuan$ pytest --html=report.html --self-contained-html

if __name__=='__mian__':
    #制定某个测试文件
    pytest.main("pytest exe01/")
    #指定测试目录
    #pytest.main("/users/yuanyuan/PycharmProjects/pytest/exe01")

