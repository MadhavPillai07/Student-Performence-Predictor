import pandas as pd
from sklearn.linear_model import LinearRegression

# -----------------------------
# Sample Dataset (you can expand later)
# -----------------------------
data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "attendance": [50, 60, 65, 70, 75, 80, 85, 90],
    "sleep_hours": [5, 6, 6, 7, 7, 7, 8, 8],
    "previous_marks": [40, 45, 50, 55, 60, 65, 70, 75],
    "final_marks": [42, 48, 52, 58, 63, 68, 74, 80]
}

df = pd.DataFrame(data)

# -----------------------------
# Training ML Model
# -----------------------------
X = df[["study_hours", "attendance", "sleep_hours", "previous_marks"]]
y = df["final_marks"]

model = LinearRegression()
model.fit(X, y)

print("✅ Model trained successfully!\n")

# -----------------------------
# Taking User Input
# -----------------------------
print("Enter student details:\n")

study_hours = float(input("Study hours per day: "))
attendance = float(input("Attendance (%): "))
sleep_hours = float(input("Sleep hours: "))
previous_marks = float(input("Previous marks: "))

# -----------------------------
# Prediction
# -----------------------------
prediction = model.predict([[study_hours, attendance, sleep_hours, previous_marks]])

predicted_marks = round(prediction[0], 2)

print(f"\n📊 Predicted Marks: {predicted_marks}")

# -----------------------------
# Performance Category
# -----------------------------
if predicted_marks >= 75:
    performance = "Excellent"
elif predicted_marks >= 60:
    performance = "Good"
elif predicted_marks >= 50:
    performance = "Average"
else:
    performance = "Poor"

print(f"📈 Performance Level: {performance}")

# -----------------------------
# Study Suggestions (AI Logic)
# -----------------------------
print("\n💡 Suggestions:")

if study_hours < 4:
    print("- Increase study hours 📚")

if attendance < 75:
    print("- Improve attendance 🏫")

if sleep_hours < 6:
    print("- Get proper sleep 😴")

if previous_marks < 50:
    print("- Revise basics and practice more ✍️")

if (study_hours >= 5 and attendance >= 80 and sleep_hours >= 7):
    print("- Keep up the good work! 🚀")
