import tkinter as tk
from tkinter import ttk

# Function to apply ROT-13 transformation
def rot13(text):
    return text.translate(str.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
        "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    ))

# Function to update the text with ROT-13 encoding
def apply_rot13():
    input_text = text_entry.get()
    output_text.set(rot13(input_text))

# Create the main window
root = tk.Tk()
root.title("ROT-13 Encoder")
root.geometry("400x200")

# Input field
text_entry = tk.Entry(root, width=50)
text_entry.pack(pady=10)

# Output field
output_text = tk.StringVar()
output_label = tk.Label(root, textvariable=output_text, font=("Arial", 12))
output_label.pack(pady=10)

# ROT-13 Button
rot13_button = ttk.Button(root, text="Apply ROT-13", command=apply_rot13)
rot13_button.pack(pady=10)

# Run the application
root.mainloop()
