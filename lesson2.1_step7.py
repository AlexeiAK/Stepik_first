from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element_by_id("treasure")
    treasure_valuex = x_element.get_attribute("valuex")
    print(treasure_valuex)
    x = treasure_valuex
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    option1 = browser.find_element_by_id('robotCheckbox')
    option1.click()
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
  

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()