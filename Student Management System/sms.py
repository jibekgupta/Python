class Student:
  def __init__(self, student_id, name, age):
    self.student_id = student_id
    self.name  = name
    self.age = age
    self.grades = {}

  def add_grades(self, subject, grade):
    self.grades[subject] = grade

  def remove_grade(self, subject):
    if subject in self.grades:
      del self.grades[subject]

  def update_grade(self, subject, grade):
    if subject in self.grades:
      self.grades[subject] = grade

  def get_average_grade(self):
    if not self.grades:
      return 0
    total = sum(self.grades.values())
    count = len(self.grades)
    return total/ count

class StudentManagementSystem:
  def __init__(self):
    self.students = {}

  def add_student(self, student_id, name, age):
    if student_id not in self.students:
      self.students[student_id] = Student(student_id, name, age)

  def remove_student(self,student_id):
    if student_id not in self.students:
      del self.students[student_id]

  def update_student(self, student_id, name=None, age=None):
    if student_id in self.students:
      student =self.students[student_id]
      if name:
        student.name = name
      if age:
        student.age =age

  def add_grade_to_student(self,student_id, subject, grade):
    if student_id in self.students:
      self.students[student_id].add_grades(subject,grade)

  def remove_grade_from_student(self, student_id, subject):
    if student_id in self.students:
      self.students[student_id].remove_grade(subject)

  def update_grade_for_student(self, student_id, subject,grade):
    if student_id in self.students:
      self.students[student_id].update_grade(subject,grade)

  def get_student_average_grade(self, student_id):
    if student_id in self.students:
      return self.students[student_id].get_average_grade()

  def display_student(self,student_id):
    if student_id in self.students:
      student =self.students[student_id]
      info = f"Student ID: {student.student_id}\n"
      info += f"Name: {student.name}\n"
      info += f"Age: {student.age}\n"
      info +="Grades:\n"
      for subject, grade in student.grades.items():
        info +=f"  {subject}: {grade}\n"
      info += f"Average Grade: {student.get_average_grade()}\n"
      return info
    return "Student not found."
  
  def display_all_students(self):
    info =""
    for student_id, student in self.students.items():
      info += self.display_student(student_id) + "\n" + "-"*30 + "\n"
    return info
  










import tkinter as tk
from tkinter import messagebox

class StudentManagementGUI:
    def __init__(self,root):
        self.sms = StudentManagementSystem()
        self.root = root
        self.root.title("Student Management System")

        self.setup_ui()
    
    def setup_ui(self):
      # Frame fro student info
      frame_student = tk.Frame(self.root)
      frame_student.pack(pady=10)

      tk.Label(frame_student, text="Student ID").grid(row=0, column=0)
      tk.Label(frame_student, text="Name").grid(row=1, column=0)
      tk.Label(frame_student, text="Age").grid(row=2, column=0)

      self.entry_student_id = tk.Entry(frame_student)
      self.entry_name = tk.Entry(frame_student)
      self.entry_age = tk.Entry(frame_student)

      self.entry_student_id.grid(row=0, column=1)
      self.entry_name.grid(row=1, column=1)
      self.entry_age.grid(row=2, column=1)

      tk.Button(frame_student, text="Add Student", command=self.add_student).grid(row=3, column=0, columnspan=2)

      # Frame for grade info
      frame_grade =tk.Frame(self.root)
      frame_grade .pack(pady=10)

      tk.Label(frame_grade, text="Student ID").grid(row=0, column=0)
      tk.Label(frame_grade, text="Subject").grid(row=1,column=0)
      tk.Label(frame_grade, text="Grade").grid(row=2, column=0)

      self.entry_grade_student_id = tk.Entry(frame_grade)
      self.entry_subject = tk.Entry(frame_grade)
      self.entry_grade = tk.Entry(frame_grade)

      self.entry_grade_student_id.grid(row=0, column=1)
      self.entry_subject.grid(row=1, column=1)
      self.entry_grade.grid(row=2, column=1)


      tk.Button(frame_grade, text="Add Grade", command= self.add_grade).grid(row=3, column=0, columnspan=2)

      # Frame for displaying info
      frame_display = tk.Frame(self.root)
      frame_display.pack(pady=10)

      tk.Button(frame_display, text="Display All Students", command=self.display_all_student).grid(row=0, column=0)

      self.text_display = tk.Text(frame_display, height=10, width=50)
      self.text_display.grid(row=1, column=0)

    def add_student(self):
        try:
          student_id = int(self.entry_student_id.get())
          name = self.entry_name.get()
          age = int(self.entry_age.get())
          self.sms.add_student(student_id, name, age)
          messagebox.showinfo("Info","Student add successfully")
        except ValueError:
          messagebox.showerror("Error", "Invalid input. Please check the student ID and age")
    

    def add_grade(self):
        try:
            student_id = int(self.entry_grade_student_id.get())
            subject = self.entry_subject.get()
            grade = int(self.entry_grade.get())
            self.sms.add_grade_to_student(student_id, subject, grade)
            messagebox.showinfo("Info","Grade added successfully")
        except ValueError:
          messagebox.showerror("Error", "Invalid input. Please check the student ID and grade")
    

    def display_all_student(self):
      self.text_display.delete(1.0, tk.END)
      for student_id, student in self.sms.students.items():
        student_info = f"Student ID: {student.student_id}\nName: {student.name}\nAge:{student.age}\nGrades: {student.grades}\nAverage Grade: {student.get_average_grade()}\n\n"
        self.text_display.insert(tk.END, student_info)


    


    
      




if __name__ == "__main__":
  root =tk.Tk()
  app = StudentManagementGUI(root)
  root.mainloop()
