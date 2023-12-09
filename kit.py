import time
import pyautogui
import tkinter as tk
from tkinter import messagebox

def execute_command(command):
    pyautogui.write(command)
    pyautogui.press('enter')

def show_alert(message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Alert", message)
    root.destroy()

# Wait for a few seconds before starting to give you time to focus on the game chat.
time.sleep(6)

# Alert user that the command will be executed in 10 seconds
show_alert("Command will be executed in 10 seconds.")

# Main loop
while True:
    # Define the command you want to execute.
    command_to_execute = "/kits esmeraldas"
    
    # Wait for 10 seconds
    time.sleep(10)

    # Execute the command
    execute_command(command_to_execute)

    # Show an alert that the command has been executed
    show_alert("Command executed!")

    # Wait for some time before repeating the loop (adjust as needed).
    time.sleep(60)  # For example, wait for 60 seconds between each execution.
