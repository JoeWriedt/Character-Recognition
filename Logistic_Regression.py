import numpy as np

def sigmoid(x):
     return 1/(1+np.exp(-x))

class LogisticRegression():
     
     def __init__(self, iters=100, step=0.01):
          self.iters = iters
          self.step = step
          self.weigths = np.zeros(785)
          self.bias = 0

     def fit(self, X, y):

          for _ in range(self.iters):
               linear_pred = np.dot(X, self.weigths) + self.bias
               predictions = sigmoid(linear_pred)

               dw = (1/60000)*np.dot(X.T, (predictions-y))
               db = (1/60000)*np.sum(predictions-y)

               self.weights = self.weigths - self.step*dw
               self.bias = self.bias - self.step*db


     def predict(self, X):
          linear_pred = np.dot(X, self.weigths) + self.bias
          y_pred = sigmoid(linear_pred)
          class_pred = [0 if y < 0.5 else 1 for y in y_pred]
          return class_pred

def accuracy(y_pred, y_test):
     count = 0
     for i in range(len(y_test)):
          if y_pred[i] == y_test[i]:
               count += 1
     
     return count/len(y_test)



