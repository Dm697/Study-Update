#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print 'Number of People in the Enron dataset: {0}'.format(len(enron_data)),'\n'
print 'Number of Features for Each Person in the Enron dataset: {0}'.format(len(enron_data.values()[0])),'\n'
pois = [x for x, y in enron_data.items() if y['poi']]
print 'Number of POI\'s: {0}'.format(len(pois)), '\n\nThe name of POIS'
x = 0
while x < len(pois) :
    print pois[x]
    x = x + 1
enron_data['PRENTICE JAMES']['total_stock_value']
names = ['SKILLING JEFFREY K', 'FASTOW ANDREW S', 'LAY KENNETH L']
names_payments = {name:enron_data[name]['total_payments'] for name in names}
print '\nThe man took the most money:\n',sorted(names_payments.items(), key = lambda x: x[1], reverse =True)[0]

import pandas as pd

df = pd.DataFrame(enron_data)
print '\nHas salary data: {0}' .format(sum(df.loc['salary',:]!='NaN'))
print 'The percentage is ', sum(df.loc['salary',:]!='NaN')/(1.0*len(enron_data))

