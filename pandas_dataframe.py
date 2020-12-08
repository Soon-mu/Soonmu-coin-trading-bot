from pandas import DataFrame

data = {'open' : [100, 200], "high":[110,210]}
df = DataFrame(data)
print(df)

data = {"open" : [737, 750], "high" :[755, 780], "low":[700,710], "close" : [750,770]}
df = DataFrame(data,index=["2020-12-08","2020-12-09"])
print(df)