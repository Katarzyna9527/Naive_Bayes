#!usr/bin/env python

import csv
import pandas as pd
import random

data = pd.read_csv('donory.csv')

cross_validation  = pd.DataFrame()
names = list(data.columns.values)
cross_validation = pd.DataFrame(columns = names)

lenght  = len(data.index)
for i in range(lenght):
	rand = random.randint(0,len(data.index)-1)
	cross_validation.loc[i] = data.iloc[rand]
	data = data.drop([rand] , axis = 0).reset_index(drop=True)

cross_validation.to_csv('cross_validation.csv')
