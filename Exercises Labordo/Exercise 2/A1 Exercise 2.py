from tkinter import *
import random

# Create the main window (root)
root = Tk()
root.title("Random Joke Generator")  # Set the title of the window
root.geometry("500x500")  # Set the size of the window (width x height)
root.configure(bg="#1b6ba8")  # Set the background color of the window

# Function to load jokes from the file and return them as a list
def load_jokes():
    file_path = "C:/Users/Emelyn/Documents/ASSESSMENTS/L5 SEMESTER 1/Advanced Programming/Exercise (To Pass)/Exercise 2/randomJokes.txt"
    
    with open(file_path, 'r') as file_handler:
        jokes = [line.strip().split('?') for line in file_handler.readlines() if '?' in line]  # Split by '?' and store setup and punchline

    return jokes

# Function to display a random joke setup
def show_setup():
    global current_joke
    current_joke = random.choice(jokes)  # Select a random joke (setup and punchline)
    
    txtarea.delete("1.0", "end")  # Clear the text area for new joke
    txtarea.insert(END, current_joke[0] + "?")  # Show the joke setup

# Function to display the punchline of the current joke
def show_punchline():
    if current_joke:
        txtarea.insert(END, f"\n\n{current_joke[1]}")  # Show the punchline of the current joke

# Load jokes from the file into the list
jokes = load_jokes()
current_joke = None  # Variable to keep track of the current joke

# Create a text area (multiline text input) where the joke setup and punchline will be displayed
txtarea = Text(root, font=("Arial", 12))
txtarea.place(x=20, y=40, height=200, width=460)  # Set position and size of the text area

# Create a vertical scrollbar for the text area
scrollV = Scrollbar(root, orient='vertical')
scrollV.place(x=480, y=40, height=200)  # Set the position and height of the scrollbar

# Configure the scrollbar to scroll the text area when moved
scrollV.config(command=txtarea.yview)
txtarea.config(yscrollcommand=scrollV.set)  # Sync the text area with the scrollbar

# Button to show a new joke setup
btn_setup = Button(root, text="Tell Me a Joke", command=show_setup)
btn_setup.place(x=50, y=300, height=30, width=150)  # Set the button's position and size

# Button to show the punchline of the current joke
btn_punchline = Button(root, text="Show Punchline", command=show_punchline)
btn_punchline.place(x=300, y=300, height=30, width=150)  # Set the button's position and size

# Button to quit the application
btn_quit = Button(root, text="Quit", command=root.quit)
btn_quit.place(x=175, y=400, height=30, width=150)  # Set the button's position and size

# Run the tkinter main event loop (keeps the window open and responsive)
root.mainloop()
