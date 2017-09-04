# -*- coding: utf-8 -*-
"""
Benchmark dengan TextRank bigram
"""
import networkx as nx
import os

def filter_for_tags(tagged, tags=['NN', 'JJ', 'NNP','FW','VBI']):
    return [item for item in tagged if item[1] in tags]

skenario = 1
folder = "D:\Documents\Skripsi\Koding\Data\\result\\"
os.chdir(folder)
n = len([name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))])

fo = open('D:\Documents\Skripsi\Koding\Data\\nilaiakhir('+str(skenario)+').csv','a')
fo.write('Nomor,Precision,Recall,F-measure\n')
fo.close()
   
for i in range(n):
    fol_num = str(i+1)
    os.chdir(fol_num)
    fo = open("tagged_abstrak.txt","r+")
    abstrak = fo.read()
    fo.close()
    
    #ubah jadi tuple
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
    kandidat = []
    for i in abstrak:
        kandidat.append(filter_for_tags(i))
    kandidat = list(set([j for i in kandidat for j in i])) #merge list in list
    kandidat = [i[0] for i in kandidat]
    
    fo = open("clear_abstrak.txt","r+")
    abstrak = fo.read()
    fo.close()
    
    grlist = []
    for i in range(len(kandidat)):
        for j in range(i,len(kandidat)):
            grlist.append([kandidat[i],kandidat[j],
                           abstrak.count(kandidat[i]+" "+kandidat[j])+
                           abstrak.count(kandidat[j]+" "+kandidat[i])])
    grlist = sorted(grlist, key = lambda x : x[2], reverse = True)
    
    gr = nx.Graph()
    for i in grlist:
        gr.add_node(i[0])
        gr.add_node(i[1])
        gr.add_edge(i[0],i[1],weight=i[2])
    rank = nx.pagerank(gr)
    kandidat = sorted(rank, key = rank.get, reverse = True)
    kandidat = kandidat[0:gr.number_of_nodes()/3 + 1] #1/3 dari total vertex
    
    kandidat_fix = set([])
    dealtWith = set([])
    i = 0
    j = 1
    while j < len(abstrak.split()):
        pertama = abstrak.split()[i]
        kedua = abstrak.split()[j]
        if pertama in kandidat and kedua in kandidat:
            keyphrase = pertama + ' ' + kedua
            kandidat_fix.add(keyphrase)
            dealtWith.add(pertama)
            dealtWith.add(kedua)
        else:
            if pertama in kandidat and pertama not in dealtWith:
                kandidat_fix.add(pertama)
            if j == len(abstrak.split()) - 1 and kedua in kandidat and \
                    kedua not in dealtWith:
                kandidat_fix.add(kedua)
    
        i = i + 1
        j = j + 1
        
    fo = open('generated_katakunci('+str(skenario)+').txt','w+')
    fo.write(', '.join(kandidat_fix))
    fo.close()
    
    #TESTING
    fo = open(folder + fol_num + '\\clear_katakunci.txt','r+')
    bawaan = fo.read()
    fo.close()
    
    hasil = kandidat_fix
    
    bawaan = bawaan.split(' . ')
    match = list(set.intersection(hasil,set(bawaan)))
    precision_total = 0
    recall_total = 0
    f_total = 0
    precision = float(len(match))/float(len(hasil))
    recall = float(len(match))/float(len(bawaan))
    f = 0.0
    if precision != 0.0 or recall != 0.0:
        f = 2*precision*recall/(precision+recall)
    precision_total = precision_total + precision
    recall_total = recall_total + recall
    f_total = f_total + f
            
    fo = open(folder + fol_num +'\\hasilakhir('+str(skenario)+').txt','w+')
    fo.write('Bawaan:\n' + ', '.join(bawaan) + '\n\n'+ 'Hasil:\n' + ', '.join(hasil) + '\n\n')
    fo.write('Precision: '+str(precision) + '\nRecall: ' + str(recall) + '\nF-measure: ' + str(f))
    fo.close()  
          
    fo = open('D:\Documents\Skripsi\Koding\Data\\nilaiakhir('+str(skenario)+').csv','a')
    fo.write(fol_num+','+str(precision) + ',' + str(recall) + ',' + str(f) + '\n')
    fo.close()   
    
    os.chdir('..')
    print fol_num