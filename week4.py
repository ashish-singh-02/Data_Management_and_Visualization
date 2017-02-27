#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 22:48:10 2017

@author: ashish
"""

import pandas
import numpy
import seaborn
import matplotlib.pyplot as plt

#Load the data from CSV file
data = pandas.read_csv('GapMinder_mine.csv', low_memory=False)

data = data.apply(lambda x: x.str.strip()).replace('', numpy.nan)

#To ensure data is in numeric format
data['co2emissions'] = data['co2emissions'].convert_objects(convert_numeric=True)
data['lifeexpectancy'] = data['lifeexpectancy'].convert_objects(convert_numeric=True)
data['urbanrate'] = data['urbanrate'].convert_objects(convert_numeric=True)

print('Minimum value for CO2Emissions :')
CO2Min=data['co2emissions'].min()
print(CO2Min)
print('Maximum value for CO2Emissions :')
CO2Max=data['co2emissions'].max()
print(CO2Max)

sub1=data[(data['co2emissions']>=CO2Min) & (data['co2emissions']<=CO2Max) ]
seaborn.distplot(sub1['co2emissions'].dropna(), kde=False);
plt.xlabel('co2emissions -Total amount of CO2 emission in metric tons:')
plt.title('co2emissions as per the GapMinder Study')

#Break the data into class intervals
sub1['co2emissionsGroup'] = pandas.cut(sub1.co2emissions, [132000.0, 66800158400, 133600184800, 200400211200, 267200237600, 334000264000])
#Print Counts
c1= sub1['co2emissionsGroup'].value_counts(sort=False, dropna= True)
print('####Count for CO2EMISSIONS- Total amount of CO2 emission in metric tons since 1751.####')
print(c1)

lifeexpectancyMin=data['lifeexpectancy'].min()
lifeexpectancyMax=data['lifeexpectancy'].max()
sub2=data[(data['lifeexpectancy']>=lifeexpectancyMin) & (data['lifeexpectancy']<=lifeexpectancyMax) ]
seaborn.distplot(sub1['lifeexpectancy'].dropna(), kde=False);
plt.xlabel('lifeexpectancy -The average number of years a newborn child would live:')
plt.title('lifeexpectancy as per the GapMinder Study')

print('Minimum value for UrbanRate :')
urbanRateMin=data['urbanrate'].min()
print(urbanRateMin)
print('Maximum value for UrbanRate :')
urbanRateMax=data['urbanrate'].max()
print(urbanRateMax)

sub3=data[(data['urbanrate']>=urbanRateMin) & (data['urbanrate']<=urbanRateMax)]
seaborn.distplot(sub1['urbanrate'].dropna(), kde=False);
plt.xlabel('urbanrate :Percentage of total people living in urban areas')
plt.title('urbanrate  in the NESARC Study')

scat1 = seaborn.regplot(x='urbanrate', y='lifeexpectancy', fit_reg=True, data=data)
plt.xlabel('Urban Rate')
plt.ylabel('Life Expectancy Rate')
plt.title('Scatterplot for the Association Between Urban Rate and Life Expectancy')
