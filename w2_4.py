import sys
from matplotlib.pyplot import imshow #: will be used to display images
import matplotlib.pyplot  as plt
import numpy as np

MODE = 2


"""
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
"""
cols = ["original"]
for i in range(cluster_size):
	cols.append("c"+str(i))
da = pd.DataFrame(columns = cols)

for i in range(10):# range(int(len(values) / frame_size - 1)):
	frame = values[i*frame_size:(i+1)*frame_size]
	avg = sum(frame) / frame_size
	frame = [k / avg for k in frame]

	similarities = [ frame ]
	for c in range(cluster_size):
		correl = np.corrcoef(kmeans.cluster_centers_[c], frame)[0][1]
		similarities.append( correl )

	da.loc[len(da)] = similarities


da.to_csv("w2_4.csv", sep = ";", decimal=",")

"""

if MODE == 1:
	import numpy as np
	from PIL import Image, ImageFilter
	mypath = "C:/Users/bilge.adam/Downloads/archive (4)/Padded_imgs/"

	from os import listdir
	from os.path import isfile, join

	bigs = []

	tankclasses = ["2S1","BRDM_2","BTR_60","D7","SLICY","T62","ZIL131","ZSU_23_4"]
	for di in range(len(tankclasses)):
		d = tankclasses[di]
		tt = mypath + d + "/"
		onlyfiles = [f for f in listdir(tt) if isfile(join(tt, f))]
		for f in onlyfiles:
			if f.endswith(".JPG"):
				im = Image.open(tt + f)
				im = im.convert('L')
				imgArray = np.array(im)
				imgArray = np.ndarray.flatten(imgArray)
				imgArray = list(imgArray)
				imgArray = [str(round(q / 255.0, 3)) for q in imgArray]
				print(f, imgArray.shape)
				imgArray = " ".join(imgArray)

				s = f + " " + str(di+1) + "\n"
				s = s + imgArray + "\n"
				bigs.append(s)

	with open("C:/Users/bilge.adam/Downloads/som_demo/bin/tanks.txt", 'w') as f:
		for s in bigs:
			f.write(s)
	#grncol1  2
	#0.01 1.00 0.0
elif MODE == 2:

	import sys

	from PIL import Image, ImageFilter
	mypath = "C:/Users/bilge.adam/Downloads/som_demo/bin/tanks_1.som"

	with open(mypath) as f:
		lines = f.readlines()


	clusters = {}
	lastName = None
	offset = 4096 + 4 + 1 + 5 + 1 + 1
	buffer = []
	for i in range(len(lines)):
		if i > offset:
			l = lines[i].strip()
			if " " in l:
				if lastName != None:
					buffer = np.array(buffer)
					buffer = buffer.reshape(64, -1, order='C')
					clusters[lastName] = buffer

				buffer = []
				lastName = l
			else:
				if l != "":
					buffer.append( float( l ) * 255 )


	buffer = np.array(buffer)
	buffer = buffer.reshape(64, -1, order='C')
	clusters[lastName] = buffer



	print(clusters)

	for c in clusters:
		image = Image.fromarray(clusters[c].astype('uint8'), 'L')
		image.save("output/" + c + ".png")
		#imshow(np.asarray(image))
		#plt.show()


