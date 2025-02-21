import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('cleaned_divans_prices.csv')
average_price = data['Цена'].mean()
print(f"Средняя цена на диваны: {average_price:.2f} руб.")

plt.figure(figsize=(10, 6))
plt.hist(data['Цена'], bins=30, color='skyblue', edgecolor='black')
plt.axvline(average_price, color='red', linestyle='dashed', linewidth=2)
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена')
plt.ylabel('Количество')
plt.text(average_price + 1000, max(plt.ylim()) * 0.78,
         f'Средняя цена: \n   {average_price:.2f}', color='red')
plt.show()