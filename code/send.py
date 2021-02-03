# -*- coding: utf8 -*-
import requests,os

# 微信推送
def pushWechat(desp):
    params = {'text':'Github_BaiTa','desp':desp}
    requests.post(scurl,params=params)

def writedesp(desp,num,addstr):
    desp+='Step'+str(num)+': '+addstr+'\n\n'
    return desp

if __name__ == "__main__":
    SCKEY=os.environ['PUSHSCKEY']
    scurl = f"https://sc.ftqq.com/{SCKEY}.send"
    desp=''
    for i in range(1,3):
        desp=writedesp(desp,i,'updata')
    pushWechat(desp)