import pandas as pd 
import numpy as np 
import datetime as dt
import pylab as pl 


#base class for time series filtering 

class InitialAnalysis(object):


	def __init__(self,dataset):
		self.data = dataset


	#tranfer desired time column upto particular precision
	def transf_col(self,time_column,initial_date_format,converted_date_format):
		#Step 1 and step2
		self.time_column = time.column
		self.init_dtf = initial_date_format
		self.conv_dtf = converted_date_format
		self.data[self.time_column] = pd.to_datetime(self.data[self.time_column],format=self.init_dtf)

		self.data = self.data.dropna()
		#Step 3
		self.data[self.time_column] = self.data[self.time_column].map(lambda x: x.strftime(self.conv_dtf))

	#these grouping functions are used to analyze column with specific details.
	#e.g. mean, count number of rows, median, and mode.
	def analysis(self, grouping_func, action_col):
		self.action_col = action_col
		self.df = self.data.groupby(self.time_column).apply(lambda x: x.count())[[self.time_column,self.action_col]]

		df[self.time_column] = df.index[:]


	def give_plot():
		pl.figure()

		pl.plot(self.df[self.action_col],'o-',color="blue")
		count=1
		for ele, unique_id in zip(self.df.index,self.df[self.action_col]):
			pl.annotate(str(ele),xy=(count,unique_id),xytext=(count,unique_id+5),ha="right")
			count=count+1
		pl.show()


