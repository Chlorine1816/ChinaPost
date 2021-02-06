import numpy as np
import pandas as pd
import math
import cufflinks as cf

def CalDistance(x,y):
    return math.sqrt(x**2+y**2)

def save_excel(data):
    data_pd=pd.DataFrame(np.arange(num*num).reshape(num,num),columns=[str(i) for i in range(num)])
    for i in range(num):
        data_pd[str(i)]=data[:][i]
    data_pd.reset_index()
    data_pd.to_excel(path+filename_new,'Sheet1',float_format='%.5f')

if __name__=='__main__':
    path='d:/yz/'
    filename='test.xlsx'
    filename_new='Dis_'+filename
    excel_1=pd.read_excel(path+filename)

    lng=excel_1['lng'].values
    lat=excel_1['lat'].values
    num=len(lng)

    data=[]
    for i in range(num):
        data+=[[]]
        for j in range(num):
            data[i].append(0)

    for i in range(num-1):
        for j in range(i+1,num):
            data[i][j]=CalDistance(lng[i]-lng[j],lat[i]-lat[j])
            data[j][i]=data[i][j]
    save_excel(data)