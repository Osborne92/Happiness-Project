import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import polyfit
import seaborn as sns
from scipy.stats import linregress
import mpld3

df = pd.read_excel (r'./Chapter2OnlineData.xls')

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
Country = df.loc[df['Country name'] == 'Australia']['Life Ladder']
Year = df.loc[df['Country name'] == 'Australia']['Year']
 #transforms list into a 2d matrix to fit into the numpy plot
# print(Country)
# print(Year)

fig = plt.figure(figsize = (18,8))
slope, intercept, r_value, p_value, std_err = linregress(Year, Country)
line = [slope*xi + intercept for xi in years_extended]
plt.plot(years_extended, line, color = 'red', label="Fitting Line", linewidth=1)
plt.scatter(Year, Country, s = 5, marker = '.', label="Sample Point")
plt.xticks(range(2006, 2030, 2))
b, m = polyfit(Year, Country, 1)

Year = Year.values.reshape(-1, 1)

plt.xlabel('Year')
plt.ylabel('Happiness Rating')
plt.title('Happiness Projection')
plt.plot(Year, Country, '.', color = 'dodgerblue')
plt.plot(Year, Country, Year, b + m * Year, '-', color = 'dodgerblue')
plt.show()

html_str = mpld3.fig_to_html(fig)
Html_file= open("index.html","w")
Html_file.write(html_str)
Html_file.close()