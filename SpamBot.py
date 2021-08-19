# Automated text messaging

# Import modules
import time
import pyautogui

# The code
def send_message ():
    time.sleep(4) # Python will pause for 4 seconds before proceeding
    text = open("message.txt")
    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press(each_line)

send_message()Messenger



