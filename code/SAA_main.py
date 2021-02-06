import pandas as pd
import numpy as np
import math,os,requests
#import cufflinks as cf

# 微信推送
def pushWechat(desp):
    params = {'text':'Github_BaiTa','desp':desp}
    requests.post(scurl,params=params)

def writedesp(desp,addstr1,addstr2):
    desp+=addstr1+': '+addstr2+'\n\n'
    return desp

def CalLength(excel_dis,paths):
    lenth=0
    lenth+=excel_dis[0][paths[0]]
    lenth+=excel_dis[paths[-1]][0]
    for i in range(num-2):
        lenth+=excel_dis[paths[i]][paths[i+1]]
    return (lenth)

def CalDistance(x,y):
    return math.sqrt(x**2+y**2)

#展示最短路径
'''
def show_path(excel,min_path):
    cf.set_config_file(offline=True)
    lng=excel['lng'].values
    lat=excel['lat'].values
    data=[[lng[0],lat[0],'起点']]
    for i in range(len(min_path)):
        data.append([lng[min_path[i]],lat[min_path[i]],i+1])
    data.append([lng[0],lat[0]])
    data=pd.DataFrame(data,columns=['lng','lat','text'])
    data.iplot(kind='scatter',x='lng',y='lat',colors='blue',text='text',mode=' lines+markers+text',theme='ggplot')
'''

#距离矩阵
def get_dis(excel_1):
    lng=excel_1['lng'].values
    lat=excel_1['lat'].values
    data=[]
    for i in range(len(lng)):
        data+=[[]]
        for j in range(len(lng)):
            data[i].append(0)
    for i in range(len(lng)-1):
        for j in range(i+1,len(lng)):
            data[i][j]=CalDistance(lng[i]-lng[j],lat[i]-lat[j])
            data[j][i]=data[i][j]
    return data

if __name__=='__main__':
    path='./baita/data/'
    filename='points.xlsx'
    SCKEY=os.environ['PUSHSCKEY']
    scurl = f"https://sc.ftqq.com/{SCKEY}.send"
    
    excel=pd.read_excel(path+filename)
    excel_dis=get_dis(excel)
    excel_dis=np.array(excel_dis).reshape(excel.shape[0],-1)

    num=excel_dis.shape[0] #节点个数
    min_dispath=[x for x in range(1,num)] # 0 为起点、终点 
    min_disans=CalLength(excel_dis,min_dispath)
    
    desp='-----------日志输出-----------\n\n'
    desp=writedesp(desp,'原始路径',str(min_dispath))
    desp=writedesp(desp,'原始长度',str(min_disans))

    #初始化一个解
    #方案一
    city_list=min_dispath.copy()
    #方案二
    #paths=[i for i in range(1,num)]
    #city_list=list(np.random.permutation(paths))

    T0 = 111*num     #初始温度
    T_end = 1e-5     #结束温度
    q = 0.98         #降温系数
    L=11*num         #每个温度迭代次数
    t=0              #降温次数初始化
    T=T0             #初始温度
    city_list_copy=[]#保存原始解
    ans=0            #路径长度

    desp=writedesp(desp,'初始温度',str(T0))
    desp=writedesp(desp,'降温系数',str(q))
    desp=writedesp(desp,'节点数目',str(num))
    desp=writedesp(desp,'迭代次数',str(L))

    while (T>T_end):
        for i in range(L):
            #复制数组
            city_list_copy=city_list.copy()
            #产生新解
            a=np.random.randint(0,num-1)
            b=np.random.randint(0,num-1)

            if (a==b):
                continue
        
            city_list[a],city_list[b]=city_list[b],city_list[a]

            f1=CalLength(excel_dis,city_list_copy)  #原始状态
            f2=CalLength(excel_dis,city_list)       #更新状态
            df=f2-f1
            ans=f2

            if (min_disans>f2):
                min_disans=f2
                min_dispath=city_list.copy()
                '''
                desp+=('-----------第'+str(t+1)+'次降温'+'-----------\n\n')
                desp=writedesp(desp,'当前温度',str(round(T,5)))
                desp=writedesp(desp,'当前路径',str(min_dispath))
                desp=writedesp(desp,'当前长度',str(min_disans))
                '''
            elif (df>=0):
                r=np.random.rand() # 0-1的随机数，用来决定是否接受新解
                if (math.exp(-df/T)<=r):
                    city_list=city_list_copy.copy()   
                    ans=f1 
        T*=q #降温
        t+=1

    desp+='-----------输出结果-----------\n\n'
    desp=writedesp(desp,'降温次数',str(t))
    desp=writedesp(desp,'最短路径',str(min_dispath))
    desp=writedesp(desp,'路径长度',str(min_disans))

    #show_path(excel,min_dispath)
    pushWechat(desp)