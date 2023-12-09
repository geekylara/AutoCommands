import time
import pyautogui
import tkinter as tk
from tkinter import messagebox
from threading import Thread

def execute_command(command):
    print(f"Executing command: {command}")
    pyautogui.write(command)
    pyautogui.press('enter')

def show_alert(message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Alert", message)
    root.destroy()

def alert_thread_function(message):
    # Wait for a few seconds before showing the alert
    time.sleep(15)
    show_alert(message)

# Enable or disable the pop-up alert
SHOW_ALERT = True  # Set to True to enable, False to disable

# Wait for a few seconds before starting to give you time to focus on the game chat.
time.sleep(20) 

if SHOW_ALERT:
    # Alert user that the command will be executed in 10 seconds
    alert_thread = Thread(target=alert_thread_function, args=("Command will be executed in 10 seconds.",))
    alert_thread.start()

# Main loop
while True:
    # Define the command you want to execute.
    command_to_execute = "/kit esmeraldas"
    
    # Wait for 10 seconds
    time.sleep(10)

    # Execute the command
    execute_command(command_to_execute)

    # Show an alert that the command has been executed
    if SHOW_ALERT:
        alert_thread = Thread(target=alert_thread_function, args=("Command executed!",))
        alert_thread.start()

    # Wait for some time before repeating the loop (adjust as needed).
    time.sleep(60)  # For example, wait for 60 seconds between each execution.
