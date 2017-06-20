#!usr/bin/env python

import csv
import pandas as pd

csv = pd.read_csv('test.csv')

# prawdopodobienstwa klas
classes = csv.ix[:,0].tolist()
classes_values = list(set(classes))
dict_for_classes = {}
length = len(classes)
classes_values_sum = []

for i in range(len(classes_values)):
	x = classes_values[i]
	classes_values_sum.append(classes.count(classes_values[i]))
	y = classes_values_sum[i] / float(length)
	dict_for_classes[i] = [x,y]
	
df = pd.Series(dict_for_classes)
#print(df)


names = list(csv.columns.values)
#print(names)
#probabilities = pd.DataFrame(columns = names[1:])
probabilities  = pd.DataFrame()
#print(probabilities)

#prawdopodobienstwa cech
for i in range(1,len(csv.columns)): #iteracja po roznych cechach - kolumnach dataframe
	col = csv.ix[:,i].tolist()
	col_values = list(set(col)) 
	dat = pd.DataFrame(col_values)
	dat.columns = [names[i]]
#	print(dat)
	col_values_sum = []
	dataframe = pd.concat([probabilities,dat],axis=1)
	probabilities = dataframe
	dat_1 = pd.DataFrame()
	for a in range(len(col_values)): #obliczenie ile jest wystapien danej wartosci cechy i jej prawdopodobienstwa warunkowego 
		col_values_sum.append(col.count(col_values[a]))
#		print(col_values[a],col_values_sum[a])
		cond_prob_class = []
		for j in range(len(classes_values)): #iteracja po wartosciach klas, pod ktorch warunkiem mamy zliczac wystapienia
			counter = 0
			cond_prob = 0
			for b in range(len(col)): #iteracja po wierszach kolumny
				if classes[b] == classes_values[j] and col[b] == col_values[a]:
					counter = counter + 1
			if col_values_sum[a] != 0:
				cond_prob = counter / float(classes_values_sum[j])		
#			print(col_values[a],cond_prob)
			cond_prob_class.append(cond_prob)
#		print(cond_prob_class)
		dat_pom = pd.DataFrame([cond_prob_class])
		dat_pom.columns = classes_values
		pom = pd.concat([dat_1,dat_pom],ignore_index = True,axis = 0)
		dat_1 = pom
	dataframe = pd.concat([probabilities,dat_1], axis = 1)
	probabilities = dataframe
#probabilities.columns = names[1:]
print(probabilities)	


