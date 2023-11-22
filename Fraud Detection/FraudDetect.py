import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

# Load the dataset
file_path = 'path_to_your_dataset.csv'  # Replace with your file path
data = pd.read_csv(file_path)

# Convert 'transaction_time' to datetime and extract features
data['transaction_time'] = pd.to_datetime(data['transaction_time'])
data['hour'] = data['transaction_time'].dt.hour
data['day_of_week'] = data['transaction_time'].dt.dayofweek

# Select columns for one-hot encoding and standardization
categorical_features = ['card_type', 'location', 'purchase_category']
numerical_features = ['amount', 'customer_age', 'hour', 'day_of_week']

# Define the ColumnTransformer to transform the features
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(), categorical_features)
    ])

# Apply the transformations
processed_data = preprocessor.fit_transform(data)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    processed_data, data['is_fraudulent'], test_size=0.2, random_state=42)

# Initialize and train the Random Forest Classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)

# Predict and evaluate the model
y_pred = rf_classifier.predict(X_test)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

# Output the results
print("Confusion Matrix:\n", conf_matrix)
print("\nClassification Report:\n", class_report)
