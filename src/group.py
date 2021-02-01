# -*- coding: utf8 -*-
import requests,datetime,pytz,os

# 微信推送
def pushWechat(desp,nowtime):
    params = {
        #消息名称
        'text': '当前时间',
        #消息内容 
        'desp': desp        
        }
    requests.post(scurl,params=params)

if __name__ == "__main__":
    SCKEY = os.environ['PUSHSCKEY']
    #SERVER酱微信推送url
    scurl = f"https://sc.ftqq.com/{SCKEY}.send"
    tz = pytz.timezone('Asia/Shanghai')
    nowtime = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
    desp='测试成功！'+ nowtime
    pushWechat(desp,nowtime)