from pandas import DataFrame
from pandas import Series

data = {"open" : [737,750,770],"high" : [755,780,770],"low" : [700,710,750],"close" : [750,770,730]}
df = DataFrame(data, index=["2020-12-08", "2020-12-09", "2020-12-10"])
print(df)

df["volatility"] = df['high'] - df['low']
print(df)

