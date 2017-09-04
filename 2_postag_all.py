# -*- coding: utf-8 -*-
"""
PoSTag Training: Katakunci
"""
def get_tag_from_text(kunci,acuan):
    tagged = []
    kunci = kunci.split()
    n = len(kunci)
    for sub in acuan:
        end = len(sub) + 1 - n
        for ind, (a,b) in enumerate(sub):
            if(len(sub)<n):                                         #berhenti kalau panjang kalimat pada acuan < panjang kata kunci
                break
            if ind == end:
                break
            x = True
            for num, i in enumerate(kunci):
                if i != sub[ind+num][0]:
                    x = False
            if x:
                s = ""
                for i in range(n):
                    s = s + sub[ind+i][0] + '/' + sub[ind+i][1]
                    if i != len(kunci)-1:
                        s = s + " "
                tagged.append(s)
    if tagged != []:
        tagged = max(tagged, key = tagged.count)                
        return tagged 
  
import os
import re
os.chdir("D:\Documents\Skripsi\Koding\IPOSTAgger_v1.1\\")
folder = "D:\Documents\Skripsi\Koding\Data\\data_all\\"
n = len([name for name in os.listdir(folder)
    if os.path.isdir(os.path.join(folder, name))])

for i in range(n): #ganti jumlah folder di
    folder_number = str(i+1)
    command = "java ipostagger " + folder + folder_number + "\\clear_abstrak.txt"
    command = command + " 1 1 0 1 > " + folder + folder_number + "\\tagged_abstrak.txt"
    os.system(command)
    
    command = "java ipostagger " + folder + folder_number + "\\clear_badanteks.txt"
    command = command + " 1 1 0 1 > " + folder + folder_number + "\\tagged_badanteks.txt"
    os.system(command)
    
    fo = open(folder+folder_number+"\\tagged_abstrak.txt",'r+')
    tagged_abstrak = fo.read()
    fo.close()
    fo = open(folder+folder_number+"\\tagged_badanteks.txt",'r+')
    tagged_badanteks = fo.read()
    fo.close()
    
    tagged_abstrak = re.split('\s\./\.\s|\s\?/\.\s|\s!/\.\s',tagged_abstrak)[:-1]           #sentence tokenize
    tagged_badanteks = re.split('\s\./\.\s|\s\?/\.\s|\s!/\.\s',tagged_badanteks)[:-1]       #sentence tokenize
    tagged_all = tagged_abstrak + tagged_badanteks
    for j in tagged_all:
        ind = tagged_all.index(j)
        tagged_all[ind]= j.split()                                                          #word tokenize
        for k in tagged_all[ind]:
            ine = tagged_all[ind].index(k)
            if tagged_all[ind][ine] == '//GM':
                tagged_all[ind][ine] = ('/','GM')
            else:
                temp = tuple(k.split('/'))
                tagged_all[ind][ine] = tuple((temp[0].lower(),temp[1]))
    
    fo = open(folder+folder_number+"\\clear_katakunci.txt",'r+')
    clear_katakunci = fo.read()
    fo.close()
    #clear_katakunci = clear_katakunci.lower()
    clear_katakunci = clear_katakunci.split(' . ')
    tagged = []    
    for j in clear_katakunci:
        if get_tag_from_text(j,tagged_all) != None:
            tagged.append(get_tag_from_text(j,tagged_all))
    
        
    fo = open(folder + folder_number + '\\tagged_katakunci.txt','w+')
    for j in tagged:
        fo.write(j)
        if j != tagged[-1]:
            fo.write(' ./.\n')
    fo.write('\n\n')
    fo.close()
    
#    command = "java ipostagger " + folder + folder_number + "\\clear_katakunci.txt"
#    command = command + " 1 1 0 1 > " + folder + folder_number + "\\tagged_katakunci2.txt"
#    os.system(command)
    print "Tagging document "+folder_number+" done!"