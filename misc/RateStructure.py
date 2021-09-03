# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 20:22:49 2015

@author: Dustin

This program calculates the total cost of electricity for a given rate
structure and load curve.

Necessary input: Date, Time, tariff schedule versus time, energy usage, power
usage, 

"""
import pandas as pd


def rateCalc(usage):
    '''the function that a 2-columned (excluding index) dataframe as input and
    returns the numerical charge to the customer'''
    
    '''The rate structure will charge $0.10/kWh and $0.50/kW for the first 
    two hours and then $0.20/kWh and $1.00/kW for the second two hours'''
    
    
    charge = 0.0 # final charge to the customer
    
    for i in list(usage.index):
        if i <2:
            #print()
            charge+=0.1*usage.loc[i,'NRG']
            charge+=0.5*usage.loc[i,'PWR']
        else:
            charge+=0.2*usage.loc[i,'NRG']
            charge+=1*usage.loc[i,'PWR']
    
    print(charge)
    return charge







if __name__=="__main__":
    
    usage=pd.DataFrame({'NRG':[1,2,3,1], 'PWR':[5,6,7,8]},index=[0,1,2,3])
    
    rateCalc(usage)
    