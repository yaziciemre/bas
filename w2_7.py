import math
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

path = "C:/Users/bilge.adam/Desktop/Radar_Data/MAFAT RADAR Challenge - Training Set V1.csv"

def load_csv_metadata(file_path):
  """
  Reads csv as pandas DataFrame (only Metadata).

  Arguments:
    file_path -- {str} -- path to csv metadata file

  Returns:
    Pandas DataFarme
  """
  path = os.path.join(file_path)
  with open(path, 'rb') as data:
    output = pd.read_csv(data)
  return output

print(load_csv_metadata(path))

"""
import scipy.io
mat = scipy.io.loadmat('file.mat')


from scipy.io import savemat
import numpy as np
a = np.arange(20)
mdic = {"a": a, "label": "experiment"}
mdic
{'a': array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
    17, 18, 19]),
'label': 'experiment'}
savemat("matlab_matrix.mat", mdic)


"""

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

print("birinci segment'in doppler", doppler_burst[0])
print("birinci segment'in iq_sweep", iq_sweep_burst[0])

print( iq_sweep_burst[0][0][0].real )
print( iq_sweep_burst[0][0][0].imag )

import cmath
x = 5
y = 3
z = complex(x, y);
#print("The real part of complex number is : ", end="")
#print(z.real)
#print(z.imag)


def complexToReal( c ):
	return math.sqrt(c.real * c.real + c.imag * c.imag)


data = []
for i in range(6656):
	vectori = iq_sweep_burst[i].reshape(4096, -1, order='C')
	vectori = [complexToReal(q[0]) for q in vectori]
	data.append(vectori)

data = np.array(data)
data = pd.DataFrame(data)
from sklearn.decomposition import PCA
pca = PCA(n_components=100)
pca.fit( data )
print(pca.explained_variance_ratio_)
print(pca.explained_variance_ratio_.cumsum())

# 4096





