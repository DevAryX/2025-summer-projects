"""
Iris Flower Classification using a Decision Tree

This script:
1. Loads the Iris dataset
2. Splits it into training and testing sets
3. Trains a Decision Tree classifier
4. Evaluates the model's accuracy
5. Predicts a single sample manually
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# --- Load Dataset ---
iris = load_iris()
features = iris.data           # Feature matrix: sepal length, sepal width, petal length, petal width
labels = iris.target          # Label vector: species (0=setosa, 1=versicolor, 2=virginica)

# --- Split Dataset (80% train, 20% test) ---
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# --- Train Model ---
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# --- Predict and Evaluate ---
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print("Prediction accuracy:", accuracy)

# --- Manual Sample Prediction ---
sample = [[5.1, 3.5, 1.4, 0.2]]  # Example input: [sepal length, sepal width, petal length, petal width]
predicted_class_index = model.predict(sample)[0]
predicted_species = iris.target_names[predicted_class_index]
print("Predicted flower class:", predicted_species)
