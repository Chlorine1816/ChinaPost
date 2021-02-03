import pandas as pd
import numpy as np
import os

if __name__=='__main__':
    path_in='./BaiTa/data/'
    path_out='./BaiTa/output/'
    '''
    filename1='1.xlsx'
    filename2='2.xlsx'
    excel1=pd.read_excel(path+filename1,sheet_name='Sheet1',dtype={'邮件号': 'string'})
    excel2=pd.read_excel(path+filename2,sheet_name='Sheet1',dtype={'邮件号': 'string'})
    megre=pd.merge(left=excel1,right=excel2,how='left',left_on='邮件号',right_on='邮件号')
    print(megre.head())
    megre.to_excel(path+'out.xlsx',index=False)
    '''
    filename='1月国际.xls'
    excel=pd.read_excel(path_in+filename,sheet_name='邮件查询')
    grouped=excel.groupby(by=['可售卖产品','大宗客户名称','收寄员'])
    result=grouped.aggregate({'收寄员':np.size,'总邮资':np.sum})
    print(result.head())
    result.to_excel(path_out+'grouped_1月国际.xlsx')