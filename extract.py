# -*- coding: utf-8 -*-
"""
Created on Mon Sep 04 10:57:16 2017

@author: I Nyoman P. Trisna
"""

import sys
import re
import os

def chunk(text,pattern,n_pattern):
    candidate = []
    pattern = pattern.split()
    n = len(pattern)
    for sub in text:
        end = len(sub) + 1 - n
        for ind, (a,b) in enumerate(sub):
            if(len(sub)<n): #berhenti kalau panjang kalimat < panjang pola
                break
            if ind == end:
                break
            x = True
            for num, i in enumerate(pattern):
                if i != sub[ind+num][1]:
                    x = False
            if x:
                s = ""
                for i in range(n):
                    s = s + sub[ind+i][0]
                    if i != len(pattern)-1:
                        s = s + " "
                candidate.append(s)
    candidate = [(candidate.count(i),n_pattern,i) for i in set(candidate)]
    return candidate
#%% Argument
input_ = sys.argv[1]
output_ = sys.argv[2]
limit = int(sys.argv[3])
min_freq = int(sys.argv[4])

fo = open(input_,'r+')
input_text = fo.read()
fo.close()

fo = open('symbol.txt','r+')
symbol = fo.read()
fo.close()
symbol = symbol.split("\n")

#%%Preprocess
input_text = input_text.decode('UTF-8')
input_text = re.sub(r'[^\x00-\x7f]',r' ',input_text)
input_text = input_text.encode()
input_text = input_text.replace("\n"," ")
for i in symbol:
    input_text = input_text.replace(i," " + i + " ")
    input_text = re.sub(' +',' ', input_text)
    input_text = input_text.strip()
    
fo = open('preprocessed.txt',"w+")
fo.write(input_text)
fo.close()
print "Preprocessed"
#%%POS Tag using IPOSTagger v1.1
os.chdir("IPOSTAgger_v1.1")
command = "java ipostagger ..\\preprocessed.txt"  
command = command + " 1 1 0 1 > ..\\tagged.txt"
os.system(command)
os.chdir("..")
print "POS Tagged"
#%% Read pattern from training
fo = open('weight.csv')
pattern = fo.read()
fo.close()
pattern = pattern.split('\n')[1:]
pattern = [i.split(',') for i in pattern]
pattern = [[i[0], int(i[1]), int(i[2])] for i in pattern]

#%%Chunking
fo = open("tagged.txt","r+")
tagged = fo.read()
fo.close()
tagged = tagged.replace('\n','')
tagged = tagged.split(' ./. ')[:-1] #sentence tokenize
for i in tagged:
    ind = tagged.index(i)
    tagged[ind]= i.split() #word tokenize
    for j in tagged[ind]:
        ine = tagged[ind].index(j)
        if tagged[ind][ine] == '//GM':
            tagged[ind][ine] = ('/','GM')
        else:
            temp = tuple(j.split('/'))
            tagged[ind][ine] = tuple((temp[0].lower(),temp[1]))  
candidate = []
for i in pattern:
    candidate = candidate + chunk(tagged,i[0],i[1])
print "Chunked"
#%% Selection
candidate = sorted(candidate, reverse = True, key = lambda x: (x[0]*x[1],len(x[2])))
selected_candidate = []
index_upper = 0
while(limit != 0 and index_upper != len(candidate)):
    if not any(candidate[index_upper][2] in i[2] for i in selected_candidate):
        if not any(i[2] in candidate[index_upper][2] for i in selected_candidate):
            if candidate[index_upper][0] > min_freq:
                selected_candidate.append(candidate[index_upper])
                limit = limit - 1
    index_upper = index_upper + 1

while(index_upper != len(candidate) \
and selected_candidate[-1][0] == candidate[index_upper][0] \
and selected_candidate[-1][1] == candidate[index_upper][1]): #cari duplikasi
    if not any(candidate[index_upper][2] in i[2] for i in selected_candidate):
        if not any(i[2] in candidate[index_upper][2] for i in selected_candidate):
            selected_candidate.append(candidate[index_upper])
    index_upper = index_upper + 1
print "Selected"
#%% Result writing
keywords = ', '.join([i[2] for i in selected_candidate])
fo = open(output_,'w+')
fo.write(keywords)
fo.close()
print "Keywords: "+ keywords