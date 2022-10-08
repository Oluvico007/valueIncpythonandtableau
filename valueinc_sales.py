# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 22:00:23 2022

@author: Ogunyemi Victor O
"""

import pandas as pd

# file_name = pd.read_csv('file.csv') <---- format of read_csv

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv', sep=';')

#summary of the data
data.info()

#working with calculations

#Defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemsPurchased = 6

#Mathematical Operations on Tableau

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberofItemsPurchased*ProfitPerItem
CostPerTransaction = CostPerItem*NumberofItemsPurchased
SellingPricePerTransaction = SellingPricePerItem*NumberofItemsPurchased

#CostPerTransaction Column Calculation for Value Inc. DATA

#Since CostPerTransaction = CostPerItem * NumberofItemPurchased
#variable = dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberofItemsPurchased

#adding a new column to a dataframe

data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

#Sales Per Transaction
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit Calculation = Sales - Cost

data['ProfitperTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup = (Sales-Cost)/Cost

data['Markup'] = ( data['SalesPerTransaction'] - data['CostPerTransaction'] )/data['CostPerTransaction']

#Rounding Markup

roundmarkup = round(data['Markup'], 2)

data['Markup'] = round(data['Markup'], 2)

#Combining data fields

my_name = 'Victor'+'O'
my_date = 'Day'+'-'+'Month'+'-'+'Year'

#change columns type

day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)
print(year.dtype)


my_date = day+'-'+data['Month']+'-'+year

data['date'] = my_date

#using iloc to view specific columns/rows

data.iloc[0] #view the row with index = 0
data.iloc[0:3] #first 3 rows
data.iloc[-5:] #last 5 rows

#OR
data.head(5) #brings in first 5 rows

data.iloc[:,2] #brings all rows on the 2nd column

data.iloc[4,2] #brings in 4th row, 2nd column


#using split to split the client_keywords field
#new_var = column.str.split('sep' , expand = True)

split_col = data['ClientKeywords'].str.split(',' , expand=True)

#Creating new columns for the split columns in Client Keywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]

#using the replace function

data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthofContract'] = data['LengthofContract'].str.replace(']' , '')

#using the lower function to change item to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files

#bringing in a new dataset

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')


data = pd.merge(data, seasons, on = 'Month')

#dropping columns

#df = df.drop('columnname' , axis = 1)

data = data.drop('ClientKeywords', axis = 1)
data = data.drop('Day', axis = 1)
data = data.drop(['Year', 'Month'], axis = 1)

#Export new cleaned data into csv

#data.to_csv('ValueInc_Cleaned.csv', index = False)


