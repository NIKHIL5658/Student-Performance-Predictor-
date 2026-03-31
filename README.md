# Student Performance Predictor

📖 Description

This project uses Machine Learning (Linear Regression) to predict a student’s marks based on their study habits. The model takes into account factors like:

Study Hours
Attendance Percentage
Sleep Hours

The goal is to understand how these variables affect academic performance and to predict marks accordingly. <br>

🛠️ Technologies Used <br>
Python <br>
Pandas <br>
Scikit-learn <br>
📂 Project Structure <br>
├── main.py                     # Main Python program <br>
├── dataset_StudyPattern.csv   # Dataset file <br>
└── README.md                  # Project documentation <br>
📊 Dataset Information <br>

The dataset contains the following columns: <br>

Column Name	Description <br>
StudyHours	Number of hours studied per day <br>
Attendance	Attendance percentage (%)  <br>
SleepHours	Average sleep hours per day  <br>
Marks	Marks obtained by the student  <br>

⚙️ How It Works   <br>

The dataset is loaded using Pandas   <br>
Features (inputs) and target (output) are defined   <br>
Data is split into training and testing sets   <br>
A Linear Regression model is trained   <br>
Model accuracy is calculated  <br>
User inputs values to predict marks  <br>

Code reference:  <br>
▶️ How to Run the Project  <br>
Install required libraries:  <br>
pip install pandas scikit-learn  <br>
Update dataset path in the code:  <br>
data = pd.read_csv("dataset_StudyPattern.csv")  <br>
Run the program:  <br>
python main.py <br>

Enter input values when prompted: <br>
Enter study hours:  <br>
Enter attendance (%):  <br>
Enter sleep hours:  <br>

📈 Output  <br>
Displays model accuracy  <br>
Predicts student marks based on input  <br>

⚠️ Important Notes <br>
The dataset path in the code is currently hardcoded. Change it to a relative path before running.  <br>
Input values should be numeric  <br>
Accuracy depends on dataset quality  <br>

🚀 Future Improvements  <br>
Add data visualization (graphs)  <br>
Use advanced models (Random Forest, etc.)   <br>
Build a web interface using Flask or Streamlit  <br>
Improve dataset size and diversity  <br>

Developer-Nikhil Kumar <br>
REgistration no. -25BAI10465  <br>
