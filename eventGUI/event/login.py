from tkinter import *
from tkinter import messagebox

def student_login():
    username = student_username.get()
    password = student_password.get()
    if username == "student" and password == "123456":
        messagebox.showinfo("Login Successful", "Welcome, Student!")
        student_username.set("")
        student_password.set("")
        # Redirect to student home page
    else:
        messagebox.showerror("Login Error", "Invalid Username or Password")
        student_password.set("")

def admin_login():
    username = admin_username.get()
    password = admin_password.get()
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
        admin_username.set("")
        admin_password.set("")
        # Redirect to admin home page
    else:
        messagebox.showerror("Login Error", "Invalid Username or Password")
        admin_password.set("")

root = Tk()
root.title("Login Page")

# Create student login frame
student_frame = Frame(root, padx=10, pady=10)
student_frame.pack()
student_label = Label(student_frame, text="Student Login", font=("Helvetica", 16, "bold"))
student_label.grid(row=0, column=0, columnspan=2, pady=10)
student_username_label = Label(student_frame, text="Username:")
student_username_label.grid(row=1, column=0, padx=5, pady=5)
student_username = StringVar()
student_username_entry = Entry(student_frame, textvariable=student_username)
student_username_entry.grid(row=1, column=1, padx=5, pady=5)
student_password_label = Label(student_frame, text="Password:")
student_password_label.grid(row=2, column=0, padx=5, pady=5)
student_password = StringVar()
student_password_entry = Entry(student_frame, textvariable=student_password, show="*")
student_password_entry.grid(row=2, column=1, padx=5, pady=5)
student_login_button = Button(student_frame, text="Login", command=student_login)
student_login_button.grid(row=3, column=0, columnspan=2, pady=10)

# Create admin login frame
admin_frame = Frame(root, padx=10, pady=10)
admin_frame.pack()
admin_label = Label(admin_frame, text="Admin Login", font=("Helvetica", 16, "bold"))
admin_label.grid(row=0, column=0, columnspan=2, pady=10)
admin_username_label = Label(admin_frame, text="Username:")
admin_username_label.grid(row=1, column=0, padx=5, pady=5)
admin_username = StringVar()
admin_username_entry = Entry(admin_frame, textvariable=admin_username)
admin_username_entry.grid(row=1, column=1, padx=5, pady=5)
admin_password_label = Label(admin_frame, text="Password:")
admin_password_label.grid(row=2, column=0, padx=5, pady=5)
admin_password = StringVar()
admin_password_entry = Entry(admin_frame, textvariable=admin_password, show="*")
admin_password_entry.grid(row=2, column=1, padx=5, pady=5)
admin_login_button = Button(admin_frame, text="Login", command=admin_login)
admin_login_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()