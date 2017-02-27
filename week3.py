#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 22:31:12 2017

@author: ashish
"""

import pandas
import numpy

#load csv file
data = pandas.read_csv('GapMinder_mine.csv', low_memory=False)
#Replace all blank spaces in file with NAN
data = data.apply(lambda x: x.str.strip()).replace('', numpy.nan)

#To ensure data is in numeric format
data['co2emissions'] = data['co2emissions'].convert_objects(convert_numeric=True)
data['lifeexpectancy'] = data['lifeexpectancy'].convert_objects(convert_numeric=True)
data['urbanrate'] = data['urbanrate'].convert_objects(convert_numeric=True)

#function to find class interval of W=UrbanRate and LifeExpectancy
def create_New_Varable_For_Urban_Or_Life(urbanORlife):
   if (urbanORlife >0) & (urbanORlife <=20):
       return 1
   elif(urbanORlife >20) & (urbanORlife <=40):
       return 2    
   elif(urbanORlife >40) & (urbanORlife <=60):
       return 3        
   elif(urbanORlife >60) & (urbanORlife <=80):
       return 4
   elif(urbanORlife >80) & (urbanORlife <=100):
       return 5
#Function to find class interval of CO2Emissions
def create_New_Varable_For_CO2Emissions(C02):
   if (C02 >132000.0) & (C02 <=66800158400):
       return 1
   elif(C02 >66800158400) & (C02 <=133600184800):
       return 2    
   elif(C02 >133600184800) & (C02 <=200400211200):
       return 3        
   elif(C02 >200400211200) & (C02 <=267200237600):
       return 4
   elif(C02 >267200237600) & (C02 <=334000264000):
       return 5

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

subUrban = data['urbanrate']
#Calls the function created to find class interval
subUrban['Urbanrate_new']= subUrban.apply(create_New_Varable_For_Urban_Or_Life)
Urbanrate_new = subUrban['Urbanrate_new'].value_counts(sort=False, dropna= False)
print('####Count for urbanrate_New- New variable :####')
print(Urbanrate_new)
print('####Percentage for urbanrate_New- New variable :####')
Urbanrate_new1 = subUrban['Urbanrate_new'].value_counts(sort=False, dropna= False, normalize =True)
print(Urbanrate_new1)

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
subLife = data['lifeexpectancy']
#Calls the function created to find class interval
subLife['Lifeexpectancy_new']= subLife.apply(create_New_Varable_For_Urban_Or_Life)
Lifeexpectancy_new = subLife['Lifeexpectancy_new'].value_counts(sort=False, dropna= False)
print('####Count for lifeexpectancy_New- New variable created.####')
print(Lifeexpectancy_new)
print('####Percentge for lifeexpectancy_New- New variable created.####')
Lifeexpectancy_new1 = subLife['Lifeexpectancy_new'].value_counts(sort=False, dropna= False, normalize= True)
print(Lifeexpectancy_new1)

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
print('####Count for CO2EMISSIONS- Total amount of CO2 emission in metric tons since 1751.####')
print(c1)
subCO2 = data['co2emissions']
#Calls the function created to find class interval
subCO2['CO2emissions_new']= subCO2.apply(create_New_Varable_For_CO2Emissions)
CO2emissions_new = subCO2['CO2emissions_new'].value_counts(sort=False, dropna= False)
print('####Count for CO2emissions_new- New variable created .####')
print(CO2emissions_new)
print('####Percentage for CO2emissions_new- New variable created .####')
CO2emissions_new1 = subCO2['CO2emissions_new'].value_counts(sort=False, dropna= False, normalize=True)
print(CO2emissions_new1)