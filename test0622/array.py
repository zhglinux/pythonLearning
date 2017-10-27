

from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import tree
from sklearn import preprocessing
from sklearn.externals.six import StringIO

# Read in the csv file and put features into list of dict and list of class label
allElectronicsData = open(r'/home/zhoumiao/MachineLearning/01decisiontree/AllElectronics.csv', 'rb')
reader = csv.reader(allElectronicsData)
headers = reader.next()


ab = ["asdfaf",123,23,"2323"]

adb = ["asdfaf",123,23,"2323"]


print(ab)

print(adb)
