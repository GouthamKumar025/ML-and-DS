import numpy as np

class LinearRegression:
    def __init__(self, lr_rate, n_iters):
        self.lr_rate = lr_rate
        self.n_iters = n_iters
        self.weight = None
        self.bias = None

    def fit(self, X, y):
        n_sample, n_features = X.shape

        self.weight = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iters):
            y_predicted = np.dot(X, self.weight) + self.bias

            # compute gradient descent

            dw = (1 / n_sample) * np.dot(X.T,(y_predicted - y))
            db = (1 / n_sample) * np.sum(y_predicted - y)

            # update parameters

            self.weight -= self.lr_rate * dw
            self.bias -= self.lr_rate * db

    def predict(self, X):
        y_approximated = np.dot(X, self.weight) + self.bias
        return y_approximated


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    from sklearn import datasets


    def mean_square_error(y_true, y_pred):
        return np.mean((y_true - y_pred) ** 2)


    def r2_score(y_true, y_pred):
        corr_matrix = np.corrcoef(y_true, y_pred)
        corr = corr_matrix[0, 1]
        return corr ** 2


    X, y = datasets.make_regression(
        n_samples=100, n_features=1, noise=20, random_state=4
    )
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

    regressor = LinearRegression(lr_rate=0.01, n_iters=1000)
    regressor.fit(X_train, y_train)
    predictions = regressor.predict(X_test)

    mse = mean_square_error(y_test, predictions)
    print("MSE: ", mse)

    accu = r2_score(y_test, predictions)
    print("Accuracy:", accu)

    y_pred_line = regressor.predict(X)
    cmap = plt.get_cmap("viridis")
    fig = plt.figure(figsize=(8, 6))
    m1 = plt.scatter(X_train, y_train, color=cmap(0.9), s=10)
    m2 = plt.scatter(X_test, y_test, color=cmap(0.5), s=10)
    plt.plot(X, y_pred_line, color="black", linewidth=2, label="Prediction")
    plt.show()
