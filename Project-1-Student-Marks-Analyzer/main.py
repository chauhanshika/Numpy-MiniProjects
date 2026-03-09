import numpy as np

# Student marks dataset
marks = np.array([
    [85, 78, 92, 88],
    [76, 81, 79, 85],
    [90, 95, 94, 92],
    [65, 70, 72, 68],
    [88, 84, 86, 90]
])

students = ["Aman", "Riya", "Karan", "Neha", "Arjun"]

# Calculate average marks per student
avg_marks = np.mean(marks, axis=1)

print("Average Marks Per Student\n")

for i, student in enumerate(students):
    print(student, ":", avg_marks[i])
