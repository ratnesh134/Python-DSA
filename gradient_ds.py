class GDRegressor:

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
            # Update all the coefficient and the intercepts
            y_hat = np.dot(X_train,self.coef_) + self.intercept_
            intercept_der = -2 * np.mean(y_train - y_hat)
            self.intercept_ = self.intercept_ - (self.lr * intercept_der)

            coef_der = -2 * np.dot((y_train - y_hat), X_train)/X_train.shape[0]
            self.coef_ = self.coef_ - (self.lr * coef_der)
        print(self.intercept_)
        print(self.coef_)

    def predict(self,X_test):

        # Prediction
        return np.dot(X_test,self.coef_) + self.intercept_

