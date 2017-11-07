import  numpy as np

tmp = [0.470745584727, 0.438719080061, 0.279802995752, 0.34581676321, 0.387184471739, 0.326809925762, 0.342704953856, 0.386393862904, 0.415457115933, 0.410775342343]
minimum_price =  np.min(tmp)
maximum_price = np.max(tmp)  #None
mean_price = np.mean(tmp)  #None
median_price = np.median(tmp) # None
std_price = np.std(tmp) #None

print  'min = '+ str(minimum_price)
print  'max = '+ str(maximum_price)
print  'mean = '+str(mean_price)
print  'median = '+str(median_price)
print   'std = '+str(std_price)
