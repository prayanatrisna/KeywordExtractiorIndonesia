# -*- coding: utf-8 -*-
"""
Perhitungan Frekuensi Pola Frase Training
"""
import re
import os
folder = "data_train\\"
n = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]
tag_all = []
os.chdir(folder)
for i in n:
    fol_num = i
    os.chdir(fol_num)
    tag = open('tagged_keyword.txt', 'r+').read()
    tag = re.sub('\n+',' ', tag)
    tag = re.sub(' +',' ', tag)
    tag = re.sub(r'[^\s]+/','',tag)
    tag = tag.strip()
    tag = tag.split(' . ')
    tag_all = tag_all + tag
    
    os.chdir('..')
    
#distinct counting
tagcount = [(j,tag_all.count(j),str(len(j.split()))) for j in set(tag_all)]
tagcount = sorted(tagcount, key = lambda x:(x[1],x[2]), reverse = True)

os.chdir('..')
fo = open("weight.csv","w+")
fo.write("pattern,weight,number of words\n")
for k in tagcount:
    fo.write(str(k[0]) + ",")
    fo.write(str(k[1]) + ",")
    fo.write(str(k[2]))
    if tagcount.index(k) != len(tagcount) - 1:
        fo.write("\n")
fo.close()