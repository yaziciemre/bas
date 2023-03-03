import matplotlib.pyplot as plt
import sys
from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import pickle
path = "C:/Users/bilge.adam/Desktop/Radar_Data/MAFAT RADAR Challenge - Training Set V1.pkl"
output = None
with open(path, 'rb') as data:
    output = pickle.load(data)

print(output.keys())

doppler_burst = output["doppler_burst"]
iq_sweep_burst = output["iq_sweep_burst"]
segment_id = output["segment_id"]

print(doppler_burst.shape)
print(iq_sweep_burst.shape)
print(segment_id.shape)

#print("birinci segment'in doppler", doppler_burst[0])
# print("birinci segment'in iq_sweep", iq_sweep_burst[0])


data = pd.DataFrame(columns = ['atım', 'bin', 'real', 'imag'])

for atım in range(32):
	for bin in range(128):
		r = iq_sweep_burst[0][bin][atım].real
		i = iq_sweep_burst[0][bin][atım].imag

		data.loc[len(data)] = [atım, bin, r, i]
data["genlik"] = np.sqrt(data["real"] * data["real"] + data["imag"] * data["imag"])

plt.hist(data["genlik"])
plt.show()

del data["real"]
del data["imag"]
#del data["atım"]
#del data["bin"]

#for c in data:
	#data[c] = (data[c] - data[c].min()) / (data[c].max() - data[c].min())
	#data[c] = (data[c] - data[c].mean()) / data[c].std()





upper = data["genlik"].quantile(0.75)
lower = data["genlik"].quantile(0.25)
iqr = upper - lower
ubound = upper + 1.0 * iqr
lbound = lower - 1.5 * iqr


data["isoutlier"] = data["genlik"] > ubound
data["isoutlier"] = data["isoutlier"].astype(int)

print("----------------------------------")
print("yüksek", data[data["genlik"] > ubound])
print("----------------------------------")
print("düşük", data[data["genlik"] < lbound])
print("----------------------------------")
data.to_csv("data.csv", sep = ";" , decimal = ",")


img = np.zeros( (128,32) )
for i in range(len(data)):
	row = data.iloc[i]
	y = int(row["atım"])
	x = int(row["bin"])
	v = row["isoutlier"]
	img[x,y] = v


data = data[ data["isoutlier"] == 1 ]
del data["isoutlier"]

del data["genlik"]
for c in data:
	data[c] = (data[c] - data[c].min()) / (data[c].max() - data[c].min())
	#data[c] = (data[c] - data[c].mean()) / data[c].std()

gm3 = GaussianMixture(n_components=3, random_state=0).fit(data)
gm2 = GaussianMixture(n_components=2, random_state=0).fit(data)
gm1 = GaussianMixture(n_components=1, random_state=0).fit(data)
print("gm3", gm3.means_)
print("gm2", gm2.means_)
print("gm1", gm1.means_)

from PIL import Image
from matplotlib import cm
#im = Image.fromarray(np.uint8(cm.gist_earth(img)*255))
im = Image.fromarray(np.uint8(cm.gist_earth(img)*255))
im.show()

sys.exit(1)
#print( iq_sweep_burst[0][0][0].real )
#print( iq_sweep_burst[0][0][0].imag )

gm3 = GaussianMixture(n_components=3, random_state=0).fit_predict(data)
gm2 = GaussianMixture(n_components=2, random_state=0).fit_predict(data)
gm1 = GaussianMixture(n_components=1, random_state=0).fit_predict(data)



from sklearn.mixture import GaussianMixture
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
ax1.scatter(data["genlik"], data["bin"], c=gm2)
ax2.scatter(data["genlik"], data["bin"], c=gm3)
plt.show()

"""
img = iq_sweep_burst[0] / 1000

from PIL import Image
from matplotlib import cm
#im = Image.fromarray(np.uint8(cm.gist_earth(img)*255))
im = Image.fromarray(np.uint8(cm.gist_earth(img)*255))
im.show()
"""
