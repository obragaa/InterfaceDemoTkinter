from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedStyle  # Import themed style


# Function to close the window
def close_window():
    root.destroy()


# Create the main Tkinter window
root = Tk()

# Set the window size
root.geometry('400x300')

# Change the background to a specific color (can be a color name or hexadecimal code)
root.configure(bg="#67DBF5")

# Create a themed style
style = ThemedStyle(root)
style.set_theme("clam")  # Choose the "clam" theme

# Create a styled label with a message and center it
t = ttk.Label(root, text="Testing my Python skills with Tkinter!", font=('Arial', 16, 'bold'), foreground="#6781F5", background="#67DBF5")
t.place(relx=0.5, rely=0.4, anchor=CENTER)

# Style the button
style.configure('TButton', font=('Helvetica', 12), background="#6781F5", foreground="white", bordercolor="#6781F5")

# Button to close the window and center it
close_button = ttk.Button(root, text="Close Window", command=close_window)
close_button.place(relx=0.5, rely=0.6, anchor=CENTER)

# Start the Tkinter main loop
root.mainloop()
