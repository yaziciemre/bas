import sys
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import pandas as pd


file = "marketing_campaign.csv"
df = pd.read_csv(file, sep = "\t")
del df["Response"]
del df["ID"]

del df["Recency"]
del df["AcceptedCmp3"]
del df["Complain"]



#df.to_csv("marketing_campaign2.csv", sep = ";", decimal = ",")


kmeans = KMeans(n_clusters=3,  n_init="auto")
x = df.select_dtypes(exclude = ["object"])
x = x.fillna(0)
pca = PCA(n_components=3)
pca.fit(x)
x = pca.transform(x)
x = pd.DataFrame(x)


print(x.columns)


for i in x:
	if x[i].nunique()  == 1:
		del x[i]



for i in x:
	x[i] = (x[i] - x[i].mean()) / x[i].std()

x = x.fillna(0)


kmeans.fit(x)
print( kmeans.cluster_centers_ )
from sklearn import metrics

print(metrics.silhouette_score(
	x,
	kmeans.labels_,
	metric="euclidean",
	sample_size=300,
))




clusters = pd.DataFrame(columns = list(x.columns))

for c in kmeans.cluster_centers_:
	clusters.loc[len(clusters)] = c

print(clusters)

x["cluster"] = kmeans.predict(x)
x.to_csv("w2_clusters.csv", sep = ";", decimal = ",")


analysis = pd.DataFrame( columns = ["Cluster", "Field", "Mean", "Std"] )

for i in x.groupby( "cluster" ):
	name = i[0]
	data = i[1]

	for c in data.select_dtypes(exclude = ["object"]):
		analysis.loc[ len(analysis) ] = [name, c, data[c].mean(), data[c].std()]


analysis.to_csv("analysis.csv", sep = ";", decimal = ",")


