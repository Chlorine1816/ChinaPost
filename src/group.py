import pandas as pd
import numpy as np

if __name__=='__main__':
    path='./data/'
    filename='1.xlsx'
    excel=pd.read_excel(path+filename)
    print(excel.head())
    excel.to_excel(path+'2.xlsx')