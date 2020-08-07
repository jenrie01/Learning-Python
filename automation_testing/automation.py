from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()
chrome_browser.get(
    'https://www.seleniumeasy.com/test/basic-first-form-demo.html')

# print('Selenium Easy Demo' in chrome_browser.title)
assert 'Selenium Easy Demo' in chrome_browser.title
message_button = chrome_browser.find_element_by_class_name('btn-default')
print(message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source
user_message = chrome_browser.find_element_by_id('user-message')
user_button2 = chrome_browser.find_element_by_css_selector('#get-input > .btn')
print(user_button2)
user_message.clear()
user_message.send_keys('Testing input using send keys')

message_button.click()

output_message = chrome_browser.find_element_by_id('display')
assert 'Testing input using send keys' in output_message.text
print(output_message.get_attribute('innerHTML'))

# chrome_browser.close()
chrome_browser.quit()
