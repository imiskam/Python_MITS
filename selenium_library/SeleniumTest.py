# Документация - https://www.selenium.dev/documentation/

# Установка пакета selenium через pip
# pip install selenium
# Импорт пакета WebDriver из библиотеки Selenium
from selenium import webdriver
# Импорт модуля By для поиска веб-элементов по определенным значениям
from selenium.webdriver.common.by import By
# Импорт модуля Time для работы с задержками
import time


def test_login():
    # С помощью метода find_element() найти страницу Form Authentication (текст ссылки) и кликнуть по ней
    driver.find_element(By.LINK_TEXT, "Form Authentication").click()
    # Найти идентификатор логина
    username_field = driver.find_element(By.ID, "username")
    # Найти идентификатор пароля
    password_field = driver.find_element(By.ID, "password")
    # Найти путь кнопки "Login" по XPath
    """
    Xpath - это язык запросов к элементам xml или xhtml документа. 
    Xpath является декларативным языком запросов. 
    Чтобы получить интересующие данные, необходимо всего лишь создать запрос, описывающий эти данные.
    Структура Xpath: //tag[@attribute='value'] 
    """
    login_button = driver.find_element(By.XPATH, "//*[@type='submit']")
    # Ввести данные в поле Username
    username_field.send_keys("tomsmith")
    # Ввести данные в поле Password
    password_field.send_keys("SuperSecretPassword!")
    # Поставить задержку 5 секунд
    time.sleep(5)
    # Нажать на кнопку "Login"
    login_button.click()

    # Проверки
    expected_login_message = "You logged into a secure area!"  # ожидаемый результат
    actual_login_message = driver.find_element(By.XPATH, "//div[@class='flash success']").text  # фактический рез-т
    assert expected_login_message in actual_login_message, \
        f"Expected '{expected_login_message}' text but found '{actual_login_message}'"
    driver.save_screenshot("login_result.png")  # метод save_screenshot сохраняет скриншот с заданным именем
    time.sleep(5)
    print("Login Test successfully completed!")


def test_logout():
    # Найти путь кнопки "Logout"
    logout_button = driver.find_element(By.XPATH, "//a[@class='button secondary radius']")
    # Кликнуть по кнопке Logout
    logout_button.click()

    # Проверки
    expected_logout_message = "You logged out of the secure area!"
    actual_logout_message = driver.find_element(By.XPATH, "//div[@class='flash success']").text
    assert expected_logout_message in actual_logout_message, \
        f"Expected '{expected_logout_message}' text but found '{actual_logout_message}'"
    driver.save_screenshot("logout_result.png")
    time.sleep(5)
    print("Logout Test successfully completed!")


# Инициализация драйвера и установка пути его исполнения
# driver = webdriver.Chrome() --> для Chrome
# driver = webdriver.Firefox() --> для Firefox
# driver = webdriver.Safari() --> для Safari
# Скачать chrome webdriver.exe для вашей версии Chrome и прописать путь к этому файлу
driver = webdriver.Chrome(executable_path="/selenium_library/chromedriver.exe")

url = "https://the-internet.herokuapp.com/"  # инициализация адреса ресурса
driver.get(url)  # метод get открывает браузер и загружает веб-страницу в текущей сессии
driver.maximize_window()  # метод maximize_window раскрывает окно браузера на полный экран

# Автотест для входа в аккаунт
test_login()
# Автотест для выхода из аккаунта
test_logout()

# Закрыть браузер после прохождения тестов
driver.quit()














"""
Задача для отработки (только с помощью методов Selenium!):
1. Открыть ресурс - https://21vek.by
2. Развернуть на полный экран окно браузера
3. Найти через поиск любой товар на ваш выбор и открыть страницу с ним
4. Добавить товар в корзину
5. Открыть корзину
6. Проверить, что товар действительно находится в корзине (сделать скриншот или использовать assert)
"""