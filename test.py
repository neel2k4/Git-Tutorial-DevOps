#my first python code. Time to learn data science technologies like PowerBI and Tableau and Python
#my first change to compare
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Selenium WebDriver (you need to have the appropriate driver executable in your PATH)
driver = webdriver.Chrome()

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")

# Wait for the user to scan the QR code and log in
input("Press enter after scanning the QR code and logging in...")

# Find the target group by its title
group_title = "DYPH(Part)-NityaNanda BV"
group_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, f'//span[@title="{DYPH(Part)-NityaNanda BV}"]'))
)

# Click on the group to open the chat
group_element.click()

# Wait for the chat to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.message-in'))
)

# Find all the messages in the chat
messages = driver.find_elements(By.CSS_SELECTOR, '.message-in .copyable-text')

# Iterate over the messages and print their content
for message in messages:
    print(message.text)

# Close the browser
driver.quit()
