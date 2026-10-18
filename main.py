import tkinter as tk

root = tk.Tk()
root.title("Workshop Participant Greeting")

heading = tk.Label(
    root, 
    text="Workshop Welcome Desk", 
    fg="white", 
    bg="#525f07", 
    height=5,
    width=300
)
heading.pack()

name_label = tk.Label(root, text="Participant Name", bg="#D3A438")
name_label.pack(pady=10)

name_entry = tk.Entry(root)
name_entry.pack()

# Define the text_box BEFORE the function so Python can see it
text_box = tk.Text(root, height=4, width=40)

def display_welcome():
    # Both lines are properly indented together
    name = name_entry.get()
    text_box.delete(1.0, tk.END)
    
    # Inserting your greeting message
    text_box.insert(tk.END, "Hello " + name + "!\n")
    text_box.insert(tk.END, "Welcome to the workshop.")

welcome_button = tk.Button(root, text="Check In", command=display_welcome, bg="#2712A0", fg="white")
welcome_button.pack(pady=15)

text_box.pack()

root.mainloop()