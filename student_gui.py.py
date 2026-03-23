import tkinter as tk
from tkinter import messagebox

class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

class StudentManagement:
    def __init__(self, root):
        self.students = []
        self.root = root
        self.root.title("Student Management System")

        tk.Label(root, text="Name").grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        tk.Label(root, text="Roll No").grid(row=1, column=0)
        self.roll_entry = tk.Entry(root)
        self.roll_entry.grid(row=1, column=1)

        tk.Label(root, text="Marks").grid(row=2, column=0)
        self.marks_entry = tk.Entry(root)
        self.marks_entry.grid(row=2, column=1)

        tk.Button(root, text="Add", command=self.add_student).grid(row=3, column=0)
        tk.Button(root, text="Show", command=self.show_students).grid(row=3, column=1)
        tk.Button(root, text="Delete", command=self.delete_student).grid(row=4, column=0)
        tk.Button(root, text="Search", command=self.search_student).grid(row=4, column=1)

        self.output = tk.Text(root, height=10, width=40)
        self.output.grid(row=5, column=0, columnspan=2)

    def add_student(self):
        name = self.name_entry.get()
        roll = self.roll_entry.get()

        try:
            marks = int(self.marks_entry.get())
        except:
            messagebox.showerror("Error", "Invalid Marks")
            return

        self.students.append(Student(name, roll, marks))
        messagebox.showinfo("Success", "Student Added")
        self.show_students()
        self.clear_fields()

    def show_students(self):
        self.output.delete(1.0, tk.END)

        if not self.students:
            self.output.insert(tk.END, "No Students Found\n")
            return

        for s in self.students:
            self.output.insert(tk.END, f"{s.name} | {s.roll} | {s.marks}\n")

    def delete_student(self):
        roll = self.roll_entry.get().strip()

        for s in self.students:
            if s.roll == roll:
                self.students.remove(s)
                messagebox.showinfo("Deleted", "Student Removed")
                self.show_students()
                self.clear_fields()
                return

        messagebox.showerror("Error", "Student Not Found")

    def search_student(self):
        roll = self.roll_entry.get().strip()

        for s in self.students:
            if s.roll == roll:
                self.output.delete(1.0, tk.END)
                self.output.insert(tk.END, f"{s.name} | {s.roll} | {s.marks}")
                return

        messagebox.showerror("Error", "Student Not Found")

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.roll_entry.delete(0, tk.END)
        self.marks_entry.delete(0, tk.END)


root = tk.Tk()
app = StudentManagement(root)
root.mainloop()