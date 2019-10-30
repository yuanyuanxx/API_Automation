import yaml
import os


class  InterInfo(object):
    # 获取当前脚本所在文件夹路径
    curPath = os.path.dirname(os.path.realpath(__file__))
    # 获取yaml文件路径
    yamlPath = os.path.join(curPath, "base_info.yaml")

    with open(yamlPath, 'r', encoding='utf-8') as file:
        data = yaml.load(file)

    def hujiangUrl(self):
        hujiang_Url=self.data['hujiangUrl']
        print(hujiang_Url)
        return hujiang_Url

    def mukestudyUrl(self):
        mukestudy_Url = self.data['mukestudyUrl']
        return mukestudy_Url


