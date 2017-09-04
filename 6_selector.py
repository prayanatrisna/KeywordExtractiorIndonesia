# -*- coding: utf-8 -*-
"""
Selector semua pola
"""
import os
import math
folder = "D:\Documents\Skripsi\Koding\Data\\testing\\"
os.chdir(folder)
n = len([name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))])
list_skenario = range(2,46) 

for skenario in list_skenario:
    print skenario # 2 - 12
    for i in range(n):
        n_kandidat = 5
        min_freq = 1
        fol_num = str(i+1)
        os.chdir(fol_num)
        if 2 <= skenario <= 12:
            fo = open("generated_kandidat.txt",'r+')
        elif 13 <= skenario <= 23:
            fo = open("generated_kandidat23.txt",'r+')
        elif 24 <= skenario <= 34:
            fo = open("generated_kandidat_badan.txt",'r+')
        elif 35 <= skenario <= 45:
            fo = open("generated_kandidat23_badan.txt",'r+')
        kandidat = fo.read()
        fo.close()
        
        kandidat = kandidat.split('\n')
        kandidat = [i.split(',') for i in kandidat]
        kandidat = [[int(i[0]),int(i[1]),i[2]] for i in kandidat]
        
        #semua
        if skenario == 2 or skenario == 13 or skenario == 24 or skenario == 35:
            kandidat_upper = kandidat
        
        #5 teratas, frekuensi
        elif skenario == 3 or skenario == 14 or skenario == 25 or skenario == 36: 
            kandidat = sorted(kandidat, reverse = True, key = lambda x:x[0])
            kandidat_upper = []
            index_upper = 0
            while(n_kandidat != 0 and index_upper != len(kandidat)):
                if kandidat[index_upper][0] > min_freq:
                    kandidat_upper.append(kandidat[index_upper])
                    n_kandidat = n_kandidat - 1
                index_upper = index_upper + 1
            while(index_upper != len(kandidat) \
            and kandidat_upper[-1][0] == kandidat[index_upper][0]): #cari kesamaan nilai
                kandidat_upper.append(kandidat[index_upper])
                index_upper = index_upper + 1
        
        #5 teratas, bobot dan frekuensi
        elif 4 <= skenario <= 7 or 15 <= skenario <= 18 \
        or 26 <= skenario <= 29 or 37 <= skenario <= 40:
            if skenario == 4 or skenario == 15 or skenario == 26 or skenario == 37: #bobot normal
                kandidat = sorted(kandidat, reverse = True, key = lambda x: x[0]*x[1])
            elif skenario == 5 or skenario == 16 or skenario == 27 or skenario == 38: #bobot log 10
                kandidat = [[i[0],1 + math.log(i[1],10),i[2]] for i in kandidat]
                kandidat = sorted(kandidat, reverse = True, key = lambda x: x[0]*x[1])
            elif skenario == 6 or skenario == 17 or skenario == 28 or skenario == 39: #bobot log 2
                kandidat = [[i[0],1 + math.log(i[1],2),i[2]] for i in kandidat]
                kandidat = sorted(kandidat, reverse = True, key = lambda x: x[0]*x[1])
            elif skenario == 7 or skenario == 18 or skenario == 29 or skenario == 40: #bobot augmented 0.5
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
            and kandidat_upper[-1][1] == kandidat[index_upper][1]): #cari kesamaan nilai
                kandidat_upper.append(kandidat[index_upper])
                index_upper = index_upper + 1
        
        #5 teratas, frekuensi, reduksi
        elif skenario == 8 or skenario == 19 or skenario == 30 or skenario == 41: 
            kandidat = sorted(kandidat, reverse = True, key = lambda x: (x[0],len(x[2].split())))
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
            and kandidat_upper[-1][0] == kandidat[index_upper][0]): #cari kesamaan nilai
                if not any(kandidat[index_upper][2] in i[2] for i in kandidat_upper):
                    if not any(i[2] in kandidat[index_upper][2] for i in kandidat_upper):
                        kandidat_upper.append(kandidat[index_upper])
                index_upper = index_upper + 1
        
        #5 teratas, reduksi frekuensi dan bobot, frekuensi > 1
        elif 9 <= skenario <= 12 or 20 <= skenario <= 23 \
        or 31 <= skenario <= 34 or 42 <= skenario <= 45:
            if skenario == 9 or skenario == 20 or skenario == 31 or skenario == 42: #bobot normal
                kandidat = sorted(kandidat, reverse = True, key = lambda x: (x[0]*x[1],len(x[2].split())))
            elif skenario == 10 or skenario == 21 or skenario == 32 or skenario == 43: #bobot log 10
                kandidat = [[i[0],1 + math.log(i[1],10),i[2]] for i in kandidat]
                kandidat = sorted(kandidat, reverse = True, key = lambda x: (x[0]*x[1],len(x[2].split())))
            elif skenario == 11 or skenario == 22 or skenario == 33 or skenario == 44: #bobot log 2
                kandidat = [[i[0],1 + math.log(i[1],2),i[2]] for i in kandidat]
                kandidat = sorted(kandidat, reverse = True, key = lambda x: (x[0]*x[1],len(x[2].split())))
            elif skenario == 12 or skenario == 23 or skenario == 34 or skenario == 45: #bobot augmented 0.5
                max_bobot = max(kandidat,key=lambda x:x[1])[1]
                kandidat = [[i[0],0.5 + (0.5*i[1])/max_bobot,i[2]] for i in kandidat]
                kandidat = sorted(kandidat, reverse = True, key = lambda x: (x[0]*x[1],len(x[2].split())))
        
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
        if 2 <= skenario <= 45:
            fo = open('generated_katakunci('+str(skenario)+').txt','w+')
            fo.write(', '.join([i[2] for i in kandidat_upper]))
            fo.close()
    
        os.chdir("..")
#        print fol_num