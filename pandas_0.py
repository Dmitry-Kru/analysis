import pandas as pd
print('Задание 1')
df = pd.read_csv('Submission.csv')
print(df.head(5), end='\n---------------*---------------\n')
print(df.info(), end='\n---------------*---------------\n')
print(df.describe(), end='\n---------------*---------------\n')

print('Задание 2')
print(pd.read_csv('dz.csv').groupby('City')['Salary'].mean())