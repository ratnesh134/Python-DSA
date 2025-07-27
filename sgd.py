class SGDRegressor:

    def __init__(self,learning_rate=0.1,epochs=100):
        self.coef_ = None
        self.intercept_ = None
        self.lr = learning_rate
        self.epochs = epochs

    def fit(self,X_train,y_train):
        # Here we will initialize our coefficients
        self.intercept_ = 0
        self.coef_ = np.ones(X_train.shape[1])

        for i in range(self.epochs):
            for j in range(X_train.shape[0]):

                # Generating the random number between 0 to total number of rows
                idx = np.random.randint(0,X_train.shape[0])  
                
                # Prediction for that particular index
                y_hat = np.dot(X_train[idx],self.coef_) + self.intercept_

                # Calculating the intercept derivative
                intercept_der = -2 * (y_train[idx] - y_hat)

                # Updating the intercept
                self.intercept_ = self.intercept_ - (self.lr * intercept_der)

                # Updating the coefficient derivative
                coeff_der = -2 * np.dot((y_train[idx] - y_hat),X_train[idx])
                
                # Updating the coefficients
                self.coef_ = self.coef_ - (self.lr * coeff_der)
                               
        print(self.intercept_)
        print(self.coef_)

    def predict(self,X_test):

        # Prediction
        return np.dot(X_test,self.coef_) + self.intercept_

    
        

