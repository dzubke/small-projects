# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 12:03:17 2015

@author: Dustin

This function will create a data set a perform a linear fit of the data.
"""


import pandas as pd
import matplotlib as plt
import math


data = pd.DataFrame([0,1.4,2.4,3,4.4,7], index=[list(range(6))])


def leastSqFit(y,x):
    '''This funciton takes two lists, y and x, as input and returns a list of
    with the first element as the y-intercept and the second element as the
    slope of the least squares fit of y'''
    
    
    beta  =  0.0    #the slope of the least squares linear fit
    alpha = 0.0     #the y-intercept of the least squares linear fit
    x_bar = sum(x)/len(x)     #the mean of the x list
    y_bar = sum(y)/len(y)     #the mean of the y list
    x1    = []      #contains a list of values x - x_bar
    y1    = []      #contains a list of values y - y_bar
    xy1   = []      #contains a list of value (x1*y1)
    sqx1  = []      #contains a list of x1**2
    rlist = []      #a list that contains alpha and beta
    
    
    for i in range(len(x)):
        x1.append(x[i]-x_bar)
        
    for i in range(len(y)):
        y1.append(y[i]-y_bar)
    
    for i in range(len(y1)):
        xy1.append(x1[i]*y1[i])
    
    for i in range(len(x1)):
        sqx1.append(x1[i]**2)
    
    beta = sum(xy1)/sum(sqx1)
    
    alpha = y_bar - beta*x_bar
    
    rlist=[alpha, beta]
    
    return rlist
    
    
    

def Variance(l):
    '''this function takes a lis l , an int mean, and int N as input and
    computes the variance of the list from the mean.'''
     
    N = len(l)  # the length of the data set
    mean = sum(l)/len(l)        # the mean of the data set
    sd = []     #list ofsquared difference between the list and the mean
    stddev = 0.0    #the standard deviation    
    var  = 0.0    #their variance
    i  = 0      #index for while loop
    

    sd = list(map(lambda x: (x-mean)**2,l))
    
    stddev=math.sqrt(sum(sd)/N)
    
    var= sum(sd)/N
    
    #print('N=', N)    
    #print('mean=', mean) 
    #print('lm=', lm)  
    #print('l=', l) 
    #print('sd=', sd)
    #print('sum sd=', sum(sd)) 
    
    return var
    


if __name__=="__main__":
     
     
    ab=leastSqFit(data[0],data.index)
    x=list(range(6))
    y_hat = []
    
    
    for i in range(len(x)):
        y_hat.append(ab[0] + ab[1]*x[i])
        
    df_yhat = pd.DataFrame(y_hat, index=x)
    
    ax=df_yhat.plot(color='r')    
    data.plot(ax=ax)
