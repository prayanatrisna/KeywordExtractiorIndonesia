# -*- coding: utf-8 -*-
"""
Rekapitulasi
"""
#import matplotlib.pyplot as plt
import os
folder = "D:\Documents\Skripsi\Koding\Data\\"
os.chdir(folder)
n = len([name for name in os.listdir(folder) if 'nilaiakhir' in name])
m = 0
fa = open('rekap.csv','w+')
fa.write('skenario,precision,recall,f measure')
hasil_akhir = []
for i in range(n):
    num = str(i+1+m)
    while not os.path.exists('nilaiakhir('+ num +').csv'):
        m = m + 1
        num = str(i+1+m)  
    fo = open('nilaiakhir('+ num +').csv','r+')
    hasil = fo.read()
    fo.close()
    
    counter = 1
    hasil = hasil.split('\n')
    header = hasil[0]
    hasil = hasil[1:-1]
    hasil = [i.split(',') for i in hasil]
    hasil = [[i+1,float(j[1]),float(j[2]),float(j[3])] for i,j in enumerate(hasil)]
    rekap = ['Avg',
            sum([i[1] for i in hasil])/len(hasil), 
            sum([i[2] for i in hasil])/len(hasil),
            sum([i[3] for i in hasil])/len(hasil)]
    fo = open('nilaiakhir('+ num +').csv','w+')
    fo.write(header)
    for j in hasil:
        fo.write('\n'+','.join(map(str,j)))
    fo.close()  
    fa.write('\n'+num+','+','.join(map(str,rekap[1:])))
fa.close()