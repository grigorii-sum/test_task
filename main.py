import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By


LOGIN = ""
PASSWORD = ""


if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1280,721")
    browser = webdriver.Chrome(options=options)

    base_link = "https://www.gosuslugi.ru/"
    browser.get(base_link)
    time.sleep(3)

    lk_button = browser.find_element(By.CSS_SELECTOR, "a.lk-enter")
    lk_button.click()
    time.sleep(3)

    login_input = browser.find_element(By.CSS_SELECTOR, "input#login")
    login_input.send_keys(LOGIN)
    password_input = browser.find_element(By.CSS_SELECTOR, "input#password")
    password_input.send_keys(PASSWORD)
    login_button = browser.find_element(By.CSS_SELECTOR, "[data-bind='click: loginByPwd']")
    login_button.click()
    time.sleep(3)

    document_page = browser.find_element(By.LINK_TEXT, "Документы и данные")
    document_page.click()
    time.sleep(3)

    series_and_number_of_passport = browser.find_element(By.CSS_SELECTOR, "a > div.content > lk-doc-card-row:nth-child(1) > h5")
    series_and_number_of_passport = series_and_number_of_passport.text
    passport_issued = browser.find_element(By.CSS_SELECTOR, "lk-doc-card-row:nth-child(2) > div > div.text-plain.mt-4")
    passport_issued = passport_issued.text
    department_code = browser.find_element(By.CSS_SELECTOR, "lk-doc-card-row:nth-child(3) > div > div.text-plain.mt-4")
    department_code = department_code.text
    date_of_issue = browser.find_element(By.CSS_SELECTOR, "lk-doc-card-row:nth-child(4) > div > div.text-plain.mt-4")
    date_of_issue = date_of_issue.text

    browser.quit()

    os.mkdir('new_folder')

    file_with_passport_data = open("new_folder/passport_data", "w+")
    file_with_passport_data.write("---ПАСПОРТ ГРАЖДАНИНА РФ---\nСерия и номер паспорта: "
                                  + series_and_number_of_passport
                                  + "\nВыдан: "
                                  + passport_issued
                                  + "\nКод подразделения: "
                                  + department_code
                                  + "\nДата выдачи: "
                                  + date_of_issue)
    file_with_passport_data.close()
