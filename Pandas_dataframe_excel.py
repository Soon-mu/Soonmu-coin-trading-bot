import pandas as pd
url = "https://finance.naver.com/item/sise_day.nhn?code=066570"
df = pd.read_html(url)
print(df[0].dropna(axis=0))
df[0].to_excel("D:\Soonmu_phyton\enaver.xlsx")