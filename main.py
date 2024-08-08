from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

# Инициализация драйвера
driver = webdriver.Chrome()

# URL страницы
url = 'https://www.divan.ru/kazan/category/svet'

# Открываем страницу
driver.get(url)

# Ждем загрузки страницы
time.sleep(10)

# Ищем элементы товаров
svets = driver.find_elements(By.CLASS_NAME, '_Ud0k')

time.sleep(5)

parser_data = []

for svet in svets:
    try:
        # Правильные селекторы для имени и цены
        name = svet.find_element(By.CSS_SELECTOR, 'div.lsooF span').text
        price = svet.find_element(By.CSS_SELECTOR, 'div.pY3d2 span').text
        url = svet.find_element(By.TAG_NAME, 'a').get_attribute('href')
    except Exception as e:
        print(f'Произошла ошибка: {e}')
        continue

    parser_data.append([name, price, url])

# Закрываем браузер
driver.quit()

# Сохранение данных в CSV файл
with open('data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Цена', 'Ссылка'])
    writer.writerows(parser_data)

print("Данные успешно сохранены в файл data.csv")
