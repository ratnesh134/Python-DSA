class LassoRegression:
    def __init__(self, learning_rate=0.01, epochs=1000, alpha=0.1):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.alpha = alpha
        self.coef_ = None
        self.intercept_ = None

    def fit(self, X, y):
        X = np.array(X)
        y = np.array(y).reshape(-1, 1)  # Ensure y is a column vector
        self.m, self.n = X.shape

        # Initialize weights and bias
        self.coef_ = np.zeros((self.n, 1))
        self.intercept_ = 0

        # Gradient descent
        for _ in range(self.epochs):
            y_pred = X @ self.coef_ + self.intercept_
            error = y_pred - y

            # Gradient of loss + L1 regularization
            d_coef = (X.T @ error) / self.m + self.alpha * np.sign(self.coef_)
            d_intercept = np.sum(error) / self.m

            # Update
            self.coef_ -= self.learning_rate * d_coef
            self.intercept_ -= self.learning_rate * d_intercept

    def predict(self, X):
        X = np.array(X)
        return (X @ self.coef_ + self.intercept_).flatten()

