# -*- coding: utf-8 -*-

#"Created on Tue Jan  3 10:30:42 2017"

#'@author: Ashish'

#Import the necessary library
import pandas
import numpy

#Load the data from CSV file
data = pandas.read_csv('GapMinder_mine.csv', low_memory=False)

#Print the number of rows and columns
print('Number of Rows:')
print(len(data))
print('Number of Columns:')
print(len(data.columns))

#To ensure data is in numeric format
data['co2emissions'] = data['co2emissions'].convert_objects(convert_numeric=True)
data['lifeexpectancy'] = data['lifeexpectancy'].convert_objects(convert_numeric=True)
data['urbanrate'] = data['urbanrate'].convert_objects(convert_numeric=True)

#Minimum and maximum values for CO2Emissions
print('Minimum value for CO2Emissions :')
CO2Min=data['co2emissions'].min()
print(CO2Min)
print('Maximum value for CO2Emissions :')
CO2Max=data['co2emissions'].max()
print(CO2Max)

sub1=data[(data['co2emissions']>=CO2Min) & (data['co2emissions']<=CO2Max) ]

#Break the data into class intervals
sub1['co2emissionsGroup'] = pandas.cut(sub1.co2emissions, [132000.0, 66800158400, 133600184800, 200400211200, 267200237600, 334000264000])

#Print Counts
c1= sub1['co2emissionsGroup'].value_counts(sort=False, dropna= True)
print("####Count for CO2EMISSIONS- Total amount of CO2 emission in metric tons since 1751.####")
print(c1)
#Prints Percentage
print('####Percentage for CO2EMISSIONS :####')
p1= sub1['co2emissionsGroup'].value_counts(sort=False, normalize= True)
print(p1)

#Minimum and maximum values
lifeexpectancyMin=data['lifeexpectancy'].min()
print('Minimum value for LifeEcpectancy :')
print(lifeexpectancyMin)
lifeexpectancyMax=data['lifeexpectancy'].max()
print('Maximum value for LifeEcpectancy :')
print(lifeexpectancyMax)

sub2=data[(data['lifeexpectancy']>=lifeexpectancyMin) & (data['lifeexpectancy']<=lifeexpectancyMax) ]

#Break the data into class intervals
sub2['lifeexpectancyGroup'] = pandas.cut(sub2.urbanrate, [0, 20, 40, 60, 80, 100])

#Print Counts
c2= sub2['lifeexpectancyGroup'].value_counts(sort=False, dropna= True)
print('####Count for lifeexpectancy- The average number of years a newborn child would live if current mortality patterns were to stay the same.####')
print(c2)

#Prints Percentage
p2= sub2['lifeexpectancyGroup'].value_counts(sort=False, dropna= True, normalize = True)
print('####Percentage for lifeexpectancy####')
print(p2)

#Minimum and maximum values
print('Minimum value for UrbanRate :')
urbanRateMin=data['urbanrate'].min()
print(urbanRateMin)
print('Maximum value for UrbanRate :')
urbanRateMax=data['urbanrate'].max()
print(urbanRateMax)

sub3=data[(data['urbanrate']>=urbanRateMin) & (data['urbanrate']<=urbanRateMax)]

#Break the data into class intervals
sub3['urbanrateGroup'] = pandas.cut(sub3.urbanrate, [0, 20, 40, 60, 80, 100])

#Print Counts
c3= sub3['urbanrateGroup'].value_counts(sort=False, dropna= True)
print('####Count for urbanrate- Percentage of total people living in urban areas :####')
print(c3)

#Prints Percentage
p3= sub3['urbanrateGroup'].value_counts(sort=False, dropna= True, normalize = True)
print('####Percentage for urbanrate####')
print(p3)

#*ct1= data.groupby(“urbanrate”).size() #using groupby
#*print(ct1)  #using groupby 