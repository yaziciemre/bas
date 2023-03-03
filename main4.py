
import pandas as pd
path = "C:/Users/bilge.adam/PycharmProjects/pythonProject/"

df = pd.read_csv(path + "train.csv")
df = df.select_dtypes(exclude=["object"])
df = df[ ["Age", "Vintage", "Annual_Premium"] ]
print(df.columns)
print(df.describe())

# min max scaler: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html
#for c in df:
#	df[c] = (df[c] - df[c].min()) / (df[c].max() - df[c].min())

for c in df:
	df[c] = (df[c] - df[c].mean()) / df[c].std()

#(x - mean) / std



print(df.describe())

"""
                 Age        Vintage  Annual_Premium
mean       38.822584     154.347397    30564.389581
std        15.511611      83.671304    17213.155057
min        20.000000      10.000000     2630.000000
25%        25.000000      82.000000    24405.000000
50%        36.000000     154.000000    31669.000000
75%        49.000000     227.000000    39400.000000
max        85.000000     299.000000   540165.000000
"""


