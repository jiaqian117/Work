#encoding=utf-8
import os
import codecs
import glob
import pandas as pd

os.getcwd()

def txtcombine():
	
	files=glob.glob('*txt')

	all=codecs.open('all.txt','a')
	
	for filename in files:
		print(filename)
		fopen=codecs.open(filename,'r',encoding='utf-8')
		lines=[]
		lines=fopen.readlines()
		fopen.close()
		i=0
		for line in lines:
			for x in line:
				all.write(x)
		all1=pd.read_csv('all.txt',sep=' ',encoding='GB2312')
		all1.to_csv('all.csv',encoding='GB2312')

if __name__=='__main__':
	txtcombine()
	
