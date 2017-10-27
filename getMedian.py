# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import  sys
import  numpy as np



def get_median(data):
    data.sort()
    # print  data
    half = len(data)//2 # //	取整除 - 返回商的整数部分	9//2 输出结果 4 , 9.0//2.0 输出结果 4.0
    # print data[half]
    # print data[~half]
    return (data[half] + data[~half]) / 2

l0 = [1,2,2,2,2,3,3,3,3,3,3,3,3,3,4,4,4,5,5,6,7,8,9,10,11,12,13];

print  get_median(l0)
print  np.mean(l0)
print  np.median(l0)
arr = np.array(l0)
print  np.bincount(arr)



l1 = [58350, 63120, 44640, 56380, 72250];
l2 = [48670, 57320, 38150, 41290, 53160,500000];

av1 = sum(l1)/len(l1)
print av1
print sum(l2)/len(l2)

print get_median(l1)
print get_median(l2)


l1.sort()
print l1

l4 = sorted(l2)
print l4

print "hello world"

print '=--------1------->'

l100 = [33219, 36254, 38801,46335,46840,47596,55130,56863,78070,88830]
av100 = np.mean(l100)
print  av100

print '=---------2------>'
l101 = []
for num in l100:
    l101.append(num-av100)
    print  num-av100

print '=-------3-------->'
avl101 = np.mean(l101)
print  avl101

okl101 = []
for num in  l101:
    if num < 0:
        okl101.append(-num)
    else:
        okl101.append(num)

print okl101
print '=-------4-------->'
print np.mean(okl101)
print '=-------5-------->'

sql103 = []
for num  in  l101:
    sql103.append(np.square(num))
    print  np.square(num)

print  np.mean(sql103)

nor103 = np.mean(sql103)

print  np.sqrt(nor103)

snd1 = [38946,43420,49191,50430,50557,52580,53595,54135,60181,62076]

def get_standard_deviation(data):
    ave = np.mean(data)
    da2 = []
    for num in data:
        tmp =np.square(num - ave)
        da2.append(tmp)

    ave2 = np.mean(da2)

    sqr = np.sqrt(ave2)

    return  sqr

print  get_standard_deviation(snd1)

snd2 = [18,21,18,20,23,15,17,22,21]
print  get_standard_deviation(snd2)




