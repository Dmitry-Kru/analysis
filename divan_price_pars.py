from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

driver = webdriver.Chrome()
url = "https://www.divan.ru/category/divany-i-kresla"
driver.get(url)
time.sleep(5)  # Ждем загрузки страницы

divans = driver.find_elements(By.CSS_SELECTOR, "div.WdR1o")

data = []

for item in divans:
    try:
        price = item.find_element(By.CSS_SELECTOR, "span.ui-LD-ZU.KIkOH").text
    except Exception as e:
        print(f"Ошибка при парсинге: {e}")
    data.append(price)
driver.quit()

# Сохраняем данные в CSV-файл
with open("divans_prices.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Цена"])  # Заголовки столбцов
    writer.writerows(data)  # Записываем данные

print("Данные успешно сохранены в divans_prices.csv")