import numpy as np

w = np.zeros(1)
b1 = 0 
iterations = 100 
x = np.array([1,2,3,4])
y = np.array([3,5,7,9])
N = len(x)

for i in range(iterations):
    y_pred = x*w + b1
    dw = -(2/N)*sum(x*(y - y_pred))
    db = -(2/N)*sum(y - y_pred)
    w = w - 0.1*dw
    b1 = b1 - 0.1*db

print(w, b1)
