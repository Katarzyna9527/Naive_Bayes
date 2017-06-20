#!usr/bin/env python

import csv
import pandas as pd
from functools import reduce

from train_vs_func import *


def classify(example, atribute_prob, classes_prob, names):
	class_classification_prob = []
	for j in range(len(classes_prob)):		
		pom_prob_list = []
		for i in range(1,len(example.columns)): 
			if atribute_prob[names[i]].str.contains(example.ix[0,i]).any():
				row_id = int(atribute_prob.loc[atribute_prob[names[i]]==example.ix[0,i]].index.values)	
				c_prob = atribute_prob.ix[row_id,(i-1)*(len(classes_prob.index)+1)+j+1]
			else:
				c_prob = 0
			pom_prob_list.append(c_prob)
		#print(pom_prob_list)	
		class_classification_prob.append((reduce(lambda x,y: x*y, pom_prob_list))*classes_prob.ix[j,1])
	#print(class_classification_prob)
	class_idx = class_classification_prob.index(max(class_classification_prob))
	#print(class_idx)
	which_class = classes_prob.ix[class_idx,0]	
	return which_class 




donory = pd.read_csv('test.csv')
nam = list(donory.columns.values)
example = pd.DataFrame()
example = pd.DataFrame(columns = nam)

cross_validation = 10




probabilities, classes, names = train_bayes(donory)
example.loc[0] = donory.iloc[0]
example.ix[0,5] = 'M'
#print(example)
#print(probabilities)

c = classify(example, probabilities, classes, names)

#print(classes)
#
#z = int(example.loc[example[nam[9]]=='G'].index.values)
#print(z)

