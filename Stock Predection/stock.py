import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'path_to_your_dataset.csv'  # Replace with the path to your dataset
data = pd.read_csv(file_path)

# Convert the 'Date' column to datetime and set as index
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

# Feature Engineering
data['1d_lag_close'] = data['Close'].shift(1)
data['7d_MA_close'] = data['Close'].rolling(window=7).mean()
data.dropna(inplace=True)

# Splitting the Data
split_ratio = 0.8
split_index = int(len(data) * split_ratio)
train = data[:split_index]
test = data[split_index:]

X_train = train.drop('Close', axis=1)
y_train = train['Close']
X_test = test.drop('Close', axis=1)
y_test = test['Close']

# Building and Training the Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
print("Root Mean Squared Error:", rmse)

# Visualizing Predictions
plt.figure(figsize=(10, 6))
plt.plot(test.index, y_test, label='Actual')
plt.plot(test.index, predictions, label='Predicted')
plt.title('Google Stock Price Prediction')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
