import numpy as np
import sys

from sklearn.cluster import KMeans
import re
import pandas as pd
path = "household_power_consumption.txt"
df = pd.read_csv(path, sep = ";")
df.head(100000).to_csv("household_power_consumption.csv", sep = ";", decimal=",")
values = df["Global_active_power"].head(100000).values
print(df.columns)
print(df)
values = [float(s) for s in values if s != "?"]

cluster_size = 30
frame_size = 8
dataset = []

for i in range(len(values) - frame_size - 1):
	frame = values[i:i+frame_size]
	avg = sum(frame) / frame_size
	frame = [k/avg for k in frame]
	dataset.append( frame )

print(dataset[0:10])


kmeans = KMeans(n_clusters=cluster_size, n_init="auto")
kmeans.fit(dataset)
index = 0
import matplotlib.pyplot as plt
for c in kmeans.cluster_centers_:
	plt.cla()
	plt.clf()
	plt.plot(c)
	plt.savefig("figs/" + str(index) + ".png")
	index += 1
	#plt.show()



"""
plt.cla()
plt.clf()
plt.plot( kmeans.cluster_centers_[0] )
start = 0

frame = values[start:start+8]
avg = sum(frame) / frame_size
frame = [k / avg for k in frame]

plt.plot( frame )
plt.show()
"""


real = []
pred = []


for i in range(10):# range(int(len(values) / frame_size - 1)):
	frame = values[i*frame_size:(i+1)*frame_size]
	avg = sum(frame) / frame_size
	frame = [k / avg for k in frame]

	max_item = 0
	max_value = 0
	for c in range(cluster_size):
		correl = np.corrcoef(kmeans.cluster_centers_[c], frame)[0][1]
		if correl > max_value:
			max_value = correl
			max_item = c

	real.extend( frame )
	pred.extend( kmeans.cluster_centers_[max_item] )


error = [abs(real[i] - pred[i]) for i in range(len(real))]


xxx = np.corrcoef(pred, real)[0][1]
print("correl", xxx)

plt.clf()
plt.cla()
plt.plot(real, label="real")
plt.plot(pred, label="pred")
plt.plot(error, label="error")
plt.legend()
plt.show()