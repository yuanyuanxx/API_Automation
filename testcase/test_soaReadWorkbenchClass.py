
from business.apiread import soaReadWorkbenchclass as Workbench
# 2.1 查询所有期
def test004_get_read_period(self):
    #pci.getCaseClassAndCaseName(self.__class__, pci.getCurrentFunctionName())

    # 默认参数
    Workbench.check_get_read_period(params=None, status_exp=0)
