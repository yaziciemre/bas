import sys
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', 6)
df = pd.read_csv("C:/Users/bilge.adam/PycharmProjects/pythonProject/train.csv")
# del df["id"]
df = df.drop(columns = ["id"])
df = df[ df["Driving_License"] == 1 ]
df = df.drop(columns = ["Driving_License"])

for c in df: # for c in df.columns
	cardinality = df[c].nunique() / df[c].count()
	if df[c].nunique() == 2:
		pass
		#print(c, df[c].nunique(), df[c].value_counts().to_dict(), cardinality)

#print(df.describe())

df["Vehicle_Damage"] = df["Vehicle_Damage"].map({"Yes":1, "No":0})
df["Gender"] = df["Gender"].map({"Male":1, "Female":0})
df["Vehicle_Age"] = df["Vehicle_Age"].map( {"> 2 Years": 2, "1-2 Year": 1, "< 1 Year": 0} )


for c in df.columns:
	if c not in ["Region_Code", "Policy_Sales_Channel"]:
		#print(c, df[c].corr( df["Response"] ))
		pass

for c in df.columns:
	a = df[c].unique()
	if len(a) < 5:
		for i in a:
			#print(c, i, df[df[c] == i]["Response"].mean())
			pass
	elif len(a) < 1000:
		ortalamalar = []
		for i in a:
			ortalamalar.append( df[df[c] == i]["Response"].mean())

		#print("!", c, np.mean(ortalamalar), np.std(ortalamalar) )


#Region_Code
#Vehicle_Age
#Policy_Sales_Channel
print("-------------------------")
values = df["Policy_Sales_Channel"].unique()
ITEMS_LOW = []
ITEMS_HIGH = []
for value in values:
	#print(value, df[df["Policy_Sales_Channel"] == value]["Response"].mean(), len(df[df["Policy_Sales_Channel"] == value]) )
	if df[df["Policy_Sales_Channel"] == value]["Response"].mean() < 0.03:
		ITEMS_LOW.append(value)
	elif df[df["Policy_Sales_Channel"] == value]["Response"].mean() > 0.17:
		ITEMS_HIGH.append(value)





df["LOW_CHANNEL"] = df["Policy_Sales_Channel"].isin(ITEMS_LOW)
df["HIGH_CHANNEL"] = df["Policy_Sales_Channel"].isin(ITEMS_HIGH)

df["HIGH_CHANNEL"] = df["HIGH_CHANNEL"].astype(int)
df["LOW_CHANNEL"] = df["LOW_CHANNEL"].astype(int)

df["MID_CHANNEL"] = (df["LOW_CHANNEL"] + df["HIGH_CHANNEL"]) == 0

print(df["LOW_CHANNEL"].corr(df["Response"]))
print(df["HIGH_CHANNEL"].corr(df["Response"]))
print(df["MID_CHANNEL"].corr(df["Response"]))



values = df["Region_Code"].unique()
REGION_ITEMS_LOW = []
REGION_ITEMS_HIGH = []
for value in values:
	#print(value, df[df["Region_Code"] == value]["Response"].mean(), len(df[df["Region_Code"] == value]) )
	if df[df["Region_Code"] == value]["Response"].mean() < 0.08:
		REGION_ITEMS_LOW.append(value)
	elif df[df["Region_Code"] == value]["Response"].mean() > 0.13:
		REGION_ITEMS_HIGH.append(value)


df["LOW_REGION"] = df["Region_Code"].isin(REGION_ITEMS_LOW)
df["HIGH_REGION"] = df["Region_Code"].isin(REGION_ITEMS_HIGH)

df["HIGH_REGION"] = df["HIGH_REGION"].astype(int)
df["LOW_REGION"] = df["LOW_REGION"].astype(int)

df["MID_REGION"] = (df["LOW_REGION"] + df["HIGH_REGION"]) == 0

print(df["LOW_REGION"].corr(df["Response"]))
print(df["HIGH_REGION"].corr(df["Response"]))
print(df["MID_REGION"].corr(df["Response"]))


del df["Region_Code"]
del df["Policy_Sales_Channel"]

print("-------------")
for i in range(20,81):
	#print( "Age", i, df[df["Age"] == i]["Response"].mean() )
	pass

df["AgeX"]  =df["Age"] > 30
print("AgeX", df["AgeX"].corr( df["Response"] ))
df["AgeY"]  =(df["Age"] > 32) * (df["Age"] < 50)
print("AgeY", df["AgeY"].corr( df["Response"] ))
"""
best = 0
bestAt = None
for i in range( df["Vintage"].min(), df["Vintage"].max() ):
	df["VintageX"] = df["Vintage"] > i
	c = df["VintageX"].corr( df["Response"] )
	if abs(c) > best:
		best = abs(c)
		bestAt = i
	print("Vintage", i, c)

print("best", best, bestAt)
df["VintageX"] = np.log(df["Vintage"])
c = df["VintageX"].corr(df["Response"])
print(c)
"""


"""
(['Gender', 'Age', 'Previously_Insured', 'Vehicle_Age', 'Vehicle_Damage',
       'Annual_Premium', 'Vintage', 'Response', 'LOW_CHANNEL', 'HIGH_CHANNEL',
       'MID_CHANNEL', 'LOW_REGION', 'HIGH_REGION', 'MID_REGION', 'AgeX',
       'AgeY', 'VintageX'])
"""

# df.corr().to_csv("corr.csv", sep=";", decimal=",")

transformation = ["sqrt", "log", "log2", "pow2", "pow0.1", "pow0.3", "exp"]

def transform( values: np.array, function: str ) -> np.array:
	if function == "sqrt":
		return np.sqrt( values )
	if function == "log":
		return np.log10( values )
	if function == "log2":
		return np.log2( values )
	if function == "pow2":
		return np.power( values, 2.0 )
	if function == "pow0.1":
		return np.power( values, 0.1 )
	if function == "pow0.3":
		return np.power( values, 0.3 )
	if function == "exp":
		return np.exp( values )

for c in ["Annual_Premium"]:
	for t in transformation:
		df["yeni_değişken"] = transform(df[c].values, t)
		original = df[c].corr(df["Response"])
		new = df["yeni_değişken"].corr( df["Response"] )
		#if abs(new) > abs(original) + 0.01:
		#print("yeni_değişken", c, t, original, new)



"""
Index(['Gender', 'Age', 'Previously_Insured', 'Vehicle_Age', 'Vehicle_Damage',
       'Annual_Premium', 'Vintage', 'Response', 'LOW_CHANNEL', 'HIGH_CHANNEL',
       'MID_CHANNEL', 'LOW_REGION', 'HIGH_REGION', 'MID_REGION', 'AgeX',
       'AgeY'],
      dtype='object')
"""

df["x1"] = df["Previously_Insured"] + df["LOW_CHANNEL"]
#df["x1a"] = df["Previously_Insured"] * df["LOW_CHANNEL"]
#df["x1b"] = 2 * df["Previously_Insured"] + df["LOW_CHANNEL"]
df["x1c"] = 0.5 * df["Previously_Insured"] + df["LOW_CHANNEL"]
df["x1d"] = 0.1 * df["Previously_Insured"] + df["LOW_CHANNEL"]
df["x1e"] = np.sign(df["Previously_Insured"] + df["LOW_CHANNEL"])
#df["x1f"] = df["Previously_Insured"] * df["LOW_CHANNEL"]
#df["x1e"] = 0.1 * df["Previously_Insured"] + df["LOW_CHANNEL"] + df["Vehicle_Damage"]
#df["x1f"] = 0.1 * df["Previously_Insured"] + df["LOW_CHANNEL"] + 3* df["Vehicle_Damage"]
df["x1g"] = 0.1 * df["Previously_Insured"] + df["LOW_CHANNEL"] + 0.3* df["Vehicle_Damage"]



df["x2"] = df["Vehicle_Damage"] + df["HIGH_CHANNEL"]
df["x3"] = df["AgeX"] + df["HIGH_CHANNEL"]
#df["x4"] = df["LOW_REGION"] + df["LOW_CHANNEL"]
df["x5"] = df["LOW_REGION"] * df["LOW_CHANNEL"]
#df["x6"] = df["HIGH_REGION"] * df["HIGH_CHANNEL"]
df["x7"] = df["Previously_Insured"] * df["LOW_CHANNEL"]
df["x8"] = df["Previously_Insured"] + df["LOW_CHANNEL"] + df["LOW_REGION"]
df["x9"] = df["Previously_Insured"] + df["LOW_CHANNEL"] + df["LOW_REGION"] + df["Vehicle_Damage"]
df["x10"] = df["Previously_Insured"] * -0.34 + df["LOW_CHANNEL"] * -0.24 + df["LOW_REGION"] * -0.08

df["x11"] = df["Vehicle_Damage"] * df["Vehicle_Age"] * df["HIGH_CHANNEL"] * df["AgeY"]
df["x12"] = df["Vehicle_Damage"] * df["Vehicle_Age"] * df["HIGH_CHANNEL"]
#df["x13"] = df["Vehicle_Damage"] * df["Vehicle_Age"] * df["AgeY"]
df["x14"] = df["Vehicle_Damage"] * df["AgeY"]

df["x15"] = df["Vehicle_Damage"] + df["Vehicle_Age"] + df["HIGH_CHANNEL"] + df["AgeY"]
df["x16"] = 0.1 * df["Vehicle_Damage"] + df["AgeY"]
df["x17"] = df["Vehicle_Damage"] * df["AgeY"]
df["x18"] = df["Vehicle_Damage"] + df["AgeY"]






#: Sonsuzları 0 ile replace edelim
del df["yeni_değişken"]
del df["MID_CHANNEL"]
del df["MID_REGION"]
del df["Gender"]

del df["Annual_Premium"]
del df["Vintage"]
del df["x5"]
del df["x10"]
del df["x9"]
del df["x8"]
del df["x2"]
del df["x3"]
del df["x7"]

df["AgeX"] = df["AgeX"].astype(int)
df["AgeY"] = df["AgeY"].astype(int)

df = df.replace(np.inf, 0)
df = df.sample(frac = 0.80)
print("-------------------")
for c in df:
	#print( c, df[c].corr(df["Response"]) )
	pass

limit = int(0.70 * len(df))
train = df[:limit]
test = df[limit:]

# dengeleme
# balancing
train0 = train[  train["Response"] == 0 ].sample(frac = 0.40)
train1 = train[  train["Response"] == 1 ]
train = pd.concat( [train0, train1] )

train_y = train["Response"]
train_x = train.drop( columns = ["Response"] )

test_y = test["Response"]
test_x = test.drop( columns = ["Response"] )


from imblearn.ensemble import BalancedBaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier

import lightgbm as lgb
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import VotingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import f1_score
import xgboost as xgb


clf1 = LogisticRegression(multi_class='multinomial', random_state=1, max_iter=500)
clf2 = RandomForestClassifier(n_estimators=50, random_state=1)
clf3 = GaussianNB()

# Use "gpu_hist" for training the model.
reg = xgb.XGBClassifier()
# Fit the model using predictor X and response y.
reg.fit(train_x, train_y)
# Save model into JSON format.
print("X", f1_score( test_y, reg.predict(test_x)))

#f = VotingClassifier(estimators=[('lr', clf1), ('rf', clf2), ('gnb', clf3)], voting='hard')

clf1.fit(train_x, train_y)
clf2.fit(train_x, train_y)
clf3.fit(train_x, train_y)

c1 = clf1.predict(test_x)
c2 = clf2.predict(test_x)
c3 = clf3.predict(test_x)

test_x["REAL"] = test_y
test_x["c1"] = c1
test_x["c2"] = c2
test_x["c3"] = c3
test_x["c"] = test_x["c1"] + test_x["c2"] + test_x["c3"]

test_x["c_eq_1"] = test_x["c"] == 1
test_x["c_eq_2"] = test_x["c"] == 2
test_x["c_eq_3"] = test_x["c"] == 3
test_x["c_eq_23"] = test_x["c"] > 1
test_x["c_eq_123"] = test_x["c"] > 0

print("A",f1_score(test_y, test_x["c_eq_1"]))
print("A",f1_score(test_y, test_x["c_eq_2"]))
print("A",f1_score(test_y, test_x["c_eq_3"]))
print("A",f1_score(test_y, test_x["c_eq_23"]))
print("A",f1_score(test_y, test_x["c_eq_123"]))

sys.exit(1)
f.fit(train_x, train_y)
print("FX", f1_score(test_y, f.predict(test_x)))

sys.exit(1)




f0 = RandomForestClassifier(max_depth=5, random_state=0, n_estimators=100, class_weight="balanced")
f1 = BalancedBaggingClassifier()
f2 = AdaBoostClassifier(n_estimators=100, random_state=0)
f3 = lgb.LGBMClassifier()
#f4 = MLPClassifier(random_state=1, hidden_layer_sizes=(300,), max_iter=300)
#f5 = SVC(gamma='auto')
f4 = LogisticRegression(random_state=0)
import datetime
fs = [f0, f1, f2, f3, f4]

for f in fs:
	print(datetime.datetime.now())
	from sklearn.metrics import f1_score
	f.fit(train_x, train_y)
	print("F1", f1_score(test_y, f.predict(test_x)))


sys.exit(1)
p = f.predict(test_x)

pr = f.predict_proba(test_x)[:,1]

test_x["REAL"] = test_y
test_x["PRED"] = p
test_x["PROB"] = pr

# test_x["PRED"] = test_x["PROB"] > 0.6

print("PRED.AVG", test_x["PRED"].mean())
print("REAL.AVG", test_x["REAL"].mean())

test_x["TRUE"] = test_x["PRED"] == test_x["REAL"]
test_x["TRUE"] = test_x["TRUE"].astype(int)
test_x["ERROR"] = 1 - test_x["TRUE"]

test_x["TP"] = (test_x["PRED"] == 1) & (test_x["REAL"] == 1)
test_x["TN"] = (test_x["PRED"] == 0) & (test_x["REAL"] == 0)
test_x["FP"] = (test_x["PRED"] == 1) & (test_x["REAL"] == 0)
test_x["FN"] = (test_x["PRED"] == 0) & (test_x["REAL"] == 1)

test_x["TP"] = test_x["TP"].astype(int)
test_x["TN"] = test_x["TN"].astype(int)
test_x["FP"] = test_x["FP"].astype(int)
test_x["FN"] = test_x["FN"].astype(int)

print("TP", test_x["TP"].mean())
print("TN", test_x["TN"].mean())
print("FP", test_x["FP"].mean())
print("FN", test_x["FN"].mean())

print("TRUELAR", test_x["TP"].mean() + test_x["TN"].mean())

"""
for i in range(len(f.feature_importances_)):
	print("FI", test_x.columns[i], f.feature_importances_[i])
"""

test_x.to_csv("pred.csv", sep=";", decimal=",")





