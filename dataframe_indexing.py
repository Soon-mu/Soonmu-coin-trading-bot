from pandas import DataFrame
from pandas import Series


data = {"open" : [737, 750], "high" :[755, 780], "low":[700,710], "close" : [750,770]}
df = DataFrame(data) #,index=["2020-12-08","2020-12-09"])
s = Series([300, 400])
df["volume"] = s
df.index=["2020-12-08","2020-12-09"]

df.loc['2020-12-10'] = (100,200,300,400,500)

upper = df["open"] * 1.3
df["upper"] = upper

print(df)