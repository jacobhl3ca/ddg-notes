import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Initialize Selenium WebDriver (using Chrome in this case)
def initialize_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--remote-debugging-port=9222")  # To debug
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.google.com')  # Just an example URL
    return driver

# Automate the actions on the browser tabs
def automate_tabs(driver):
    try:
        # Get the total number of open tabs in the browser
        tabs = driver.window_handles
        num_tabs = len(tabs)

        print(f"Found {num_tabs} open tabs.")

        for i in range(num_tabs):
            driver.switch_to.window(tabs[i])

            # Perform the action on each tab (e.g., copy text, close tab, switch apps)
            pyautogui.press('tab')  # Navigate through tab
            pyautogui.hotkey('ctrl', 'c')  # Copy selected text
            time.sleep(0.1)

            pyautogui.hotkey('ctrl', 'w')  # Close the tab
            time.sleep(0.1)

            # Switch to the next app (e.g., text editor or terminal)
            pyautogui.hotkey('alt', 'tab')
            time.sleep(0.1)

            # Paste and press Enter
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')

            # Switch back to the browser
            pyautogui.hotkey('alt', 'tab')
            time.sleep(0.1)

    except Exception as e:
        print(f"Error during automation: {e}")

if __name__ == "__main__":
    browser = initialize_browser()
    automate_tabs(browser)
