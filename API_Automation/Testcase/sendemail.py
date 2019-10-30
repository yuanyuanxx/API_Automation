# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import pytest



def sendemail():
    # 发送邮箱服务器
    smtpserver = "smtp.126.com"

    # 发送邮箱用户名密码
    user = "zyj420@126.com"
    password = "zhouyuan30"

    # 发送和接收邮箱
    sender = "zyj420@126.com"
    # 多个收件人在列表中以逗号隔开
    receive = "415592428@qq.com"

    # 创建一个带附件的实例
    message = MIMEMultipart()
    # message['From'] = Header("ZY自动化测试", 'utf-8')
    # message['To'] = Header("测试", 'utf-8')
    message['from'] = "zyj420@126.com"
    message['to'] = "415592428@qq.com"
    subject = '主题：自动化测试报告'
    message['Subject'] = Header(subject, 'utf-8').encode()



    # 邮件正文内容
    # message.attach(MIMEText('这是最新的测试结果报告', 'plain', 'utf-8'))

    # 构造附件1，传送当前目录下的 test.txt 文件
    with open('/Users/yuanyuan/PycharmProjects/pytest/API_Automation/Testcase/report.html','rb') as f:
        mailbody=f.read()
        html = MIMEText(mailbody, _subtype='html', _charset='utf-8')  # 将测试报告的内容放在 邮件的正文当中
        message.attach(html)

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(smtpserver, 25) # 25 为 SMTP 端口号
        smtpObj.login(user, password)
        smtpObj.sendmail(sender, receive, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")
    smtpObj.close()
