import sys

import numpy as np
import pandas as pd
import json
from c import countries, codes
from sklearn.decomposition import PCA

#: Load the dataset
file = "HotelCustomersDataset.csv"
path = "C:/Users/bilge.adam/PycharmProjects/pythonProject/"
df = pd.read_csv(path + file, sep=";")
df = df.drop(columns=["NameHash", "ID"])

#: Country lookup
df["Nationality"] = df["Nationality"].map( codes )
continents = {a["name"]: a["continent"] for a in countries}

#: Continent lookup
df["Continent"] = df["Nationality"].map( continents )

#: Drop Nationality
del df["Nationality"]
df = df[ df["Continent"] != "AN" ]

vc = df[ "DocIDHash" ].value_counts()
df["NofVisit"] = df[ "DocIDHash" ].map( vc )

#df.to_csv(path + "m6.csv", sep = ";", decimal = ",")

#: 0 - Remove non useful
del df["DocIDHash"]

#: 1 - Delete columns with very high sparsity
for c in df.select_dtypes(exclude = ["object"]):
	m = df[c].mean()
	u = df[c].nunique()
	if u == 2 and m < 0.001:
		del df[c]

#: 2 - Outliers
for c in df.select_dtypes(exclude = ["object"]):
	u = df[c].nunique()
	if u > 2:
		lb = df[c].mean() - 3 * df[c].std()
		ub = df[c].mean() + 3 * df[c].std()
		df = df[ (df[c] < ub) & (df[c] > lb) ]

#: 3 - Filling

#: 4 - Check the correlations
df.corr().to_csv("corr.csv", sep=";", decimal = ",")

#: 5 - Delete if there is only one VALUE
for c in df:
	u = df[c].nunique()
	if u == 1:
		del df[c]

#: 6 - Normalization
for c in df.select_dtypes(exclude = ["object"]):
	u = df[c].nunique()
	if u > 2:
		df[c] = (df[c] - df[c].mean()) / df[c].std()

#: 7 - Categoric variables
df = pd.get_dummies(df, columns = ["Continent"])
df = pd.get_dummies(df, columns = ["DistributionChannel"])
df = pd.get_dummies(df, columns = ["MarketSegment"])

#: 8 - Dim red
print(df.shape)
from sklearn.manifold import TSNE

df = df.sample(n= 5000)

pca = PCA(n_components=20)
pca.fit(df)

# list(pca.explained_variance_ratio_)

def euclidean( a, b, w ):
	d = 0
	for i in range(len(a)):
		d += np.power(a[i] - b[i], 2) * w[i]
	return np.sqrt(d)


"""
pca_tranformed = TSNE(n_components=2, learning_rate='auto',init='random', perplexity=3).fit_transform(df)

import matplotlib.pyplot as plt

plt.scatter( pca_tranformed[:,0], pca_tranformed[:,1])
plt.show()

df.to_csv("m6.csv", sep = ";", decimal = ",")
"""


"""
changes = {}
for v in value_counts:
	da = df[ df["NameHash"] == v ]

	for c in df:
		unique = list(da[c].unique())
		if len(unique) > 1:
			if c not in changes:
				changes[c] = 0
			changes[c] += 1
			#print("değişiyor", c, v, unique)


print(changes)


print(df["DocIDHash"].nunique(), len(df))
value_counts = df["DocIDHash"].value_counts().to_dict()
value_counts = {d[0]:d[1] for d in value_counts.items() if d[1] > 1}
print(value_counts)



changes = {}
for v in vc:
	da = df[ df["DocIDHash"] == v ]

	for c in df:
		unique = list(da[c].unique())
		if len(unique) > 1:
			if c not in changes:
				changes[c] = 0
			changes[c] += 1

			if c == "Age":
				print(unique)



print(changes)

"""


