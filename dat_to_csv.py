#!usr/bin/env python
'''Zapis danych z pliku dat do odpowiedniego formatu csv'''

import csv


'''Donory'''
file_w = open('donory.csv', 'w')
file_w.write('class')

for i in range(1,16):
	file_w.write(','+str(i))

file_r = open('spliceDTrainKIS.dat','r')
c = file_r.read(2) 

while True:
	c = file_r.read(1)
	if not c: break
	if c != "\n":
		if c == '0' or c == '1':
			file_w.write("\n"+c)
		else:
			file_w.write(','+c)
				
	
file_w.close()
file_r.close()


'''Akceptory'''
file_w = open('akceptory.csv', 'w')
file_w.write('class')

for i in range(1,91):
	file_w.write(','+str(i))

file_r = open('spliceATrainKIS.dat','r')
c = file_r.read(3) 

while True:
	c = file_r.read(1)
	if not c: break
	if c != "\n":
		if c == '0' or c == '1':
			file_w.write("\n"+c)
		else:
			file_w.write(','+c)
				
	
file_w.close()
file_r.close()
