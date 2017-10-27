# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import  math
from  sklearn import  neighbors
from  sklearn import  datasets



def calcEulideanDistance(x1,y1,x2,y2):
    d = math.sqrt(math.pow((x1-x2),2)+ math.pow((y1-y2),2))
    return  d


d_ag = calcEulideanDistance(3,104,18,90)
d_bg = calcEulideanDistance(2,100,18,90)
d_cg = calcEulideanDistance(1, 81,18,90)
d_dg = calcEulideanDistance(101,10,18,90)
d_eg = calcEulideanDistance(99,5,18,90)
d_fg = calcEulideanDistance(98,2,18,90)



print("d_ag : "+str(d_ag))
print("d_ag : "+str(d_bg))
print("d_ag : "+str(d_cg))
print("d_ag : "+str(d_dg))
print("d_ag : "+str(d_eg))
print("d_ag : "+str(d_fg))

print("this is test")
print("this is test")


knn = neighbors.KNeighborsClassifier()
iris = datasets.load_iris()

# print(iris)

knn.fit(iris.data,iris.target)

predictret = knn.predict([[0.1,0.2, 0.3,0.4],[0.8,0.9, 0.9,0.6]])
print(predictret)







