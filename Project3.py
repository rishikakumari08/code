
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the data
data = pd.read_csv('Advertising.csv')

# Extract the features and target variable
X = data[['TV', 'Radio', 'Newspaper']]
y = data['Sales']

# Create and fit the linear regression model
model = LinearRegression()
model.fit(X, y)

# Make predictions
y_pred = model.predict(X)

# Plot the actual and predicted sales
plt.figure(figsize=(8, 6))
plt.scatter(data['Sales'], y_pred)
plt.plot([min(data['Sales']), max(data['Sales'])], [min(y_pred), max(y_pred)], color='red')
plt.xlabel('Actual Sales')
plt.ylabel('Predicted Sales')
plt.title('Actual vs Predicted Sales')
plt.show()