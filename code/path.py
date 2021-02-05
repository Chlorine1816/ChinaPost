import cufflinks as cf
import gopup as gp
import pandas as pd

cf.set_config_file(offline=True)

excel=pd.read_excel('d:/yz/test.xlsx')
lng=excel['lng'].values
lat=excel['lat'].values

min_path=[2, 4, 3, 1]
data=[[lng[0],lat[0],'起点']]
print(data)
for i in range(len(min_path)):
    data.append([lng[min_path[i]],lat[min_path[i]],i+1])

data.append([lng[0],lat[0]])

print(data)
data=pd.DataFrame(data,columns=['lng','lat','text'])
data.iplot(kind='scatter',x='lng',y='lat',text='text',mode=' lines+markers+text',theme='ggplot')