import  matplotlib.pyplot as plt
import  numpy as np

data = [47,10,31,25,20,
        2,11,31,25,21,
        44,14,15,26,21,
        41,14,16,26,21,
        7,30,17,27,24,
        6,30,17,27,24,
        35,32,15,29,23,
        38,33,19,28,20,
        35,34,18,29,21,
        36,32,16,27,20]
a,b = np.histogram(data,bins=[0,5,10,15,20,25,30,35,40,45,50])
print a
print b
plt.hist(data,bins=[0,5,10,15,20,25,30,35,40,45,50])
plt.show()