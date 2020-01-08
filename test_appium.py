import os

from selenium.webdriver.remote import webdriver

path_to_current_file = os.path.realpath(__file__)
print('path to the current file:', path_to_current_file)

path_to_current_folder = os.path.dirname(path_to_current_file)
print('path to the current folder:', path_to_current_folder)

folder_inside_current_folder = os.path.dirname(os.path.join(path_to_current_folder, 'app/'))
print('path to the custom folder:', folder_inside_current_folder)

from appium import webdriver
desired_caps = {
"platformName": "iOS",
"platformVersion": "12.4",
"deviceName": "iPhone 8",
"app": folder_inside_current_folder+"/Calc.app"
}


def test_sum_of_two_integers():
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.find_element_by_name('9').click()
    driver.find_element_by_name('+').click()
    driver.find_element_by_name('1').click()
    driver.find_element_by_name('=').click()
    numbers_field = driver.find_element_by_xpath('//XCUIElementTypeStaticText')
    assert float(numbers_field.text) == 10.0
    driver.quit()