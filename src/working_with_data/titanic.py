import pandas as pd
import matplotlib.pyplot as plt

# 8
titanic = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/carData/TitanicSurvival.csv')

# 9
titanic.columns = ['name', 'survived', 'sex', 'age', 'class']

print('*****************Зчитані дані********************')
print(titanic)

# 10
youngest = titanic.loc[titanic['age'].idxmin()]
eldest = titanic.loc[titanic['age'].idxmax()]
average = titanic['age'].mean()

first_class_women = titanic[(titanic['sex'] == 'female') & (titanic['class'] == '1st')].sort_values(by='name')
youngest_fcw = first_class_women.loc[first_class_women['age'].idxmin()]
eldest_fcw = first_class_women.loc[first_class_women['age'].idxmax()]
count_survived = first_class_women[first_class_women['survived'] == 'yes'].shape[0]

print('*****************youngest person********************')
print(youngest)
print('*****************eldest person********************')
print(eldest)
print('*****************average age********************')
print(average)
print('*****************women of 1st class********************')
print(first_class_women)
print('*****************youngest women of 1st class********************')
print(youngest_fcw)
print('*****************eldest women of 1st class********************')
print(eldest_fcw)
print('*****************quantity of survived women of 1st class********************')
print(count_survived)

#11
titanic.hist()
plt.xlabel("Вік пасажирів")
plt.ylabel("Частота")
plt.show()