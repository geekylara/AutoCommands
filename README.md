## Auto Command Execution Script for Minecraft

This Python script automates the execution of a specific command within Minecraft. The script utilizes the `pyautogui` library for simulating keyboard input and includes an optional alert feature using the `tkinter` library to notify the user that the command will be executed.

### How it Works

1. **Dependencies**
    - Ensure you have Python installed on your system.
    - Install the required Python packages using the following command:
        ```bash
        pip install pyautogui
        ```

2. **Execution**
    - Run the script (`script.py`) using Python:
        ```bash
        python script.py
        ```
    - The script will wait for a few seconds to allow you to focus on the game chat.

3. **Alert (Optional)**
    - A pop-up alert will notify you that the specified command will be executed in 10 seconds if the `SHOW_ALERT` variable is set to `True`.

4. **Command Execution**
    - The script will then enter a loop, executing the specified command in the Minecraft chat every 60 seconds.

### Customization

- Adjust the command to be executed by modifying the `command_to_execute` variable.
- Modify the sleep durations to suit your specific requirements.

### Optional Alert

- Set the `SHOW_ALERT` variable to `True` or `False` to enable or disable the pop-up alert.

```python
# Enable or disable the pop-up alert
SHOW_ALERT = True  # Set to True to enable, False to disable
```

### Important Note

Make sure to review and comply with the terms of service of the Minecraft server you are using. Automated scripts and certain actions may be subject to server rules and policies.

Feel free to customize and adapt the script based on your needs. Enjoy!

---

**Disclaimer:** This script is provided as-is and may be subject to the terms of service of the game or server. Use responsibly and considerate of other players' experiences.