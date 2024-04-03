import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def delete_characters(string, chars_to_delete):
    new_string = ''
    for c in string:
        if c not in chars_to_delete:
            new_string += c
    return new_string
def generate_password():
    length = int(length_entry.get())
    chars = str(char_entry.get())
    chars_list = chars.split(",")
    prefered_string = delete_characters(string.ascii_letters + string.digits + string.punctuation,chars_list)
    if length <= 0:
        messagebox.showerror("Error", "Please enter a positive integer for password length.")
        return
    password = ''.join(random.choices(prefered_string, k=length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    password = password_entry.get()
    pyperclip.copy(password)
    messagebox.showinfo("Copied", "Password copied to clipboard.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place widgets
length_label = tk.Label(root, text="Enter Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=5)

length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=5)

char_label = tk.Label(root, text="Enter excluded characters:")
char_label.grid(row=1, column=0, padx=10, pady=5)

char_entry = tk.Entry(root)
char_entry.grid(row=1, column=1, padx=10, pady=5)


generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="we")

password_label = tk.Label(root, text="Generated Password:")
password_label.grid(row=3, column=0, padx=10, pady=5)


password_entry = tk.Entry(root)
password_entry.grid(row=3, column=1, padx=10, pady=5)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="we")



# Run the main event loop
root.mainloop()