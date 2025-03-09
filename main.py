from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

def send_danmu_with_selenium(room_url, message, cookies, repeat=3):
    options = webdriver.ChromeOptions()
    # Prevent detection of Selenium
    options.add_argument("--disable-blink-features=AutomationControlled")
    # Set other WebDriver options as needed
    with webdriver.Chrome(options=options) as driver:
        try:
            driver.get(room_url)
            # Set cookies
            for cookie in cookies:
                driver.add_cookie(cookie)
            # Reload the page to apply cookies
            driver.get(room_url)
            # Wait for the page to load
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

            # Initialize WebDriverWait for waiting for iframe and elements later
            wait = WebDriverWait(driver, 10)

            # Check if iframe exists
            try:
                frame = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe[src*="live.bilibili.com/blanc"]')))
                driver.switch_to.frame(frame)
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea.chat-input.border-box')))
            except TimeoutException:
                # If the specified iframe is not detected, continue operating on the main page
                driver.switch_to.default_content()
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea.chat-input.border-box')))
                print("No specific iframe detected, continuing on the main page")

            for i in range(repeat):  # Loop to send the message a specified number of times
                for attempt in range(3):
                    try:
                        danmu_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'textarea.chat-input.border-box')))
                        danmu_input.clear()
                        danmu_input.send_keys(message)
                        danmu_input.send_keys(Keys.ENTER)
                        print(f"Sent danmu {i + 1} times")
                        break
                    except StaleElementReferenceException:
                        if attempt == 2:
                            raise

                # Random wait 5 to 6 seconds to mimic human behavior in sending danmu (comments)
                time.sleep(random.uniform(5.0, 6.0))
        finally:
            # WebDriver will automatically close when exiting the context manager
            pass

# Usage example
if __name__ == "__main__":
    room_url = "https://live.bilibili.com/12345"
    message = "test"
    cookies = [
        {'name': 'CURRENT_FNVAL',       'value': 'your own', 'domain': '.bilibili.com', 'path': '/'},
        {'name': 'CURRENT_QUALITY',     'value': 'your own', 'domain': '.bilibili.com', 'path': '/'},
        {'name': 'DedeUserID',          'value': 'your own', 'domain': '.bilibili.com', 'path': '/'},
        {'name': 'DedeUserID__ckMd5',   'value': 'your own', 'domain': '.bilibili.com', 'path': '/'},
        {'name': 'SESSDATA',            'value': 'your own', 'domain': '.bilibili.com', 'path': '/'},
        {'name': 'bili_jct',            'value': 'your own', 'domain': '.bilibili.com', 'path': '/'},
        {'name': 'bili_ticket',         'value': 'your own', 'domain': '.bilibili.com', 'path': '/'}
    ]
    repeat = 3
    send_danmu_with_selenium(room_url, message, cookies, repeat=repeat)