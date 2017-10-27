# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import  csv
import  random
import  math
import  operator

def loadDataSet(filename,split, trainingSet=[], testSet=[]):
    with open(filename,'rb') as csvfile:
        lines = csv.reader(csvfile)
        print(lines)
        dataset = list(lines)
        print(dataset)
        for x in range(len(dataset)-1):
            for y in range(4):
                dataset[x][y] = float (dataset[x][y])
                if random.random() <split:
                    trainingSet.append(dataset[x])
                else:
                    testSet.append(dataset[x])



def euclideanDistance(instance1, instance2, length):
    distance = 0
