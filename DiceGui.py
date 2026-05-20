import tkinter as tk
from PIL import Image, ImageTk
import random

# Initialize window

window = tk.Tk()
window.geometry("500x450") 
window.title("Dice Game")

# List of image files

dice = ["dice1.png.png", "dice2.png.png", "dice3.png.png", "dice4.png.png", "dice5.png.png", "dice6.png.png"]

# Function to open and resize image

def get_dice_image():
    img = Image.open(random.choice(dice))
    # Resize to 150x150 pixels
    img = img.resize((150, 150), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)

# Set initial images

image1 = get_dice_image()
image2 = get_dice_image()

# Create labels to display images

label1 = tk.Label(window, image=image1) 
label2 = tk.Label(window, image=image2)

# Keep reference to avoid garbage collection

label1.image = image1
label2.image = image2

# Position labels on window

label1.place(x=50, y=100)
label2.place(x=250, y=100)

# Function to update images on click

def roll_dice():
    global image1, image2
    image1 = get_dice_image()
    label1.configure(image=image1)
    label1.image = image1 
    
    image2 = get_dice_image()
    label2.configure(image=image2)
    label2.image = image2 

# Create Roll button

button = tk.Button(window, text="Roll Dice", bg="green", fg="white", font=("Arial", 14), command=roll_dice)
button.place(x=180, y=10)

# Create Exit button

button_exit = tk.Button(window, text="Exit", bg="red", fg="white", font=("Arial", 14), command=window.quit)
button_exit.place(x=210, y=360)

# Run the application
window.mainloop()