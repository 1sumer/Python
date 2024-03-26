import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew
from scipy.stats import kurtosis
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler

df = pd.read_excel(r"C:\Users\Admin\OneDrive\Documents\Python\Workbook\Regression\cars.xls")

scale = StandardScaler()
X = df[['Mileage', 'Cylinder', 'Liter', 'Leather']]
Y = df['Price']
X[['Mileage', 'Cylinder', 'Liter', 'Leather']] = scale.fit_transform(X[['Mileage', 'Cylinder', 'Liter', 'Leather']].to_numpy())
print(X)
est = sm.OLS(Y, X).fit()
est.summary()
print(est)

Y.groupby(df.Mileage).mean()
Z = [Y.groupby(df.Mileage).mean(), Y.groupby(df.Cylinder).mean(), Y.groupby(df.Liter).mean()]
print(Z)

Y.groupby(df.Mileage).var()
P = [Y.groupby(df.Mileage).var(), Y.groupby(df.Cylinder).var(), Y.groupby(df.Liter).var()]
print(P)

Y.groupby(df.Mileage).std()
Q = [Y.groupby(df.Mileage).std(), Y.groupby(df.Cylinder).std(), Y.groupby(df.Liter).std()]
print(Q)

A = skew(df['Mileage'], axis=0, bias=True)
print(A)
B = kurtosis(df['Mileage'], axis=0, bias=True)
print(B)

plt.plot(X, Y)
plt.show()

data = df[['Mileage', 'Price']]
plt.boxplot(data)
plt.show()