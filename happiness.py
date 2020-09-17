import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import polyfit
import seaborn as sns
from scipy.stats import linregress

df = pd.read_excel (r'./Chapter2OnlineData.xls')
sns.set()
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

# print(df.head())
# print(df.columns.values)
# print(df.describe())

# print('United States Happiness')
# print(df.loc[df['Country name'] == 'United States']['Life Ladder'].head(13))
# print('Canada Happiness')
# print(df.loc[df['Country name'] == 'Canada']['Life Ladder'].head(13))
# print('Australia Happiness')
# print(df.loc[df['Country name'] == 'Australia']['Life Ladder'].head(13))
# print('United Kingdom Happiness')
# print(df.loc[df['Country name'] == 'United Kingdom']['Life Ladder'].head(13))
# print('New Zealand Happiness')
# print(df.loc[df['Country name'] == 'New Zealand']['Life Ladder'].head(13)) 
years_extended = np.arange(2018, 2029, 1)
Country = df.loc[df['Country name'] == 'United States']['Life Ladder']
Year = df.loc[df['Country name'] == 'United States']['Year']
 #transforms list into a 2d matrix to fit into the numpy plot
# print(Country)
# print(Year)

slope, intercept, r_value, p_value, std_err = linregress(Year, Country)
line = [slope*xi + intercept for xi in years_extended]
plt.plot(years_extended, line, color = 'orange', label="Fitting Line", linewidth=1)
plt.scatter(Year, Country, s = 5, marker = '.', label="Sample Point", color = 'dodgerblue')
plt.xticks(range(2006, 2030, 2))
b, m = polyfit(Year, Country, 1)

Year = Year.values.reshape(-1, 1)

plt.plot(Year, Country, '.')
plt.plot(Year, Country, Year, b + m * Year, '-')
plt.show()

regr = linear_model.LinearRegression()
regr.fit(Year, Country)
# print(regr.coef_[0]) #slope

y_predict = regr.predict(Year)
print(y_predict)

X_future = np.array(range(2019, 2045))
X_future = X_future.reshape(-1, 1)

# future_predict = regr.predict(X_future)
# plt.plot(X_future, future_predict)
# plt.show()