# Import the necessary modules
import tkinter as tk
import tkinter.ttk as ttk

# Define the function to update the result 
def update_result(*args):
    try:
        # Get input values from entry boxes and convert from hexadecimal to integer
        base_decimal = int(base_entry.get(), 16)
        num_decimal = int(num_entry.get(), 16)
        
        # Subtract and convert the value back to hexadecimal and remove "0x" prefix
        result = hex(base_decimal - num_decimal)[2:]
        
        # Optionally make the result uppercase if the checkbox is checked
        if upper_case_text.get():
            result = result.upper()
        
        # Optionally add "0x" prefix if the checkbox is checked
        if add_prefix.get():
            result = "0x" + result
        
        # Set the string values of the result fields
        result_text.set(result)
        result_int = int(result, 16)
        result_text2.set(str(result_int // 4))

    # Handle ValueError exception
    except ValueError:
        result_text.set("Invalid input")
        result_text2.set("Invalid input")

# Define the function to copy the result to clipboard 
def copy_result():
    root.clipboard_clear()
    root.clipboard_append(result_text.get())

# Define the function to copy the VMT result to clipboard 
def copy_result2():
    root.clipboard_clear()
    root.clipboard_append(result_text2.get())

# Define the function to toggle "Always on top" feature 
def toggle_always_on_top():
    # Toggle always on top feature
    root.attributes("-topmost", not root.attributes("-topmost"))

# Create the main window and set the attributes
root = tk.Tk()
root.title("HexVMT")
root.resizable(False, False)
root.geometry("230x310")

# Set the font style
style = ttk.Style()
style.configure('.', font=('Consolas', 10))

# Add a custom X button
close_button = ttk.Button(root, text='X', command=root.quit, style='Custom.TButton')
close_button.place(relx=1, x=-2, y=-2, anchor='se')

# Add labels and entry boxes
base_label = ttk.Label(root, text="X")
base_label.grid(row=1, column=0, padx=6, pady=6, sticky="w")

base_entry = ttk.Entry(root)
base_entry.grid(row=1, column=0, padx=25, pady=6, sticky="w")
base_entry.bind("<KeyRelease>", update_result)

num_label = ttk.Label(root, text="Y")
num_label.grid(row=2, column=0, padx=6, pady=6, sticky="w")

num_entry = ttk.Entry(root)
num_entry.grid(row=2, column=0, padx=25, pady=6, sticky="w")
num_entry.bind("<KeyRelease>", update_result)

num_label = ttk.Label(root, text="R")
num_label.grid(row=3, column=0, padx=6, pady=6, sticky="w")

# Field for result
result_text = tk.StringVar()
result_box = ttk.Entry(root, textvariable=result_text, width=20, state="readonly")
result_box.grid(row=3, column=0, columnspan=6, pady=10, padx=25, sticky="w")
result_box.bind("<Control-Key-a>", lambda event: result_box.select_range(0, "end"))
result_box.bind("<Control-Key-c>", lambda event: copy_result())

# Field for VMT Result
result_text2 = tk.StringVar()
result_box2 = ttk.Entry(root, textvariable=result_text2, width=20, state="readonly")
result_box2.grid(row=6, column=0, columnspan=6, pady=10, padx=25, sticky="w")
result_box2.bind("<Control-Key-a>", lambda event: result_box2.select_range(0, "end"))
result_box2.bind("<Control-Key-c>", lambda event: copy_result2())

# Buttons to copy results
copy_button = ttk.Button(root, text="Copy R", command=copy_result,  width=6, style='Custom.TButton')
copy_button.grid(row=7, column=0, columnspan=6, pady=10, padx=25, sticky="w")

copy_button = ttk.Button(root, text="Copy I", command=copy_result2, width=6, style='Custom.TButton')
copy_button.grid(row=7, column=0, columnspan=6, pady=10, padx=100, sticky="w")

# Checkbuttons for options
always_on_top_var = tk.BooleanVar()
always_on_top_var.set(False)
always_on_top_button = ttk.Checkbutton(root, text="Always on top", variable=always_on_top_var, command=toggle_always_on_top)
always_on_top_button.grid(row=9, column=0, pady=10, padx=6, sticky="w")

add_prefix = tk.BooleanVar()
add_prefix.set(False)
prefix_check = ttk.Checkbutton(root, text="Add '0x' prefix", variable=add_prefix, command=update_result, style='Custom.TCheckbutton')
prefix_check.grid(row=10, column=0, pady=10, padx=6, sticky="w")

upper_case_text = tk.BooleanVar()
upper_case_text.set(False)
upper_case_text_check = ttk.Checkbutton(root, text="Uppercase result", variable=upper_case_text, command=update_result, style='Custom.TCheckbutton')
upper_case_text_check.grid(row=11, column=0, pady=10, padx=6, sticky="w")

# Call update result function to update the fields with initial values
update_result()

# Start the main event loop
root.mainloop()
