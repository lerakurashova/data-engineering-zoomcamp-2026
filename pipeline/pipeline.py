import sys 
import pandas as pd

#parameter for a pipeline 
month = int(sys.argv[1])

print(f"Processing data for month: {month}")

df = pd.DataFrame({"day": [1, 2], "num_passengers": [3, 4]})
#create a new column based on the month parameter
df['month'] = month
print(df.head())
#save the dataframe to a parquet file
df.to_parquet(f"data_passengers_month_{month}.parquet", index=False)



