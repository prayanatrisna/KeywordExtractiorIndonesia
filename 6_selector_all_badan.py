# -*- coding: utf-8 -*-
"""
Selector semua pola
"""
import os
import math
folder = "D:\Documents\Skripsi\Koding\Data\\testing\\"
os.chdir(folder)
n = len([name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))])
list_skenario = range(24,35) #diganti dengan list

for skenario in list_skenario:
    print skenario # 24 - 34
    for i in range(n):
        n_kandidat = 5
        min_freq = 1
        fol_num = str(i+1)
        os.chdir(fol_num)
        fo = open("generated_kandidat_badan.txt",'r+')
        kandidat = fo.read()
        fo.close()
        
        kandidat = kandidat.split('\n')
        kandidat = [i.split(',') for i in kandidat]
        kandidat = [[int(i[0]),int(i[1]),i[2]] for i in kandidat]
        
        #semua
        if skenario == 24:
            kandidat_upper = kandidat
        
        #5 teratas, frekuensi
        elif skenario == 25: 
            kandidat = sorted(kandidat, reverse = True, key = lambda x:x[0])
            kandidat_upper = []
            index_upper = 0
            while(n_kandidat != 0 and index_upper != len(kandidat)):
                if kandidat[index_upper][0] > min_freq:
                    kandidat_upper.append(kandidat[index_upper])
                    n_kandidat = n_kandidat - 1
                index_upper = index_upper + 1
            while(index_upper != len(kandidat) \
            and kandidat_upper[-1][0] == kandidat[index_upper][0]): #cari duplikasi
                kandidat_upper.append(kandidat[index_upper])
                index_upper = index_upper + 1
        
        #5 teratas, bobot dan frekuensi
        elif 26 <= skenario <= 29:
            if skenario == 26: #frekuensi * bobot normal
                kandidat = sorted(kandidat, reverse = True, key = lambda x: x[0]*x[1])
            elif skenario == 27: #frekuensi * bobot normalisasi(log 10)
                kandidat = [[i[0],1 + math.log(i[1],10),i[2]] for i in kandidat]
                kandidat = sorted(kandidat, reverse = True, key = lambda x: x[0]*x[1])
            elif skenario == 28: #frekuensi * bobot normalisasi(log 2)
                kandidat = [[i[0],1 + math.log(i[1],2),i[2]] for i in kandidat]
                kandidat = sorted(kandidat, reverse = True, key = lambda x: x[0]*x[1])
            elif skenario == 29: #frekuensi * bobot normalisasi(augmented 0.5)
                max_bobot = max(kandidat,key=lambda x:x[1])[1]
                kandidat = [[i[0],0.5 + (0.5*i[1])/max_bobot,i[2]] for i in kandidat]
                kandidat = sorted(kandidat, reverse = True, key = lambda x: x[0]*x[1])
            
            kandidat_upper = []
            index_upper = 0
            while(n_kandidat != 0 and index_upper != len(kandidat)):
                if kandidat[index_upper][0] > min_freq:
                    kandidat_upper.append(kandidat[index_upper])
                    n_kandidat = n_kandidat - 1
                index_upper = index_upper + 1
            while(index_upper != len(kandidat) \
            and kandidat_upper[-1][0] == kandidat[index_upper][0] \
            and kandidat_upper[-1][1] == kandidat[index_upper][1]): #cari duplikasi
                kandidat_upper.append(kandidat[index_upper])
                index_upper = index_upper + 1
        
        #5 teratas, reduksi frekuensi, frekuensi > 1
        elif skenario == 30: 
            kandidat = sorted(kandidat, reverse = True, key = lambda x: (x[0],len(x[2])))
            kandidat_upper = []
            index_upper = 0
            while(n_kandidat != 0 and index_upper != len(kandidat)):
                if not any(kandidat[index_upper][2] in i[2] for i in kandidat_upper):
                    if not any(i[2] in kandidat[index_upper][2] for i in kandidat_upper):
                        if kandidat[index_upper][0] > min_freq:
                            kandidat_upper.append(kandidat[index_upper])
                            n_kandidat = n_kandidat - 1
                index_upper = index_upper + 1
            while(index_upper != len(kandidat) \
            and kandidat_upper[-1][0] == kandidat[index_upper][0]): #cari duplikasi
                if not any(kandidat[index_upper][2] in i[2] for i in kandidat_upper):
                    if not any(i[2] in kandidat[index_upper][2] for i in kandidat_upper):
                        kandidat_upper.append(kandidat[index_upper])
                index_upper = index_upper + 1
        
        #5 teratas, reduksi frekuensi dan bobot, frekuensi > 1
        elif 31 <= skenario <= 34:
            if skenario == 31: #frekuensi * bobot normal
                kandidat = sorted(kandidat, reverse = True, key = lambda x: (x[0]*x[1],len(x[2])))
            elif skenario == 32: #frekuensi * bobot normalisasi(log 10)
                kandidat = [[i[0],1 + math.log(i[1],10),i[2]] for i in kandidat]
                kandidat = sorted(kandidat, reverse = True, key = lambda x: (x[0]*x[1],len(x[2])))
            elif skenario == 33: #frekuensi * bobot normalisasi(log 2)
                kandidat = [[i[0],1 + math.log(i[1],2),i[2]] for i in kandidat]
                kandidat = sorted(kandidat, reverse = True, key = lambda x: (x[0]*x[1],len(x[2])))
            elif skenario == 34: #frekuensi * bobot normalisasi(augmented 0.5)
                max_bobot = max(kandidat,key=lambda x:x[1])[1]
                kandidat = [[i[0],0.5 + (0.5*i[1])/max_bobot,i[2]] for i in kandidat]
                kandidat = sorted(kandidat, reverse = True, key = lambda x: (x[0]*x[1],len(x[2])))
        
            kandidat_upper = []
            index_upper = 0
            while(n_kandidat != 0 and index_upper != len(kandidat)):
                if not any(kandidat[index_upper][2] in i[2] for i in kandidat_upper):
                    if not any(i[2] in kandidat[index_upper][2] for i in kandidat_upper):
                        if kandidat[index_upper][0] > min_freq:
                            kandidat_upper.append(kandidat[index_upper])
                            n_kandidat = n_kandidat - 1
                index_upper = index_upper + 1
            while(index_upper != len(kandidat) \
            and kandidat_upper[-1][0] == kandidat[index_upper][0] \
            and kandidat_upper[-1][1] == kandidat[index_upper][1]): #cari duplikasi
                if not any(kandidat[index_upper][2] in i[2] for i in kandidat_upper):
                    if not any(i[2] in kandidat[index_upper][2] for i in kandidat_upper):
                        kandidat_upper.append(kandidat[index_upper])
                index_upper = index_upper + 1
    
        #tulis hasil
        if 24 <= skenario <= 34:
            fo = open('generated_katakunci('+str(skenario)+').txt','w+')
            fo.write(', '.join([i[2] for i in kandidat_upper]))
            fo.close()
    
        os.chdir("..")
        print fol_num