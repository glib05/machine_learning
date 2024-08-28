#4
import pandas as pd

def do_series(df:pd.DataFrame):
    print('-----------------Створення Series з індексами за замовчуванням--------------------')
    print(df.head())

    print('-----------------Звернення до елементів Series--------------------\n'
          '                     (Звернення до колонки)')
    print(df['у тому числі'].head())

    print('-----------------Обчислення описових статистик для Series--------------------')
    saldo = df["Unnamed: 7"]
    mean = saldo.mean()
    print("mean", mean)
    mode = saldo.mode()
    print("mode", mode if mode.size < saldo.size else "no mode")
    min = saldo.min()
    print("min", min)
    max = saldo.max()
    print("max", max)
    std = saldo.std()
    print("std", std)

    print('-----------------Створення колекції Series з нестандартними індексами--------------------')
    df.index = [df["у тому числі"]]
    df = pd.DataFrame(df.iloc[:, 1:])
    df.columns = ['експ. тис. дол.', 'експ. у % до 9 міс.', 'експ. у % до заг.',
                  'імп. тис. дол.', 'імп. у % до 9 міс.', 'імп. у % до заг.',
                  'сальдо', 'region']
    print(df.head())

    print('-----------------Інші дії--------------------')
    print('Тип даних: ',df.dtypes)
    print('\nПовернення базової колекції:\n',df.values,'\n\n\n')

def do_dataframe(df:pd.DataFrame,num_of_cloumn:int,num_of_row_start:int,num_of_row_end:int):
    print('-----------------Зернення до колонки--------------------')
    print(df[f'Unnamed: {num_of_cloumn}'])
    df=df.rename(columns={'Unnamed: 1':'|у тому числі|',
                          'Unnamed: 2':'|експорт, тис USD|',
                          'Unnamed: 3':'|експорт у % до 2022|',
                          'Unnamed: 4':'|експорт у % до загального|', 
                          'Unnamed: 5':'|імпорт, тис USD|',
                          'Unnamed: 6':'|імпорт у % до 2022|',
                          'Unnamed: 7':'|імпорт % до загального|'})
    print('------------------Звернення до стовпців-----------------------')
    print(df.iloc[num_of_row_start])
    print('------------------Вібір підмножини-----------------------')
    print(df.iloc[num_of_row_start:num_of_row_end])
    print('------------------Логічне індексування-----------------------')
    print(df[df>=45])
    print('------------------Звернення до конкретного осередку[4,5]-----------------------')
    print(df.iat[4,5])
    print('------------------Описова статистика-----------------------')
    print(df.describe())
    print('------------------Траноспонування-----------------------')
    print(df.T)
    print('------------------Сортування рядків за індексами (спадання)-----------------------')
    print(df.sort_index(ascending=False))
    print('------------------Сортування стовпців за індексами (спадання)-----------------------')
    print(df.sort_index(ascending=False,axis=1))
