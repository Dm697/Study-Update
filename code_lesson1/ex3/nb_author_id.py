#!/usr/bin/python

""" 
 	Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
   
import sys
from time import time
from email_preprocess import preprocess
from sklearn.naive_bayes import GaussianNB 

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
clf = GaussianNB()
t0 = time()
clf.fit(features_train,labels_train)
prep = clf.predict(features_test)
print "training time:",round(time()-t0,3), "s" 
accuracy = clf.score(features_train, labels_train)
print "accuracy: ",accuracy
print(sum(clf.predict(features_test)))


#########################################################
