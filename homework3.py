
import time
import csv
import numpy as np
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
link = "https://www.divan.ru/category/podushki"
driver.get(link)
time.sleep(5)

podushki = driver.find_elements(By.CSS_SELECTOR, '[data-testid="product-card"]')
print(f"{len(podushki)=}")

parsed_prices = []

for podushka in podushki:
    try:
        price = float(podushka.find_element(By.CSS_SELECTOR, '[itemprop="price"]').get_attribute('content'))
        parsed_prices.append(price)
    except Exception as e:
        print("Произошла ошибка при извлечении цены:", e)

driver.quit()

# Вычисление средней цены
average_price = np.mean(parsed_prices)
print(f"Средняя цена: {average_price:.2f}")

# Создание гистограммы
plt.figure(figsize=(10, 6))
plt.hist(parsed_prices, bins=20, edgecolor='black')
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена')
plt.ylabel('Количество')
plt.axvline(average_price, color='r', linestyle='dashed', linewidth=2, label=f'Средняя цена: {average_price:.2f}')
plt.legend()
plt.savefig('histogram_prices.png')
plt.show()

# Сохранение данных в CSV файл
with open("podushki_prices.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Цена'])
    writer.writerows([[price] for price in parsed_prices])

print("Цены сохранены в 'podushki_prices.csv'")
print("Гистограмма сохранена в 'histogram_prices.png'")