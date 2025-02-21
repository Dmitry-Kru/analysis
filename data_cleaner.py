import csv

# Открываем исходный файл для чтения
with open("divans_prices.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # Пропускаем заголовок

    # Обрабатываем данные
    cleaned_data = []
    for row in reader:
        # Объединяем все элементы строки в одну строку
        combined_row = "".join(row)
        # Убираем все символы, кроме цифр
        digits_only = "".join([char for char in combined_row if char.isdigit()])
        # Преобразуем в int и добавляем в список
        cleaned_data.append([int(digits_only)])

# Сохраняем обработанные данные в новый CSV-файл
with open("cleaned_divans_prices.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Цена"])  # Заголовок столбца
    writer.writerows(cleaned_data)  # Записываем данные

print("Данные успешно обработаны и сохранены в cleaned_divans_prices.csv")