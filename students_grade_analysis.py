
# Load dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
students_grades = pd.read_csv("students_grades.csv") # copy file path here 
print(students_grades)

# find missing values
missing_values = students_grades.isnull().sum() 
print(missing_values) 

# Imputation of Missing Values with zero
students_grades.fillna(0, inplace=True) 
missing_values = students_grades.isnull().sum() 
print(missing_values)

# Calculate average score across subjects
Average_score = students_grades[["Math", "English", "Science"]].mean(axis=1) 
print(Average_score)                                                               

# Round Off Average Scores
Average_score = Average_score.round(1)
print(Average_score)

# Add Average Score to Original Dataset
students_grades["Average_score"]= Average_score
print(students_grades)

# Find highest and lowest average scores
Highest_average = students_grades["Average_score"].max()
print(Highest_average)
Lowest_average = students_grades["Average_score"].min()
print(Lowest_average)

# Mode and Median
mode_of_average = students_grades["Average_score"].mode().tolist()
print(mode_of_average)
median_of_average = students_grades["Average_score"].median()
print(median_of_average)

# Plot distribution of average scores
sns.histplot(students_grades["Average_score"], bins=10)
plt.xlabel("Average scores")
plt.ylabel("Student count")
plt.title("Distribution of Average Scores")

plt.show()

# Correlation matrix
print(students_grades[['Math','English','Science']].corr().round(2))

# Sort averages high to low
Average_high_to_low = students_grades["Average_score"].sort_values(ascending=False)
print(Average_high_to_low)

# Find student(s) with highest average
student_with_highest_average = students_grades.loc[students_grades["Average_score"] == Highest_average, "Name"].tolist() 
word = "Student" if len(student_with_highest_average) == 1 else "Students"
print(f"{word} with highest average score: {','.join(student_with_highest_average)}")

