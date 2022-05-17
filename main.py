import time

from email163 import send_email
from spider import get_new_notice

import schedule

data_update = get_new_notice("https://www.fjut.edu.cn/561/list.htm")

str1 = "福建理工大学"
str2 = "更名"
str3 = "大学"


def run():
    if str1 in data_update or (str2 in data_update and str3 in data_update):
        #  或 可以发邮件者 发短信  进行通知可以定时每一个小时访问一次
       # print("特\"大\"喜讯!教育部正式批复，我校更名为福建理工大学")
        send_email("特\"大\"喜讯!教育部正式批复，我校更名为福建理工大学")
        print(time.localtime())
    else:
        print("No new notifications ")


schedule.every(1).hours.do(run)  # 每隔一小时执行一次
# 先执行一次
run()

while True:
    # run_pending：运行所有可以运行的任务
    schedule.run_pending()
