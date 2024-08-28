import pandas as pd
import statistics as s
import matplotlib.pyplot as plt

#1
def read_xlsx(name:str):
    return pd.read_excel(name)

df = read_xlsx("stat.xlsx")

print('*****************Зчитані дані про радіаційні викиди АЕС України********************')
print(df)

volume = df['volume'].dropna(how='all')
print("\nОб'єм:\n", volume)

year_volume = df.groupby('year')['volume'].sum().reset_index()
station_volume = df.groupby('station')['volume'].mean().reset_index()

#2
def make_statistics(df:pd.DataFrame):
    df.dropna(how='all')
    mean = df.mean()
    mode = df.mode() if df.mode().size < df.size else "no mode"
    median = s.median(sorted(volume))
    disp = s.pvariance(volume)
    std = s.pstdev(volume)
    return {"mean":mean, "mode":mode, "median":median, "disp":disp, "std":std}

def print_statistics(df:pd.DataFrame):
    stat = make_statistics(df)
    print("Мат. сподівання", stat['mean'])
    print("Мода", stat['mode'])
    print("Медіана",stat['median'])
    print("Дисперсія",stat['disp'])
    print("Станд. відхилення",stat['std'])

print('*****************Статистика по об`єму********************')
print_statistics(volume)

#3
plt.subplot(1, 2, 1)
plt.bar(year_volume['year'], year_volume['volume'], color='green')
plt.xlabel('Рік')
plt.ylabel('Кількість викидів')
plt.title('Кількість викидів від усіх станцій по рокам')

plt.subplot(1, 2, 2)
plt.bar(station_volume['station'], station_volume['volume'], color='orange')
plt.xlabel('Станція')
plt.ylabel('Кількість викидів')
plt.title('Середня кількість викидів від станції за квартал')

plt.tight_layout()
plt.show()

# 4
print('\n****************************************************')
print('*****************Колекція Series********************')
print('****************************************************\n')

print('*****************Створення Series з індексами за замовчуванням********************')
print(df.head())

print('*****************Звернення до елементів Series********************\n'
      '                     (Звернення до колонки)')
print(df['station'].head())

print('*****************Обчислення описових статистик для Series********************')
print_statistics(volume)

print('*****************Створення колекції Series з нестандартними індексами********************')
df['concatenated'] = df['year'].astype(str) + '_' + df['quarter'].astype(str) + '_' + df['station']
df.index = [df['concatenated']]
df = pd.DataFrame(df.iloc[:, 3:16])
df.rename(columns={'irg':'something'}, inplace=True)
print(df.head())

print('*****************Інші дії********************')
print('Тип даних: ',df.dtypes)
print('\nПовернення базової колекції:\n',df.values,'\n\n\n')




print('\n*******************************************************')
print('*****************Колекція DataFrame********************')
print('*******************************************************\n')

print('*****************Зернення до колонки********************')
print(df['something'])

print('******************Звернення до рядка***********************')
print(df.loc['2018_1_ХАЕС'])

print('******************Вібір підмножини***********************')
print(df.loc[['2018_1_ХАЕС','2021_4_ХАЕС'], ['something','volume']])
print(df.iloc[9:14, 3:5])

print('******************Логічне індексування***********************')
print(df[df.iloc[:,6] >=0.5])

print('******************Звернення до конкретного осередку[4,5]***********************')
print(df.iat[4,5])

print('******************Описова статистика***********************')
print(df.describe())

print('******************Траноспонування***********************')
print(df.T)

print('******************Сортування рядків за значеннями поля something (зростання)***********************')
print(df.sort_values(by='something'))

print('******************Сортування стовпців за індексами (спадання)***********************')
print(df.sort_index(ascending=False,axis=1))
