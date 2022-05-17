import time
from urllib.request import Request
from urllib.request import urlopen
import urllib.parse
import datetime
from bs4 import BeautifulSoup


def get_new_notice(website: str):
    # 直接使用 urlopen('网址') 返回 404 错误，对方网站设置有反爬虫机制
    requst = Request(website)
    requst.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')  # 添加请求头，模仿人使用浏览器访问页面
    response = urlopen(requst)
    # 一、获取该网址的源代码
    html = response.read()

    # 二、解析源代码
    bs = BeautifulSoup(html, 'html.parser')  # 爬取该网址的 HTML 源代码
    # print(bs)

    now = time.localtime()

    now_time = time.strftime("%Y-%m-%d", now)

    date_list = []

    # 三、使用 find 方法找到页面上的通知
    # 这里我用最简单的方式，把第一页的所有数据找到，最新的通知一般不会超过第一页，我的功能只是一个提醒，只要有数据提醒就行，并无大碍
    # find 返回的是单个  find_all 返回的是多个 - list
    date_list1 = bs.find('li', {'class': 'list_item i1'})
    date_list.append(date_list1)
    name_list2 = bs.find('li', {'class': 'list_item i2'})
    date_list.append(name_list2)
    name_list3 = bs.find('li', {'class': 'list_item i3'})
    date_list.append(name_list3)
    name_list4 = bs.find('li', {'class': 'list_item i4'})
    date_list.append(name_list4)
    name_list5 = bs.find('li', {'class': 'list_item i5'})
    date_list.append(name_list5)
    name_list6 = bs.find('li', {'class': 'list_item i6'})  #
    date_list.append(name_list6)
    name_list7 = bs.find('li', {'class': 'list_item i7'})  #
    date_list.append(name_list7)
    name_list8 = bs.find('li', {'class': 'list_item i8'})  #
    date_list.append(name_list8)
    name_list9 = bs.find('li', {'class': 'list_item i3'})  #
    date_list.append(name_list9)

    # print(date_list)
    for i in date_list:

        span_list = i.find_all("span")

        span_time = span_list[2].get_text()
        cc = span_time
        #  print(name_list1)  # 爬取的的结果存放在列表中，使用时需要加下标，否则会报错
        #   print(span_time)
        #  print(now_time)
        if span_time == now_time:
            # AttributeError: ResultSet object has no attribute 'find_all'.
            #  print(cc)

            span_date = span_list[1].get_text()

            #  print(span_date)

            return span_date

            # print("不是今天")
            # return span_date

