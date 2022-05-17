import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_email(text):
    # 这里使用的是163.com
    mail_host = "smtp.163.com"  # 设置服务器       邮箱服务器
    mail_user = "15243666065@163.com"  # 用户名   邮箱账号
    mail_pass = "2997854889"  # 口令              邮箱密码

    sender = '15243666065@163.com'  # 发送邮箱  和上方用户名一致
    receivers = ['2997854889@qq.com']  # 接收者的邮箱
    message = MIMEText(text, 'plain', 'utf-8')
    message['From'] = Header('FJUT')
    message['To'] = Header("2997854889")  # 填写接收人账号 @ 前 字符串  比如邮箱为 297854888@qq.com  则填写 2997854888

    subject = 'Congratulations'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        print(1)
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        print(2)
        smtpObj.login(mail_user, mail_pass)
        print(3)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")
