# -*- coding: utf-8 -*-
"""
Tester berdasarkan precision recall
"""
import os
folder = "D:\Documents\Skripsi\Koding\Data\\testing\\"
n = len([name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))])
list_skenario = range(2,46)
for skenario in list_skenario:
    if not os.path.exists('D:\Documents\Skripsi\Koding\Data\\nilaiakhir('+str(skenario)+').csv'):
        fo = open('D:\Documents\Skripsi\Koding\Data\\nilaiakhir('+str(skenario)+').csv','w+')
        fo.write('Nomor,Precision,Recall,F-measure\n')
        fo.close()

    for i in range(n):
        folder_number = str(i+1)
        fo = open(folder + folder_number + '\\clear_katakunci.txt','r+')
        bawaan = fo.read()
        fo.close()
        
        fo = open(folder + folder_number + '\\generated_katakunci('+str(skenario)+').txt','r+')
        hasil = fo.read()
        fo.close()
        
        bawaan = bawaan.split(' . ')
        hasil = hasil.split(', ')
        match = list(set.intersection(set(hasil),set(bawaan)))
        
        precision = float(len(match))/float(len(hasil))
        recall = float(len(match))/float(len(bawaan))
        f = 0.0
        if precision != 0.0 or recall != 0.0:
            f = 2*precision*recall/(precision+recall)
                
        fo = open(folder + folder_number +'\\hasilakhir('+str(skenario)+').txt','w+')
        fo.write('Bawaan:\n' + ', '.join(bawaan) 
                + '\n\n'+ 'Hasil:\n' + ', '.join(hasil) + '\n\n')
        fo.write('Precision: '+str(precision) + '\nRecall: ' 
                + str(recall) + '\nF-measure: ' + str(f))
        fo.close()  
            
        os.chdir("..")    
        fo = open('D:\Documents\Skripsi\Koding\Data\\nilaiakhir('+str(skenario)+').csv','a')
        fo.write(folder_number+','+str(precision) + ',' + str(recall) + ',' + str(f) + '\n')
        fo.close()   
        print folder_number
         