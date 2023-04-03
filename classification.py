# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 23:41:39 2020

@author: HP
"""
import matplotlib.pyplot as plt
import pandas as pd
from nltk.tokenize import word_tokenize
#reads the data dictionary
df= pd.read_csv(r'C:\Users\HP\Desktop\Pre_Process_all_tweet\most frequent\data_dictionary.csv')
#testing tweet
test = pd.read_csv(r'C:\Users\HP\Desktop\Pre_Process_all_tweet\Test\AshokParnamiBJP_pol.csv')
bus=df.iloc[:,0]
edu=df.iloc[:,1]
entr=df.iloc[:,2]
pol=df.iloc[:,3]
spo=df.iloc[:,4]
tech=df.iloc[:,5]
test=test.iloc[:,1]
count={}
word_count=0
x=[0,1,2,3,4,5]
print("BUSINESS")
for i in range(39):
   
    word_bus=str(bus[i])
    c=0
    for j in range(len(test)):
        word2=str(test[j])
        tokens = word_tokenize(word2)
        for w in tokens:
            if(w==word_bus):
                c=c+1
    if(c>15):
      word_count=word_count+1  
      print(word_bus,c)
if(word_count>0):
    print("No of words Found: ", word_count)
    x[0]=word_count
word_count=0      
print("EDUCATION")   
for i in range(44):
    word_edu=str(edu[i])
    d=0
    for j in range(len(test)):
        word2=str(test[j])
        tokens = word_tokenize(word2)
        for w in tokens:
            if(w==word_edu):
                c=c+1
    if(d>15):
        word_count=word_count+1
        print(word_edu,d)
if(word_count>0):
    print("No of words Found: ", word_count)
    x[1]=word_count
word_count=0
print("ENTERTAINMENT")        
for i in range(84):
    word_entr=str(entr[i])
    c=0
    for j in range(len(test)):
        word2=str(test[j])
        tokens = word_tokenize(word2)
        for w in tokens:
            if(w==word_entr):
                c=c+1
    if(c>15):
        word_count=word_count+1
        print(word_entr,c) 
if(word_count>0):
    print("No of words Found: ", word_count)
    x[2]=word_count
word_count=0
print("POLITICS")        
for i in range(132):
    word_pol=str(pol[i])
    c=0
    for j in range(len(test)):
        word2=str(test[j])
        tokens = word_tokenize(word2)
        for w in tokens:
            if(w==word_pol):
                c=c+1
    if(c>15):
        word_count=word_count+1
        print(word_pol,c)
if(word_count>0):
    print("No of words Found: ", word_count)
    x[3]=word_count
word_count=0
print("SPORTS")        
for i in range(66):
    word_spo=str(spo[i])
    c=0
    for j in range(len(test)):
        word2=str(test[j])
        tokens = word_tokenize(word2)
        for w in tokens:
            if(w==word_spo):
                c=c+1
    if(c>15):
        word_count=word_count+1
        print(word_spo,c)        
if(word_count>0):
    print("No of words Found: ", word_count)
    x[4]=word_count
word_count=0        
print("TECHNOLOGY")
# try:
for i in range(158):
    word_tech=str(tech[i])
    c=0
    for j in range(len(test)):
        word2=str(test[j])
        tokens = word_tokenize(word2)
        for w in tokens:
            if(w==word_tech):
                c=c+1
                
    if(c>15):
        word_count=word_count+1
        print(word_tech,c) 
if(word_count>0):
    print("No of words Found: ", word_count)
    x[5]=word_count
      

labels = ['Business', 'Education', 'Entertainment', 'politics', 'Sports', 'technology']
plt.figure(figsize=(20,10))
fig, ax = plt.subplots()
width = 0.35
ax.bar(labels,x, width)


ax.set_ylabel('most used words')
ax.set_title('categories')
ax.legend()

plt.show()
