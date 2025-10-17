# Student Grade Calculator

# Function to calculate grade and comments
def calculate_grade(marks):
    if marks >= 90:
        return "A+", "Excellent performance!"
    elif marks >= 80:
        return "A", "Very good work!"
    elif marks >= 70:
        return "B", "Good effort, keep it up!"
    elif marks >= 60:
        return "C", "Satisfactory, but can improve."
    elif marks >= 50:
        return "D", "Needs more practice."
    else:
        return "F", "Failed. Try harder next time."

# List to store student results
students = []

# Take input for multiple students
while True:
    name = input("Enter student name: ")
    marks = float(input("Enter marks (0-100): "))
    
    # Calculate grade and comment
    grade, comment = calculate_grade(marks)
    
    # Store result in list
    students.append({
        "Name": name,
        "Marks": marks,
        "Grade": grade,
        "Comments": comment
    })
    
    # Ask user if they want to add another student
    more = input("Do you want to add another student? (yes/no): ").lower()
    if more != "yes":
        break

# Display all results
print("\n===== STUDENT GRADE REPORT =====")
for student in students:
    print(f"Name: {student['Name']}")
    print(f"Marks: {student['Marks']}")
    print(f"Grade: {student['Grade']}")
    print(f"Comments: {student['Comments']}")
    print("-" * 30)
