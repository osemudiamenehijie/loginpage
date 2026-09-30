import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Login Page")
root.geometry("400x300")
root.minsize(300, 300) 
root.configure(bg="#171A2B")


def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "123":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


tk.Label(
    root,
    text="Login",
    font=("Times New Roman", 18, "bold"),
    bg="#171A2B",
    fg="#fff"
).pack(pady=10)

tk.Label(root, text="Username:", bg="#fff").pack(pady=5)

username_entry = tk.Entry(root, width=45)
username_entry.pack(pady=5)

tk.Label(root, text="Password:", bg="#fff").pack(pady=5)

password_entry = tk.Entry(root, width=45, show="*")
password_entry.pack(pady=5)

login_button = tk.Button(
    root,
    text="Login",
    width=15,
    command=login
)
login_button.pack(pady=15)

root.mainloop()