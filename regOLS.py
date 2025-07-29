class RidgeRegression:

    def __init__(self,alpha=0.1):
        self.alpha = alpha
        self.m = None
        self.b = None

    def fit(self,X_train,y_train):

        X_train = np.insert(X_train,0,1,axis=1)  # Inserting 1s at 0th index for intercept

        I = np.identity(X_train.shape[1])  # Forming the identity matrix 

        I[0][0] = 0      # In scikit-learn class for some reason element at 0,0 position is 0, it should be 1 in general

        result = np.linalg.inv(np.dot(X_train.T,X_train) + self.alpha * I).dot(X_train.T).dot(y_train)

        self.intercept_ = result[0]
        self.coef_ = result[1:]

    def predict(self,X_test):

        return np.dot(X_test,self.coef_) + self.intercept_

