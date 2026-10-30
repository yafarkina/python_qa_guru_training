import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

lst_user_pos = [
    {"full_name": "Михаил Салтыков-Щедрин",
     "email": "saltikov-shedrin@example.com",
     "current_address": "Киров, Ленина ул., 93",
     "permanent_address": "Рязань, ул. Свободы, 49"
     },
    {"full_name": "Ян У",
     "email": "u@example.com",
     "current_address": "г. Уфа, ул. Заречная, 16",
     "permanent_address": "г. Пермь, ул. Советская, 35"
     },
    {"full_name": "Пантелеймон Христорождественский",
     "email": "Khristorozhdestvenskiy@example.com",
     "current_address": "г. Красноярск, ул. Маяковского, 37",
     "permanent_address": "г. Москва, ул. Кирова, 2"
     },
]

lst_user_neg = [
    {"full_name": " ",
     "email": " ",
     "current_address": " ",
     "permanent_address": " "
     },
    {"full_name": " ",
     "email": "@example.com",
     "current_address": " ",
     "permanent_address": " "
     },
    {"full_name": " ",
     "email": "Khristorozhdestvenskiy@",
     "current_address": " ",
     "permanent_address": " "
     },
]
# Первый шаг - выделение каждого теста в отдельную функцию и ее последующий вызов
def open_page(wd: WebDriver):
    wd.get("https://qa-guru.github.io/one-page-form/text-box.html")
    wd.maximize_window()


def submit_button_click(wd: WebDriver):
    submit_button = wd.find_element(By.ID, "submit")
    submit_button.click()


def change_field_value(fild_name: str, fild_value: str, wd: WebDriver):
    wd.find_element(By.ID, fild_name).clear()
    wd.find_element(By.ID, fild_name).send_keys(fild_value)


def fill_form_text_box(name: str, email: str, current_address: str, permanent_address: str, wd: WebDriver):
    change_field_value("userName", name, wd)
    change_field_value("userEmail", email, wd)
    change_field_value("currentAddress", current_address, wd)
    change_field_value("permanentAddress", permanent_address, wd)


def test_pos_check_field():
    print("Рефакторинг - итерация 1!")
    wd = webdriver.Chrome()

    try:
        open_page(wd)
        for item in lst_user_pos:
            fill_form_text_box(item['full_name'], item['email'], item['current_address'], item['permanent_address'], wd)
            submit_button_click(wd)
            time.sleep(5)  # Пауза, чтобы увидеть результат отправки
            result_box = wd.find_element(By.ID, "output")
            assert item['full_name'] in result_box.text
            assert item['email'] in result_box.text
            assert item['current_address'] in result_box.text
            assert item['permanent_address'] in result_box.text
            print(f"Тест успешно пройден для пользователя {item['full_name']} с почтой {item['email']}")

    finally:
        wd.quit()

def test_neg_check_field():
    print("Рефакторинг - итерация 1!")
    wd = webdriver.Chrome()

    try:
        open_page(wd)
        for item in lst_user_neg:
            fill_form_text_box(item['full_name'], item['email'], item['current_address'], item['permanent_address'], wd)
            submit_button_click(wd)
            time.sleep(5)  # Пауза, чтобы увидеть результат отправки
            result_box = wd.find_element(By.ID, "output")
           # assert item['full_name'] in result_box.text
           # assert item['email'] in result_box.text
          #  assert item['current_address'] in result_box.text
           # assert item['permanent_address'] in result_box.text
            print(result_box)
            print(f"Негативный тест")

    finally:
        wd.quit()

test_pos_check_field()
test_neg_check_field()