import csv
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Read the generated dataset
features = []
labels = []

with open("ml_builds.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        features.append([
            int(row["files_changed"]),
            int(row["lines_changed"]),
            int(row["tests_touched"]),
            int(row["hour"])
        ])
        labels.append(int(row["failed"]))

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    features,
    labels,
    test_size=0.2,
    random_state=42,
    stratify=labels
)

# Train Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print("Model training completed!")
print("Model accuracy:", round(accuracy * 100, 2), "%")

# Display feature importance
feature_names = [
    "Files changed",
    "Lines changed",
    "Tests touched",
    "Commit hour"
]

print("\nFeature Importance:")
for name, importance in zip(
    feature_names, model.feature_importances_
):
    print(name, ":", round(importance, 3))

# Predict a large, late-night, untested change
large_change = [[18, 900, 1, 23]]
large_risk = model.predict_proba(large_change)[0][1]

# Predict a small, well-tested change
small_change = [[2, 30, 12, 10]]
small_risk = model.predict_proba(small_change)[0][1]

print("\nBuild Failure Predictions:")
print("Large change failure risk:", round(large_risk * 100, 2), "%")
print("Small change failure risk:", round(small_risk * 100, 2), "%")