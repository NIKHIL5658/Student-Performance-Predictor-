# Study Pattern vs Academic Performance Prediction

📖 Description

This project uses Machine Learning (Linear Regression) to predict a student’s marks based on their study habits. The model takes into account factors like:

Study Hours
Attendance Percentage
Sleep Hours

The goal is to understand how these variables affect academic performance and to predict marks accordingly.

🛠️ Technologies Used
Python
Pandas
Scikit-learn
📂 Project Structure
├── main.py                     # Main Python program
├── dataset_StudyPattern.csv   # Dataset file
└── README.md                  # Project documentation
📊 Dataset Information

The dataset contains the following columns:

Column Name	Description
StudyHours	Number of hours studied per day
Attendance	Attendance percentage (%)
SleepHours	Average sleep hours per day
Marks	Marks obtained by the student
⚙️ How It Works
The dataset is loaded using Pandas
Features (inputs) and target (output) are defined
Data is split into training and testing sets
A Linear Regression model is trained
Model accuracy is calculated
User inputs values to predict marks

Code reference:

▶️ How to Run the Project
Install required libraries:
pip install pandas scikit-learn
Update dataset path in the code:
data = pd.read_csv("dataset_StudyPattern.csv")
Run the program:
python main.py
Enter input values when prompted:
Enter study hours:
Enter attendance (%):
Enter sleep hours:
📈 Output
Displays model accuracy
Predicts student marks based on input
⚠️ Important Notes
The dataset path in the code is currently hardcoded. Change it to a relative path before running.
Input values should be numeric
Accuracy depends on dataset quality
🚀 Future Improvements
Add data visualization (graphs)
Use advanced models (Random Forest, etc.)
Build a web interface using Flask or Streamlit
Improve dataset size and diversity

Developer-Nikhil Kumar <br>
REgistration no. -25BAI10465
