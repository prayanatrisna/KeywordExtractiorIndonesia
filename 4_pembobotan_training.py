# -*- coding: utf-8 -*-
"""
Perhitungan Frekuensi Pola Frase Training
"""
import re
import os
folder = "D:\Documents\Skripsi\Koding\Data\\training\\"
n = len([name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))])
tag_all = []
os.chdir(folder)
for i in range(n):
    fol_num = str(i+1)
    os.chdir(fol_num)
    tag = open('tagged_katakunci.txt', 'r+').read()     #membaca txt
    tag = re.sub('\n+',' ', tag)                        #mengganti newline dengan space
    tag = re.sub(' +',' ', tag)                         #menghilangkan whitespace berlebih
    tag = re.sub(r'[^\s]+/','',tag)                     #menghilangkan kata non POS tag
    tag = tag.strip()                                   #menghilangkan leading dan trailing whitespace
    tag = tag.split(' . ')                              #strip menjadi list dengan delimiter ' . '
    tag_all = tag_all + tag
    
    os.chdir('..')
    
#distinct counting
tagcount = [(j,tag_all.count(j),str(len(j.split()))) for j in set(tag_all)]
tagcount = sorted(tagcount, key = lambda x:(x[1],x[2]), reverse = True)

os.chdir('..')
fo = open("bobot.csv","w+")
fo.write("Pola,Jumlah,N Frase\n")
for k in tagcount:
    fo.write(str(k[0]) + ",")
    fo.write(str(k[1]) + ",")
    fo.write(str(k[2]))
    if tagcount.index(k) != len(tagcount) - 1:
        fo.write("\n")
fo.close()