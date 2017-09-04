# -*- coding: utf-8 -*-
"""
Preporcess All
"""
import re
import os
folder = "D:\Documents\Skripsi\Koding\Data\\data_all\\"
n = len([name for name in os.listdir(folder) 
    if os.path.isdir(os.path.join(folder, name))])
os.chdir(folder)

for i in range(n):
    fol_num = str(i+1)
    os.chdir(fol_num) 
    
    #baca simbol
    fo = open('D:\Documents\Skripsi\Koding\Data\symbol.txt','r+')
    symbol = fo.read()
    fo.close()

    #symbol in list
    symbol = symbol.split("\n")

    #baca abstrak
    fo = open('pre_abstrak.txt','r+')
    abstrak = fo.read()
    fo.close()
    
    #preprocess abstrak
    abstrak = abstrak.decode('UTF-8')
    abstrak = re.sub(r'[^\x00-\x7f]',r' ',abstrak)
    abstrak = abstrak.encode()
    abstrak = abstrak.replace("\n"," ")
    for i in symbol:
        abstrak = abstrak.replace(i," " + i + " ")          #memberi spasi utk tnd baca
        abstrak = re.sub(' +',' ', abstrak)                 #whitespace berlebih
        abstrak = abstrak.strip()                           #begining dan trailing whitespace

    #tulis abstrak
    fo = open('clear_abstrak.txt','w+')
    fo.write(abstrak)
    fo.close()
     
    #baca katakunci
    fo = open('pre_katakunci.txt','r+')
    katakunci = fo.read()
    fo.close()

    #preprocess katakunci
    katakunci = katakunci.decode('UTF-8')
    katakunci = re.sub(r'[^\x00-\x7f]',r' ',katakunci)
    katakunci = katakunci.encode()
    katakunci = katakunci.lower()                           #lower text
    katakunci = katakunci.replace("\n"," ")
    katakunci = katakunci.replace('.','')
    katakunci = katakunci.replace(',','.')
    katakunci = katakunci.replace('. dan','.')
    for i in symbol:
        katakunci = katakunci.replace(i," " + i + " ")      #memberi spasi utk tanda baca
        katakunci = re.sub(' +',' ', katakunci)             #whitespace berlebih
        katakunci = katakunci.strip()
    
    #tulis kunci
    fo = open('clear_katakunci.txt','w+')
    fo.write(katakunci)
    fo.close()
    
    #baca badanteks
    fo = open('pre_badanteks.txt','r+')
    badanteks = fo.read()
    fo.close()
    
    #preprocess badanteks
    badanteks = badanteks.decode('UTF-8')
    badanteks = re.sub(r'[^\x00-\x7f]',r' ',badanteks)
    badanteks = badanteks.encode()
    badanteks = badanteks.replace("\n"," ")
    for i in symbol:
        badanteks = badanteks.replace(i," " + i + " ")      #memberi spasi utk tanda baca
        badanteks = re.sub(' +',' ', badanteks)             #whitespace berlebih
        badanteks = badanteks.strip()

    #tulis badanteks
    fo = open('clear_badanteks.txt','w+')
    fo.write(badanteks)
    fo.close()
    
    os.chdir('..')
    print "Preprocessing document "+fol_num+" done!"