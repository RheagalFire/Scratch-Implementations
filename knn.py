from collections import Counter
import numpy as np

def euclidian_distance(x,y):
    return sum((y-x)**2)**0.5
euclidian_distance(np.array([1,1]),np.array([2,2]))

def KNN(test_point,x,y,k=3):
    distances = np.array([euclidian_distance(test_point,i) for i in x])
    indexs = distances.argsort()[:k]
    retrived = y[indexs]
    return Counter(retrived).most_common()[0][0]
