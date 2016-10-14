##import numpy as np
##from math import sqrt
##import matplotlib.pyplot as plt
##import warnings
##from matplotlib import style
##from collections import Counter
##style.use('fivethirtyeight')
##dataset = {'k':[[1,2],[2,3],[3,1]], 'r':[[6,5],[7,7],[8,6]]}
##feature = [5,7]
##for i in dataset:
##    for ii in dataset[i]:
##        plt.scatter(ii[0], ii[1],s=100, color=i)
##plt.show()
        
"""K-Means Experiment"""
import warnings
from collections import Counter

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')
dataset = {'k':[[1,2],[2,3],[3,1]], 'r':[[6,5],[7,7],[8,6]]}
"""
To test the algorithm vary the coordinates of the test point.
The  algorithm prints its  prediction along  with some confidence value
e.g if the test feature is : feature = [5,6]
then the result is:

[('r', 3)]
Class r : Confidence 1
"""
feature = [5,6]
##[[plt.scatter(ii[0], ii[1],s=100, color=i) for  ii in dataset[i]] for i in dataset]
##plt.scatter(feature[0],feature[1], s=100, color='orange')
##plt.show()

def calculate_k_nearest_neighbors(data, predict, k=3):
    if len(data) >=k:
        warnings.warn('K is set to value less than total voting groups!')
    distances = []
    for group in data:
        for features in data[group]:
            #for understanding how to calc eucledian distance. 2D only example i.e suppports x and y only
            #euc_dist = sqrt((features[0]-predict[0])**2 + (features[1]-predict[1])**2)
            #More robust, supports any dimention
            euc_dist = np.linalg.norm(np.array(features)-np.array(predict))
            
            distances.append([euc_dist,group])
    votes = [i[1] for i in sorted(distances)[:k]]
    print(Counter(votes).most_common(1))
    vote_result = Counter(votes).most_common(1)[0][0]
    confidence = Counter(votes).most_common(1)[0][1]/k
    print("Class {vote_result} : Confidence {confidence}".format(vote_result=vote_result, confidence=confidence))
    return vote_result, confidence


            

result, confidence = calculate_k_nearest_neighbors(dataset, feature, k=3)


[[plt.scatter(ii[0], ii[1],s=100, color=i) for  ii in dataset[i]] for i in dataset]
plt.scatter(feature[0],feature[1], s=100, color=result)
plt.show()
        
