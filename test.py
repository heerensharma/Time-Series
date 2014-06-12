import pandas as pd 
import numpy as np 
import datetime as dt
import pylab as pl 

data = pd.read_csv("test_data.csv",sep=";",header=0)

# data['start_seen']=[dt.datetime.strptime(ele,"%d.%m.%y %H:%M") for ele in data['start_seen']]

#Step 1 and step2
data['start_seen'] = pd.to_datetime(data['start_seen'],format="%d.%m.%y %H:%M")

data = data.dropna()
#Step 3
data.start_seen = data.start_seen.map(lambda x: x.strftime("%Y-%m-%d"))

df = data.groupby('start_seen').apply(lambda x: x.count())[['start_seen','unique_id']]

df.start_seen = df.index[:]


#lets make some plot to show what you got  May be considered as step 4
pl.figure()

pl.plot(df.unique_id,'o-',color="blue")
count=1
for ele, unique_id in zip(df.index,df.unique_id):
	pl.annotate(str(ele),xy=(count,unique_id),xytext=(count,unique_id+5),ha="right")
	count=count+1
pl.show()


# print df.head()




