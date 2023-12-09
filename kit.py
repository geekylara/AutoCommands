import time  # Import the 'time' module for handling time-related functions.
import pyautogui  # Import the 'pyautogui' module for simulating keyboard and mouse input.

def execute_command(command):
    pyautogui.write(command)  # Simulate typing the specified command.
    pyautogui.press('enter')  # Simulate pressing the 'Enter' key.

# Wait for a few seconds before starting to give you time to focus on the game chat.
time.sleep(6)

# Main loop
while True:
    # Define the command you want to execute.
    command_to_execute = "/kits esmeraldas"
    
    # Execute the command
    execute_command(command_to_execute)
    
    # Wait for some time before repeating the loop (adjust as needed).
    time.sleep(60)  # For example, wait for 60 seconds between each execution.
