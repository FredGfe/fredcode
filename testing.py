import pandas as pd

# Sample coffee shop sales data
data = {
    'Date': ['2024-06-01', '2024-06-01', '2024-06-02', '2024-06-02'],
    'Product': ['Latte', 'Espresso', 'Latte', 'Cappuccino'],
    'Quantity': [10, 5, 8, 7],
    'Price': [3.5, 2.5, 3.5, 4.0]
}

df = pd.DataFrame(data)

# Calculate total sales per product
df['Total'] = df['Quantity'] * df['Price']
sales_per_product = df.groupby('Product')['Total'].sum()

# Calculate total quantity sold per product
quantity_per_product = df.groupby('Product')['Quantity'].sum()

import pandas as pd
import tkinter as tk
from tkinter import ttk

# Sample coffee shop sales data
data = {
    'Date': ['2024-06-01', '2024-06-01', '2024-06-02', '2024-06-02'],
    'Product': ['Latte', 'Espresso', 'Latte', 'Cappuccino'],
    'Quantity': [10, 5, 8, 7],
    'Price': [3.5, 2.5, 3.5, 4.0]
}

df = pd.DataFrame(data)

# Calculate total sales per product
df['Total'] = df['Quantity'] * df['Price']
sales_per_product = df.groupby('Product')['Total'].sum()

# Calculate total quantity sold per product
quantity_per_product = df.groupby('Product')['Quantity'].sum()

# Create GUI interface
root = tk.Tk()
root.title("Coffee Shop Sales Analysis")

# Create frames
sales_frame = ttk.LabelFrame(root, text="Total Sales per Product")
sales_frame.pack(pady=10, padx=10, fill="x")

quantity_frame = ttk.LabelFrame(root, text="Total Quantity Sold per Product")
quantity_frame.pack(pady=10, padx=10, fill="x")

# Display sales data
sales_text = tk.Text(sales_frame, height=5, width=50)
sales_text.pack(pady=5, padx=5)
sales_text.insert(tk.END, str(sales_per_product))

# Display quantity data
quantity_text = tk.Text(quantity_frame, height=5, width=50)
quantity_text.pack(pady=5, padx=5)
quantity_text.insert(tk.END, str(quantity_per_product))

# Run the GUI
root.mainloop()