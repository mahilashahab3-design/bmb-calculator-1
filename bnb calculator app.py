import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # convert cm to meters
        bmi = weight / (height ** 2)
        bmi_value.set(f"{bmi:.2f}")
        
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"
        bmi_category.set(category)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Variables
bmi_value = tk.StringVar()
bmi_category = tk.StringVar()

# GUI components
tk.Label(root, text="Weight (kg):").grid(row=0, column=0, padx=10, pady=10)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Height (cm):").grid(row=1, column=0, padx=10, pady=10)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=10, pady=10)

calculate_btn = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_btn.grid(row=2, column=0, columnspan=2, pady=10)

tk.Label(root, text="BMI Value:").grid(row=3, column=0, padx=10, pady=10)
tk.Label(root, textvariable=bmi_value).grid(row=3, column=1, padx=10, pady=10)

tk.Label(root, text="BMI Category:").grid(row=4, column=0, padx=10, pady=10)
tk.Label(root, textvariable=bmi_category).grid(row=4, column=1, padx=10, pady=10)

# Run the application
root.mainloop()