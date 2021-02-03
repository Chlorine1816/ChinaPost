# -*- coding:UTF-8 -*-
import requests,sys
from bs4 import BeautifulSoup

if __name__=='__main__':
    fund1='004698'
    url='http://fundgz.1234567.com.cn/js/001186.js?rt=1463558676006'
    url_2='http://fund.eastmoney.com/004698.html'
    response = requests.get(url_2)

    response.encoding='UTF-8'
    html=response.text
    bf=BeautifulSoup(html,'lxml')

    print(bf)
    #print(answer[1])