import tkinter as tk
from tkinter import messagebox, simpledialog
import os

# Define a class to represent each student's data and perform calculations
class Student:
    def __init__(self, student_id, name, coursework_marks, exam_mark):
        self.student_id = student_id
        self.name = name
        self.coursework_marks = coursework_marks
        self.exam_mark = exam_mark
        self.total_coursework = sum(coursework_marks)
        self.overall_percentage = self.calculate_percentage()
        self.grade = self.calculate_grade()

    def calculate_percentage(self):
        total_marks = self.total_coursework + self.exam_mark
        return (total_marks / 160) * 100

    def calculate_grade(self):
        if self.overall_percentage >= 70:
            return 'A'
        elif self.overall_percentage >= 60:
            return 'B'
        elif self.overall_percentage >= 50:
            return 'C'
        elif self.overall_percentage >= 40:
            return 'D'
        else:
            return 'F'

    def display_record(self):
        return (f"Name: {self.name}\nID: {self.student_id}\nTotal Coursework Mark: {self.total_coursework}/60\n"
                f"Exam Mark: {self.exam_mark}/100\nOverall Percentage: {self.overall_percentage:.2f}%\n"
                f"Grade: {self.grade}")

# Function to load student data from the file
def load_students():
    students = []
    file_path = r"C:\Users\Emelyn\Documents\ASSESSMENTS\L5 SEMESTER 1\Advanced Programming\Exercise (To Pass)\studentMarks.txt"
    
    if not os.path.isfile(file_path):
        messagebox.showerror("File Not Found", f"The file '{file_path}' was not found.")
        return students
    
    with open(file_path, 'r') as file:
        num_students = int(file.readline().strip())
        for line in file:
            data = line.strip().split(',')
            student_id = int(data[0])
            name = data[1]
            coursework_marks = list(map(int, data[2:5]))
            exam_mark = int(data[5])
            students.append(Student(student_id, name, coursework_marks, exam_mark))
    return students

# Function to display all student records
def view_all_records(students):
    if not students:
        messagebox.showerror("No Data", "No student data loaded.")
        return
    records = ""
    total_percentage_sum = 0
    for student in students:
        records += student.display_record() + "\n\n"
        total_percentage_sum += student.overall_percentage
    average_percentage = total_percentage_sum / len(students)
    records += f"Total Students: {len(students)}\nAverage Percentage: {average_percentage:.2f}%"
    messagebox.showinfo("All Student Records", records)

# Function to view an individual student's record by name or ID
def view_individual_record(students):
    if not students:
        messagebox.showerror("No Data", "No student data loaded.")
        return
    choice = simpledialog.askstring("Select Student", "Enter student name or ID:")
    if choice:
        selected_student = None
        if choice.isdigit():
            for student in students:
                if str(student.student_id) == choice:
                    selected_student = student
                    break
        else:
            for student in students:
                if student.name.lower() == choice.lower():
                    selected_student = student
                    break
        if selected_student:
            messagebox.showinfo("Individual Student Record", selected_student.display_record())
        else:
            messagebox.showerror("Error", "Student not found.")

# Function to show the student with the highest overall mark
def highest_score_student(students):
    if not students:
        messagebox.showerror("No Data", "No student data loaded.")
        return
    highest_student = max(students, key=lambda student: student.overall_percentage)
    messagebox.showinfo("Highest Scoring Student", highest_student.display_record())

# Function to show the student with the lowest overall mark
def lowest_score_student(students):
    if not students:
        messagebox.showerror("No Data", "No student data loaded.")
        return
    lowest_student = min(students, key=lambda student: student.overall_percentage)
    messagebox.showinfo("Lowest Scoring Student", lowest_student.display_record())

# Main function to run the program and create the GUI
def main():
    students = load_students()

    # Create the main window
    root = tk.Tk()
    root.title("Student Records Management")

    # Define button actions
    tk.Button(root, text="View All Student Records", command=lambda: view_all_records(students)).pack(pady=10)
    tk.Button(root, text="View Individual Student Record", command=lambda: view_individual_record(students)).pack(pady=10)
    tk.Button(root, text="Show Student with Highest Score", command=lambda: highest_score_student(students)).pack(pady=10)
    tk.Button(root, text="Show Student with Lowest Score", command=lambda: lowest_score_student(students)).pack(pady=10)
    tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

    # Run the main loop to display the window
    root.mainloop()

# Run the main function if this file is executed as a script
if __name__ == "__main__":
    main()
