import pandas as pd
sales = pd.read_csv("C:/Users/Wilson/Downloads/sales.csv")

date = pd.DatetimeIndex(sales['date'])
sales['month'] = date.month

df=sales.groupby(['month','Products']).sum('Units sold').sort_values(['month','Units sold'],ascending=[True,False])
top_five = df.groupby("month").head(5)
print(top_five)