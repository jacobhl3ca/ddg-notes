import pyautogui
import pyperclip
import time
import sys

def automate_tabs(num_tabs):
    try:
        for _ in range(num_tabs):
            # Simulate pressing Tab to focus on the text field
            pyautogui.press('tab')

            # Simulate pressing Ctrl+C to copy the text
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(0.1)  # small delay to ensure copy is successful

            # Simulate pressing Ctrl+W to close the tab
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(0.1)

            # Switch to the next application (Alt+Tab)
            pyautogui.hotkey('alt', 'tab')
            time.sleep(0.1)

            # Paste the copied text (Ctrl+V) and press Enter
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')

            # Switch back to the browser (Alt+Tab)
            pyautogui.hotkey('alt', 'tab')
            time.sleep(0.1)

    except Exception as e:
        print(f"Error during automation: {e}")

if __name__ == "__main__":
    num_tabs = int(input("Enter the number of tabs to automate: "))
    automate_tabs(num_tabs)
