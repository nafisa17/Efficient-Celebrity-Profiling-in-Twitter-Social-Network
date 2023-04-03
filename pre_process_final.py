# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 16:43:13 2020

@author: HP
"""
import re
import string
import pandas as pd
from nltk.tokenize import word_tokenize
from gensim.parsing.preprocessing import remove_stopwords

df= pd.read_csv(r'C:\Users\HP\Desktop\Pre_Process_all_tweet\Test\pol\AshokParnamiBJP_pol.csv')
df3=df.iloc[:,2]
#print(df3)
filteredword=[]
text=df3.values.tolist()
l=len(text)
strs = ['']*l
for w in range(len(text)):
    t=str(text[w])
    t = t.lower()
    #removes mentions and replace with USER_MENTION
    filteredword=re.sub('@[^\s]+',' ',t)
    #removes haashtags 
    filteredword=re.sub(r'#([^\s]+)', r'\1',filteredword)
    #removes url
    filteredword=re.sub('((www\.[^\s]+)|(https?://[^\s]+))','', filteredword)
    #emoji remove
    filteredword= re.sub('(:\s?\)|:-\)|\(\s?:|\(-:|:\'\))', ' ', filteredword)
    filteredword= re.sub('(:\s?D|:-D|x-?D|X-?D)', '  ', filteredword)
    filteredword= re.sub('(<3|:\*)', '  ', filteredword)
    filteredword= re.sub('(;-?\)|;-?D|\(-?;)', ' ', filteredword)
    filteredword= re.sub('(:\s?\(|:-\(|\)\s?:|\)-:)', '  ', filteredword)
    filteredword= re.sub('(:,\(|:\'\(|:"\()', ' ', filteredword)
    #retweet remove
    filteredword=re.sub(r'\brt\b', '',filteredword)
    filteredword = re.sub(r'\.{2,}', ' ', filteredword)
    # Strip space, " and ' from filteredword
    filteredword = filteredword.strip(' "\'')
    filteredword = re.sub(r'\s+', ' ', filteredword)
    filteredword = re.sub('([^A-Za-z0-9]+)', ' ', filteredword)
    filteredword = re.sub("\d+", "",filteredword) 
    rt=remove_stopwords(filteredword)
    strs[w]=rt 
    tokens = word_tokenize(rt)
    words = [word for word in tokens if word.isalpha()]
    sent="".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in words]).strip()
    text[w]=sent
    text[w]=filteredword
    
#print(text)    
dataedited = pd.DataFrame(text)
dataedited.to_csv('AshokParnamiBJP_pol.csv')  
    
    
    