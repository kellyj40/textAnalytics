__author__ = 'user'
# http://pythonprogramming.net/support-vector-machine-svm-example-tutorial-scikit-learn-python/

import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()

classifier = svm.SVC(gamma=0.1, C=100)
print(digits.data[0])
print("The label of this data is: " + str(digits.target[0]))
print(digits.images[0])
x, y = digits.data[:-1], digits.target[:-1]
classifier.fit(x, y)

print('Prediction:', classifier.predict([digits.data[-1]]))

plt.imshow(digits.images[-2], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()