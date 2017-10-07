import  matplotlib.pyplot as plt
import  numpy as np

data =  [0,1,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,5,5,6,7,8,9,10,11,12,13,14];
a,b = np.histogram(data,bins=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
print a
print b
print  'mean = '+ str(np.mean(data)) #5.2
print  'median ='+ str(np.median(data)) #3.5
print  "mode = 3"
print  'mode < median < mean'
plt.hist(data,bins=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
plt.show()