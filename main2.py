import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
path = "C:/Users/bilge.adam/Downloads/NN5_FINAL_DATASET_WITH_TEST_DATA.xls"
df = pd.read_excel(path)




df["mean"] = df["NN5-001"].mean()
df["movingaverage"] = df["NN5-001"].rolling(2).mean()
df["error"] = np.abs(df["NN5-001"] - df["movingaverage"])
df["error"] = df["error"] / df["NN5-001"]
# df["error"] = df["error"].apply(lambda value: value if value > 20 else 0)

df["original"] = df["NN5-001"]

print(df)


def linreg(X, Y):
    """
    return a,b in solution to y = ax + b such that root mean square distance between trend line and original points is minimized
    """
    N = len(X)
    Sx = Sy = Sxx = Syy = Sxy = 0.0
    for x, y in zip(X, Y):
        Sx = Sx + x
        Sy = Sy + y
        Sxx = Sxx + x*x
        Syy = Syy + y*y
        Sxy = Sxy + x*y
    det = Sxx * N - Sx * Sx
    return (Sxy * N - Sy * Sx)/det, (Sxx * Sy - Sx * Sxy)/det
#x = [12, 34, 29, 38, 34, 51, 29, 34, 47, 34, 55, 94, 68, 81]
# a,b = linreg(range(len(x)),x)  //your x,y are switched from standard notation

df["NN5-001"] = df["NN5-001"].fillna( df["NN5-001"].mean() )

m,n = linreg( range(len(df)), df["NN5-001"].values)
print(m,n)

df["index"] = range(len(df))
df["trend"] = m * df["index"] + n

#plt.plot( df["NN5-001"] )
#plt.plot( df["movingaverage"] )
#plt.plot( df["error"] )
#plt.plot( df["trend"] )


df = df.rename(columns = {"Time Series #ID": "Date"})

# df["Date"] = pd.to_datetime( df["Date"] )
df["Month"] = df["Date"].dt.month
df["DayOfWeek"] = df["Date"].dt.dayofweek
df["day"] = df["Date"].dt.day

# de-trend
df["NN5-001"] = df["NN5-001"] - df["trend"]

# de-cycle
dayofweek = {}
for c in df.groupby("DayOfWeek"):
	name = c[0]
	data = c[1]["NN5-001"].mean()
	dayofweek[name] = data

df["cycle"] = df["DayOfWeek"].map( dayofweek )

df["NN5-001"] = df["NN5-001"] - df["cycle"]

plt.plot( df["NN5-001"] )
"""
for i in range(60):
	cc = df["NN5-001"].corr( df["NN5-001"].shift(i) )
	if abs(cc)  > 0.10:
		print(i, cc)


"""

#df = df[400:]
#print( df["NN5-001"].corr( df["original"] ) )
#plt.show()

df["month"] = df["Date"].dt.month
df["doy"] = df["Date"].dt.day_of_year

df["wintersummer"] = df["month"].isin([9,10,11,12,1,2])
df["season_1"] = df["month"].isin([8,9])
df["season_3"] = df["month"].isin([7,8,9])
print(df["season_1"].corr(df["NN5-001"]))
print(df["season_3"].corr(df["NN5-001"]))



p = []
n = []
for i in range(1, 32):
	c = df[df["day"] == i]["NN5-001"].mean()
	if abs(c) > 0.5:
		if np.sign(c) == 1:
			p.append(i)
		else:
			n.append(i)



print(p)
print(n)


df["x10"] = df["day"].isin([30, 22, 23, 14, 12])
df["x11"] = df["day"].isin([24, 25, 10, 26])


df["xa"] = df["day"].isin(p)
df["xb"] = df["day"].isin(n)

print("!", df["NN5-001"].corr(df["x10"]))
print("!", df["NN5-001"].corr(df["x11"]))
print("!", df["NN5-001"].corr(df["xa"]))
print("!", df["NN5-001"].corr(df["xb"]))


#print("!", df["NN5-001"].corr(df["x9"]))




# fill
# dropna
# feature selection
