## -*- coding: utf-8 -*-
#"""
#Spyder Editor
#
#This is a temporary script file.
#"""
#
#x='+----+----+'
#y='|    |    |'
#
#def printGrid (line1,line2):
#    x=verticles(line2)
#    print(line1+"\n"+x+"\n"+line1+"\n"+x+"\n"+line1)
#
#def verticles (line1):
#    x=(line1+"\n"+line1+"\n"+line1+"\n"+line1)
#    return x
#
#printGrid(x,y)
#
#o = 5
#a = 4
#
#import math
#def hypot (o,a):
#    h = math.sqrt(o+a)
#    return h
#
#h = hypot(o,a) 
#print(h)
#    
#
#def hailstones(i):
#    while i != 1:
#        if i%2 == 0:
#            i=i/2
#            print(i)
#        else:
#            i=3*i+1
#            print(i)
#
#hailstones(5)
#    

#def x(n):
#    for i in range(n):
#        print(i)
#        if i == n-1:
#            print(i+1)
#            
#x(5)

#def fileTypeChange(files):
#    newList = []
#    for i in files:
#        if i.endswith("txt"):
#            i = i.replace("txt","doc")
#        newList.append(i)
#    print(newList)
#        
#fileTypeChange(["a.doc","b.txt","c.doc"])

#def histogram(items):
#    h={}
#    for i in items:
#        if i in h:
#            h[i] +=1
#        else:
#            h[i]=1
#    print(h)
#    
#histogram([17, 18, 17, 20, 15, 25, 25, 19, 18, 19, 23, 20, 22, 22, 21])

#import numpy as np
#
##x = np.array(range(10))
##x += 100
##print(x.std())
#
#print(np.linspace(0,2,9))


#import numpy as np
#
#X = [[1.0, 2.0], [3.0, 4.0]]
#X = np.array(X)
#
#print(X[1,0])
#            
#np.savetxt("lect1.txt",X)

#import pandas as pd
#pd.read_csv("C:\\Users\\Ian\\Desktop\\irish_cities.txt", sep="\t", skiprows=1)
    
import sqlite3
import pandas as pd

conn = sqlite3.connect("C:\\Users\\Ian\\Documents\\BA\\Analytics Research & Implementation\\SQL\\ian.db") 
df = pd.read_sql_query("SELECT * FROM student;",conn)
print(df)
df.to_excel("ian_db.xls")
df.to_csv("ian_db.csv")

 
    
    
    
            
            
            
            
            
            
            
            
            
            
            
            
    
   
    
    
