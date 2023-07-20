from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def test_eight_components():
    driver = webdriver.Chrome()

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    title = driver.title
    assert title == "Web form"

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    password_input = driver.find_element(by=By.NAME, value="my-password")
    textarea = driver.find_element(by=By.NAME, value="my-textarea")
    default_checkbox = driver.find_element(by=By.ID, value="my-check-2")
    default_radio = driver.find_element(by=By.ID, value="my-radio-2")
    dropdown = Select(driver.find_element(by=By.NAME, value="my-select"))
    my_color = driver.find_element(by=By.NAME, value="my-colors")

    text_box.send_keys("Selenium")
    time.sleep(1)
    dropdown.select_by_value("2")
    time.sleep(1)
    password_input.send_keys("pa$$word")
    time.sleep(1)
    textarea.send_keys("This is for testing")
    time.sleep(1)
    default_checkbox.click()
    time.sleep(1)
    default_radio.click()
    time.sleep(1)
    my_color.send_keys("#008080")
    time.sleep(1)

    submit_button.click()
    time.sleep(1)

    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"

    time.sleep(3)

    driver.quit()

if __name__ == '__main__':
    test_eight_components()