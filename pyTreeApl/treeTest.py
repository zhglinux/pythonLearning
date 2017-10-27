# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from graphviz import Digraph
from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import preprocessing
from sklearn import tree
from sklearn.externals.six import StringIO
import  itertools


a = ["asdfasdf", 123,"123"]
print(a)
e = ["asdf","thishi"]
b ={"ada","asdfaasdf","af","ad12","123asdf"}
a = ["123","123"]
print(a)
b= [1,2,3,4]

# with open(r'/selfrobot/DeepLearning_data/AllElectronics.csv', 'rt') as realldata:
#     data = csv.reader(realldata)
#     for l in  data:
#         print(l)
#     realldata.seek(0)
#     for l in  data:
#         print(l)


# allElectronicsData = open(r'/selfrobot/DeepLearning_data/AllElectronics.csv', 'rt')
# reader = csv.reader(allElectronicsData)
#
# headers = next(reader)
# print(headers)
#
# t1Reader, t2Reader = itertools.tee(reader)
#
# for row in t1Reader:
#     print(row)
#
# for row in t2Reader:
#     print(row)

allElectronicsData = open(r'/selfrobot/DeepLearning_data/AllElectronics.csv', 'rt')
reader = csv.reader(allElectronicsData)

headers = next(reader)
print(headers)

tmpReader = list(reader)

# for row in reader:
#     print(row)
#
# for row in tmpReader:
#     print(row)
#
# for row in tmpReader:
#     print(row)

featureList = []
labelList = []

for arow in  tmpReader:
    print(arow, arow[len(arow)-1])
    labelList.append(arow[len(arow)-1])
    rowdict = {}
    for i in  range(1, len(arow)-1):
        rowdict[headers[i]] = arow[i]
    featureList.append(rowdict)

print(featureList)

vec = DictVectorizer()
dummyX1 = vec.fit_transform(featureList)
dummyX = dummyX1.toarray()

print("dummyX: "+str(dummyX))
print(vec.get_feature_names())

print("labelList:"+str(labelList))

lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labelList)
print("dummyY:"+str(dummyY))


clf = tree.DecisionTreeClassifier(criterion="entropy")
clf = clf.fit(dummyX,dummyY)
print("clf:"+str(clf))


with open("/selfrobot/DeepLearning_data/AllElectronicData.dot","w") as file:
    file = tree.export_graphviz(clf, feature_names=vec.get_feature_names(),out_file=file)





