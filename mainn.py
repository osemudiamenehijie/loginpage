import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Login Page")
root.geometry("400x300")
root.minsize(300, 300)
root.configure(bg="#171A2B")


# Dashboard
def dashboard():

    # Close the login window
    root.destroy()

    # Create dashboard window
    dashboard_window = tk.Tk()
    dashboard_window.title("Dashboard")
    dashboard_window.geometry("600x400")
    dashboard_window.configure(bg="#171A2B")

    tk.Label(
        dashboard_window,
        text="Dashboard",
        font=("Times New Roman", 24, "bold"),
        bg="#171A2B",
        fg="white"
    ).pack(pady=30)

    tk.Label(
        dashboard_window,
        text="Welcome, Admin!",
        font=("Arial", 16),
        bg="#171A2B",
        fg="white"
    ).pack(pady=10)

    tk.Button(
        dashboard_window,
        text="Logout",
        width=15,
        command=dashboard_window.destroy
    ).pack(pady=30)

    dashboard_window.mainloop()


# Login function
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "123":
        dashboard()
    else:
        messagebox.showerror(
            "Login Failed",
            "Invalid username or password"
        )


# Login title
tk.Label(
    root,
    text="Login",
    font=("Times New Roman", 18, "bold"),
    bg="#171A2B",
    fg="#fff"
).pack(pady=10)


# Username
tk.Label(
    root,
    text="Username:",
    bg="#171A2B",
    fg="white"
).pack(pady=5)

username_entry = tk.Entry(root, width=45)
username_entry.pack(pady=5)


# Password
tk.Label(
    root,
    text="Password:",
    bg="#171A2B",
    fg="white"
).pack(pady=5)

password_entry = tk.Entry(
    root,
    width=45,
    show="*"
)

password_entry.pack(pady=5)


# Login button
login_button = tk.Button(
    root,
    text="Login",
    width=15,
    command=login
)

login_button.pack(pady=15)


root.mainloop()
