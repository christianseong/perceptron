# -*- coding: utf-8 -*-
import numpy as np

class Perceptron(object):
    def __init__(self, eta=0.01, n_iter=10):
        self.eta= eta
        self.n_iter=n_iter
        
    def fit(self, X, y):
        self.w_ = np.zeros(1+X.shape[1],object) #object를 매개변수로 추가해 주어야 한다
        self.errors_=[]
        
        
        for _ in range(self.n_iter):
            errors=0
            for xi, target in zip(X,y):
                update = self.eta * (target-self.predict(xi))
                self.w_[1:]+=update*xi
                self.w_[0]+=update
               
                
                errors+= np.int32(update!=0.0)
                print(errors)
                print(self.w_)
            self.errors_.append(errors)
            
            
        return self
        
    def net_input(self, X):
         
         return np.dot(X, self.w_[1:])+ self.w_[0]
        
    def predict(self ,X):
         
         return np.where(self.net_input(X)>=0.0 ,1,-1)
        
        
        
   
        
        
def main():    
    p= Perceptron()
    arr1= np.array([[1,1],[4,1]],object)
    arr2= np.array([[1,1],[3,1]],object)
    p.fit(arr1,arr2)
    
    
    
if __name__ == "__main__":
    main()



   



                    
      
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                