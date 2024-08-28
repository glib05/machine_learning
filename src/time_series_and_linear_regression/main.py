import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
import numpy as np

df = pd.read_csv('january.csv')

df.columns = ['Date', 'Temperature', 'Anomaly']
df.Date = df.Date.floordiv(100)

# 1
print('#######################Зчитані та трохи оброблені дані############################')
print(df)

# 2
regression = stats.linregress(x=df.Date, y=df.Temperature)

date = np.linspace(1895, 2018)
temperature = date * regression.slope + regression.intercept

sns.lineplot(x=date, y=temperature)
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.title('Регресійна пряма')
plt.grid(True)
plt.show()

# 3
temperature = lambda date: date * regression.slope + regression.intercept

print('\n\n#######################Прогнозована температрура############################')
for date in range(2019,2029):
    print(date,': ', temperature(date))

#4
print('\n\n#######################Оцінка температури до 1895############################')
for date in range(1885,1895):
    print(date,': ', temperature(date))

#5
sns.set_style('whitegrid')
plt.title('№5 regplot')
axes = sns.regplot(x=df.Date, y=df.Temperature)
plt.show()

#6
sns.set_style('whitegrid')
plt.title('№6 масштабування')
axes = sns.regplot(x=df.Date, y=df.Temperature)
axes.set_ylim(10, 90)
plt.show()

#7
print('\n\n#######################Порівняння############################')
for date in range(2019, 2024):
    print(f'-----------------------------------\n'
          f'Прогноз на {date} рік: {temperature(date)}\n'
          f'Реальне значення на {date} рік: {df[df["Date"] == date]["Temperature"].iloc[0]}')