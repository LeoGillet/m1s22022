import pandas as pd

df = pd.DataFrame(columns=["Mouse1", "Mouse2", "Mouse3"],
index=["weight day1", "weight day2", "weight day3","weight day4"],
data=[[20, 18, 22],
[17, 16, 19],
[21, 21, 23],
[20, 18, 22] ])
print(df)

writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')