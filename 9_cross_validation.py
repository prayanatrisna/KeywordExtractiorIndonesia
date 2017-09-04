# -*- coding: utf-8 -*-
"""
Distribusi data ke training dan testing
"""
import os
import shutil

folder = "D:\Documents\Skripsi\Koding\Data\\data_all"
os.chdir(folder)
group = 30
data = range(1,151)
data_group = [data[group*i:group*(i+1)] for i in range(len(data)/group)]

for fold in data_group:
    num = str(data_group.index(fold) + 1)
    ind_testing = fold
    ind_training = list(set(data) - set(fold))
    counter = 1
    print "Fold " + num
    print "Fold " + num + ': Working on splitting.'
    for i in ind_testing:
        fol_num = str(i)
        shutil.copytree(fol_num, "..\\testing\\"+ str(counter))
        counter = counter + 1
    
    counter = 1 
    for i in ind_training:
        fol_num = str(i)
        shutil.copytree(fol_num, "..\\training\\"+str(counter))
        counter = counter + 1
    print "Fold " + num + ': Splitting done!'
        
    os.system('python D:\Documents\Skripsi\Koding\Code\\4_pembobotan_training.py')
    print "Fold " + num + ': Pattern done!'
    
    print "Fold " + num + ': Working on Chuking.'
    os.system('python D:\Documents\Skripsi\Koding\Code\\5_chunker_all_badan.py')
    os.system('python D:\Documents\Skripsi\Koding\Code\\5_chunker_all.py')
    os.system('python D:\Documents\Skripsi\Koding\Code\\5_chunker_23_badan.py')
    os.system('python D:\Documents\Skripsi\Koding\Code\\5_chunker_23.py')
    print "Fold " + num + ': Chunking done!'    
    
    print "Fold " + num + ': Working on selection.'
    os.system('python D:\Documents\Skripsi\Koding\Code\\6_selector.py')
#    os.system('python D:\Documents\Skripsi\Koding\Code\\6_selector_all_badan.py')
#    os.system('python D:\Documents\Skripsi\Koding\Code\\6_selector_all.py')
#    os.system('python D:\Documents\Skripsi\Koding\Code\\6_selector_23_badan.py')
#    os.system('python D:\Documents\Skripsi\Koding\Code\\6_selector_23.py')
    print "Fold " + num + ': Selection done!'
    
    print "Fold " + num + ': Working on testing.'
    os.system('python D:\Documents\Skripsi\Koding\Code\\7_tester.py')
    print "Fold " + num + ': Testing done!'            
    
    if not os.path.exists('D:\Documents\Skripsi\Koding\Data\\result\\'):
        os.makedirs('D:\Documents\Skripsi\Koding\Data\\result\\')
    for i in range(group):
        fol_num = i+1
        while os.path.exists('D:\Documents\Skripsi\Koding\Data\\result\\'+str(fol_num)):
            fol_num = fol_num + group
        fol_num = str(fol_num)
        src = 'D:\Documents\Skripsi\Koding\Data\\testing\\'+str(i+1)
        dest = 'D:\Documents\Skripsi\Koding\Data\\result\\'+fol_num
        shutil.copytree(src,dest)
        
    not_deleted = [i for i in os.listdir("D:\Documents\Skripsi\Koding\Data\\") if 'nilaiakhir' in i] + ['data_all','rekap.csv','symbol.txt', 'result']
    shutil.copyfile("D:\Documents\Skripsi\Koding\Data\\bobot.csv","D:\Documents\Skripsi\Koding\Data\\result\\bobot("+num+").csv")    
    for i in os.listdir("D:\Documents\Skripsi\Koding\Data"):
        if i not in not_deleted:
            if os.path.isfile("D:\Documents\Skripsi\Koding\Data\\"+i):
                os.remove("D:\Documents\Skripsi\Koding\Data\\"+i)
            elif os.path.isdir("D:\Documents\Skripsi\Koding\Data\\"+i):
                shutil.rmtree("D:\Documents\Skripsi\Koding\Data\\"+i)
    print "Fold " + num +" done!"
print "All fold done!\nWorking on TextRank"
#os.system('python D:\Documents\Skripsi\Koding\Code\\3_textrank_selector.py')
#print "TextRank done!\nWorking on resumer"
#os.system('python D:\Documents\Skripsi\Koding\Code\\8_resumer.py')
#print "Resuming done!"    