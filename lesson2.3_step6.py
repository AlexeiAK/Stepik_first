from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)
    
    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    print(x)
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    

    # находим элемент, содержащий текст
    
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
  

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
  
  
finally:
    
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
