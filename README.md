# Keyword Extraction Indonesia
Keyword Extraction for Indonesian Paper based on Phrase Chunking

Note:
* Run pyhton in the representative directory with command: python extract.py <input file> <output file> <number of average keywords> <number of minimum ocurence>. Example: python extract.py sample.txt keyword.txt 5 1
* This method use HMM based POS tag, from https://www.researchgate.net/publication/209387036_HMM_Based_Part-of-Speech_Tagger_for_Bahasa_Indonesia
* Data Training is gained from E-Journal of Accounting Universitas Udayana (https://ojs.unud.ac.id/index.php/Akuntansi). If you want to add more training, just save the data in directories with POS-tagged keyword. For training, simply put python train.py.
