import pandas as pd

if __name__=='__main__':
    path='./data/'
    filename1='1.xlsx'
    filename2='2.xlsx'
    excel1=pd.read_excel(path+filename1,sheet_name='Sheet1',dtype={'邮件号': 'string'})
    excel2=pd.read_excel(path+filename2,sheet_name='Sheet1',dtype={'邮件号': 'string'})
    megre=pd.merge(left=excel1,right=excel2,how='left',left_on='邮件号',right_on='邮件号')
    print(megre.head())
    megre.to_excel(path+'out.xlsx',index=False)

    #grouped=excel2.groupby(by=['可售卖产品','收寄员'])
    #result=grouped.aggregate({'收寄员':np.size,'总邮资':np.sum})
    #print(result.head())
    #result.to_excel(path+'out.xlsx')