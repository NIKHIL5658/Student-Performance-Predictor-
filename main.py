import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv(r"C:\Desktop\AI & ML\dataset_StudyPattern.csv", skipinitialspace=True)

X = data[["StudyHours", "Attendance", "SleepHours"]]
y = data["Marks"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

print("Model Accuracy:", model.score(X_test, y_test))

study_hours = float(input("Enter study hours: "))
attendance = float(input("Enter attendance (%): "))
sleep_hours = float(input("Enter sleep hours: "))

prediction = model.predict([[study_hours, attendance, sleep_hours]])
print("Predicted Marks:", prediction[0])