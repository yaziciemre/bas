import sys
import numpy as np
# import pandas
import pandas as pd
# from pandas import *, kullanmayalım
from pandas import read_csv, read_sql
pd.set_option('display.max_columns', 6)


def f2c(f):
	a = 3
	return (f-32) / 1.8
a = 4

if a == 4:
	print("test")
print("test2")
"""
df = read_csv("C:/Users/bilge.adam/Downloads/Radar_Traffic_Counts.csv/Radar_Traffic_Counts.csv")
df = df.sample(n = 100000)
df.to_csv("C:/Users/bilge.adam/Downloads/Radar_Traffic_Counts.csv/Radar_Traffic_Counts_small.csv")

sys.exit(1)
"""
df = read_csv("C:/Users/bilge.adam/Downloads/Radar_Traffic_Counts.csv/Radar_Traffic_Counts_small.csv")
#ISO-8859-1
#Windows-1254
#utf-8

#: Türüne bakalım
print(type(df))
print(df)
print(df.columns)

#: Bir kolonu seçmek için
print(df["location_latitude"])

liste = ["a", "b", "c"]

#: Birden fazla kolonu seçmek için
print(df[ ["location_latitude", "location_longitude"]  ])

#: Tüm kolonlar = df

#: Türlerini göster
print(df.dtypes)

#: Sadece integer olan kolonları göster
print( df.select_dtypes(include = ["int64"]) )

#: İnteger olmayanları seç
print( df.select_dtypes(exclude = ["int64"]) )

liste = ["a", "b", "c", "d"]
#liste = [i.upper() for i in liste if i != "d"]
liste = [i for i in liste if i != "d"]

liste = [i for i in df.columns if i != "Unnamed: 0"]
print(liste)

df = df[ liste ]
print( df )

#: baştan 11 tane göster
print(df.head(11))
#: Sondan 500 göster
print(df.tail(500))


#: 10 ile 20 inci satır arasını göster
print(df[10:20])

#: bastan, 20 inci satır arasını göster
print(df[:20])

# 20 inci satırdan sonra  -- ilk 20 tanesini egale ettik
print(df[20:])

# 500 den başla, sondan 1200 öncesine kadar
print(df[500:-1200])
print(df[500:-1])

print( df[ df.columns[1:3] ] )

#: sadece 1 satırı al
print( df.iloc[34] )


# ETL (extract transform load)

"""
df = [
	["2021 blk", 30324, 14910234, 2018, 1, 23],
	["CAPITAL", 30324, 14910234, 2018, 1, 23],
	["2021 blk", 30324, 14910234, 2018, 1, 23],
] 

df = [
	["xxx", "xx", "qweqwerw"],
	[30.123424, 12341242. 12341234 234 241 123]

]
"""
"""
Unnamed 0:	location_name	location_latitude	location_longitude	Year	Month	Day	Day of Week	Hour	Minute	Time Bin	Direction	Volume
0	2021 BLK KINNEY AVE (NW 300ft NW of Lamar)	30.248.691	-97.770.409	2018	1	23	2	22	15	22:15	None	4
1	 CAPITAL OF TEXAS HWY / LAKEWOOD DR	303.716.736	-977.856.598	2017	12	16	6	19	45	19:45	NB	103
2	400 BLK AZIE MORTON RD (South of Barton Springs Rd)	30.264.245	-97.765.802	2018	1	23	2	21	45	21:45	SB	44
3	400 BLK AZIE MORTON RD (South of Barton Springs Rd)	30.264.245	-97.765.802	2018	1	23	2	21	45	21:45	NB	13
4	2021 BLK KINNEY AVE (NW 300ft NW of Lamar)	30.248.691	-97.770.409	2018	1	23	2	22	15	22:15	None	0
"""
print("-------------------------------------")
print(df.info())


print(df.values)
print(df.size)
print(df.shape)


print(df["Volume"] > 4)

print(df[   (df["Volume"] > 4) & (df["Volume"]  < 100)  & (df["Direction"].isin(["NB", "SB"])) ]  )
print(df.query("Volume > 4"))


for c in df.groupby('location_name'):
	print(c[0])
	print(c[1])

#: gruplama fonksiyonu - pivot

print("--------x------------")

print( df["location_name"].value_counts() )


df = df.rename( columns = {"location_name": "loc"} )

print(df[   ["Hour", "Minute", "Time Bin"]  ]  )

# del df["Time Bin"]
df = df.drop( columns = ["Time Bin"] )
print(df.columns)

# tail (sondan N item)

# Örneklem almak
d1 = df.sample( n = 100)
d2 = df.sample( frac = 0.30 )
d3 = df.sample( n = len(df) )



print(df.describe())
print(df.corr().to_csv("corr.csv", sep=";", decimal=","))



print(df.columns)


def hesapla(x: int, y: int) -> int:

	def subhesapla(a: int) -> int:
		return a * x

	q =  x + y + subhesapla(y)
	return q

i:float = 0
i:float = 0.0


i = 0
i = 0.0



fahr2celc = lambda x: (x-32) / 1.8

def fahr2celc_2(x):
	return (x-32) / 1.8

print(fahr2celc(20))

"""
Index(['loc', 'location_latitude', 'location_longitude', 'Year', 'Month',
       'Day', 'Day of Week', 'Hour', 'Minute', 'Direction', 'Volume'],
      dtype='object')
"""

print( df["Volume"].mean() )
print( df["Volume"].max() )
print( df["Volume"].min() )
print( df["Volume"].values )

print( df["Volume"].std() )


for c in df.groupby( 'loc' ):
	groupname = c[0]
	groupdata = c[1]
	print(groupname, groupdata["Volume"].std())


# Excel = dataframe = tablo = matrix
# Kolon = Series df["Volume"] = Vector = Column = Sütun


a = df[  df["loc"] == " CAPITAL OF TEXAS HWY / CEDAR ST" ]
print(a)


# data type
print( df["Volume"].dtype )

print( df["Volume"].median() )
print( df["Volume"].quantile(0.75) )
print( df["Volume"].quantile(0.25) )


print( df["Volume"].quantile(0.99) )
print( df["Volume"].quantile(0.01) )


print( df["Volume"].mode() )

# filtrele
# outlier eliminasyon
print( df[  (df["Volume"] < df["Volume"].quantile(0.99)) & (df["Volume"] > df["Volume"].quantile(0.01))  ] )

ub = df["Volume"].mean() + 3 * df["Volume"].std()
lb = df["Volume"].mean() - 3 * df["Volume"].std()

# outlier eliminasyon 2
df[ (df["Volume"] > lb) & (df["Volume"] < ub) ]


print(df["Volume"].skew())
print(df["Volume"].kurt())

import matplotlib.pyplot as plt
plt.hist(df["Volume"])

# 3. outlier
q3 = df["Volume"].quantile(0.75)
q1 = df["Volume"].quantile(0.25)
iqr = 1.5 * (q3-q1)

upper_bound = q3 + iqr
lower_bound = q1 - iqr

print( len(df[df["Volume"]<lower_bound]) )
print( len(df[df["Volume"]>upper_bound]) )
#plt.show()


df["Volume0MıDeğilMi"] = 0
df["Volume0MıDeğilMi"] = (df["Volume"] != 0)
df["Volume0MıDeğilMi"] = df["Volume0MıDeğilMi"].astype(int)

df["Volume0MıDeğilMi2"] = df["Volume"].astype(bool)
df["Volume0MıDeğilMi2"] = df["Volume0MıDeğilMi2"].astype(int)

df["Volume0MıDeğilMi3"] = np.sign(df["Volume"])

def sign(value):
	if value == 0: return 0
	return 1

# fahr2celc = lambda x: (x-32) / 1.8

df["Volume0MıDeğilMi4"] = df["Volume"].apply( sign )
df["Volume0MıDeğilMi5"] = df["Volume"].apply( lambda value: sign(value) )
df["Volume0MıDeğilMi6"] = df["Volume"].apply( lambda value: 0 if value == 0 else 1 )

print(df)


s = " LAMAR BLVD / SANDRA MURAIDA WAY (Lamar Bridge)"
print(s.strip())
# s = "LAMAR BLVD / SANDRA MURAIDA WAY (Lamar Bridge)"

print( df["loc"].nunique())
df["loc"] = df["loc"].apply( lambda value: value.strip() )
print( df["loc"].nunique())

print(df["Direction"].value_counts())


for g in df.groupby("loc"):
	name = g[0]
	data = g[1]

	print(name, data["Direction"].value_counts().to_dict())


for c in ["NB", "SB", "WB", "EB", "None"]:
	df[c] = df.apply(lambda row: row["Volume"] if row["Direction"] == c else 0, axis=1)

#df.to_csv("sample.csv")

print(df)
df2 = pd.pivot_table(df, values='Volume', index=['loc', 'Direction'], aggfunc=np.sum)


caddeler = df["loc"].unique()
print(caddeler)

dogrultular = {}

for cadde in caddeler:
	subset = df[ df["loc"] == cadde ]
	subset = subset["Direction"].unique()
	subset = list(subset)
	subset.sort()
	subset = "-".join(subset) # EB-WB
	dogrultular[cadde] = subset


print( dogrultular )

# df["DOGRULTU"] = df["loc"].apply(lambda loc: dogrultular[ loc ] )
df["DOGRULTU"] = df["loc"].map(dogrultular)
#df.to_csv("sample2.csv", sep = ";", encoding = "Windows-1254")

nbsb = df[ df["DOGRULTU"] == "NB-SB" ]
ebwb = df[ df["DOGRULTU"] == "EB-WB" ]
none = df[ df["DOGRULTU"] == "None" ]

print(nbsb["Volume"].mean(), nbsb["Volume"].std())
print(ebwb["Volume"].mean(), ebwb["Volume"].std())
print(none["Volume"].mean(), none["Volume"].std())





