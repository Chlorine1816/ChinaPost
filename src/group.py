import pandas as pd
import os

if __name__=='__main__':
    path='./data/'
    filename='1.xlsx'
    key=os.environ['KEY']
    excel=pd.read_excel(path+filename)
    print(excel.head())
    print(key)