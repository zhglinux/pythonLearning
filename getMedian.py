# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import  sys


def get_median(data):
    data.sort()
    # print  data
    half = len(data)//2 # //	取整除 - 返回商的整数部分	9//2 输出结果 4 , 9.0//2.0 输出结果 4.0
    # print data[half]
    # print data[~half]
    return (data[half] + data[~half]) / 2


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


