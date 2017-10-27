import  math
from  fractions import  Fraction


print  math.log(0.5,2)
print "--->"

num = -0.5*math.log(0.5, 2)- 0.5*math.log(0.5, 2)
print  num

print "--->"
print Fraction(2,3)

if Fraction(1,3) == 1/3:
    print  "asdfasdf"
else:
    print("----nbo--")

# tmp1 = -0.667*math.log((2/3),2)-Fraction(1, 3)*math.log((1/3),2)

tmp1 = -0.667*math.log(0.667,2)-0.333*math.log(0.333,2)

print  tmp1

tmp2 = math.log(Fraction(1,3),2) #OK
print  tmp2

tmp3 = math.log((1/3.0), 2)#
print  tmp3

last = -2.0/3*math.log(2.0/3, 2) - 1.0/3*math.log(1/3.0,2)
print ('last = '+str(last))


print  0.75*last

tmp4 = -1.0/2*math.log(1.0/2, 2)
print "---> "
print  tmp4

tmp5 = -3.0/4*math.log(3.0/4, 2)
print   tmp5


tmp6 = -1.0/4*math.log(1.0/4,2)
print  tmp6

tmp7 = -1.0/2*math.log(1.0/2, 2)
print tmp7

tmp8 = -1.0*math.log(1.0, 2)
print  tmp8

print  ('--->>>>')

print  -1