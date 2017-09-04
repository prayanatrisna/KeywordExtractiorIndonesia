# -*- coding: utf-8 -*-
"""
Chunker + Selector dengan Pola NN NN
"""
skenario = 32
from operator import itemgetter
def chunk(text,pattern,n_pattern):
    candidate = []
    pattern = pattern.split()
    n = len(pattern)
    for sub in text:
        end = len(sub) + 1 - n
        #print sub
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

#from operator import itemgetter
import os
folder = "D:\Documents\Skripsi\Koding\Data\\testing\\"
os.chdir(folder)
n = len([name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))])

for i in range(n):
    fol_num = str(i+1)
    os.chdir(fol_num)
    fo = open("tagged_abstrak.txt","r+")
    abstrak = fo.read()
    fo.close()
    
    abstrak = abstrak.replace('\n','')
    abstrak = abstrak.split(' ./. ')[:-1] #sentence tokenize
    for i in abstrak:
        ind = abstrak.index(i)
        abstrak[ind]= i.split() #word tokenize
        for j in abstrak[ind]:
            ine = abstrak[ind].index(j)
            if abstrak[ind][ine] == '//GM':
                abstrak[ind][ine] = ('/','GM')
            else:
                temp = tuple(j.split('/'))
                abstrak[ind][ine] = tuple((temp[0].lower(),temp[1]))
            
    kandidat = chunk(abstrak,'NN NN',149)# + chunk(abstrak,'NN NN NN',20)
    kandidat = sorted(kandidat, reverse = True)
    
    fo = open('generated_kandidat_NN.txt','w+')
    fo.write('\n'.join([str(i[0]) +","+ str(i[1]) +","+ str(i[2]) for i in kandidat]))
    fo.close()
    
    n_kandidat = 5
    kandidat = sorted(kandidat, reverse = True, key = itemgetter(0))
    if len(kandidat) <= n_kandidat:
        kandidat_upper = kandidat
    else:
        kandidat_upper = kandidat[:n_kandidat]
        while kandidat[n_kandidat][0] > 1 and kandidat[n_kandidat][0] == kandidat[n_kandidat-1][0] and kandidat[n_kandidat][1] == kandidat[n_kandidat-1][1]:
            kandidat_upper.append(kandidat[n_kandidat])
            n_kandidat = n_kandidat + 1
    fo = open('generated_katakunci('+str(skenario)+').txt','w+')
    fo.write(', '.join([i[2] for i in kandidat_upper]))
    fo.close()
    
    os.chdir('..')
    print fol_num