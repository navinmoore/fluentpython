# coding:utf-8

import smtplib
from  celery_app import app
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

my_sender='wangzhiyao@apluslabs.com'  
my_pass = "pass"

receiver = ["258641620@qq.com"]

@app.task
def sendParentMail(name):
    ret=True
    try:
        # 邮件内容
        text = "名为:{}的专利临近到期，请上work系统上查看并处理，请注意：此邮件只提醒一次！".format(name)
        msg=MIMEText(text,'plain','utf-8')
        # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['From']=formataddr(["系统提醒",my_sender])  
        # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        # msg['To']=formataddr(["xx","258641620@qq.com"])   
        # 邮件的主题           
        msg['Subject']="专利缴费提醒"                
 
        # SMTP服务器，腾讯企业邮箱端口是465，腾讯邮箱支持SSL(不强制)， 不支持TLS
        # qq邮箱smtp服务器地址:smtp.qq.com,端口号：456
        # 163邮箱smtp服务器地址：smtp.163.com，端口号：25
        server=smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)  
        # 登录服务器，括号中对应的是发件人邮箱账号、邮箱密码
        server.login(my_sender, my_pass)  
        # 发送邮件，括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.sendmail(my_sender, receiver, msg.as_string())  
        # 关闭连接
        server.quit() 
        # 如果 try 中的语句没有执行，则会执行下面的 ret=False 
    except Exception:  
        ret=False
    return ret