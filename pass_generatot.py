import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(entry_length.get())
    if length > 0:
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
        result.set(password)
    else:
        messagebox.showwarning("Error", "Please enter a valid password length.")

# Create main window
root_password = tk.Tk()
root_password.title("Password Generator")
root_password.configure(bg="pink")

# Create UI elements
entry_length = tk.Entry(root_password, width=27, font=("Arial", 20), bg="brown")
result = tk.StringVar()

# Place UI elements in the window
tk.Label(root_password, text="Password Length:", font=("Arial", 20), bg="blue").pack(pady=(20,7))
entry_length.pack(pady=10)
generate_button = tk.Button(root_password, text="Generate Password", command=generate_password, font=("Arial", 20), bg="black", fg="blue")
generate_button.pack(pady=(7, 7))  # Added extra space below the button

password_label = tk.Label(root_password, textvariable=result, font=("Courier", 20), bg="purple")
password_label.pack(pady=(5, 5))  # Added extra space below the generated password label

# Run the password generator application
root_password.mainloop()