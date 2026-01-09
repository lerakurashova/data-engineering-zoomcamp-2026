import sys 
import pandas as pd

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
print(df.head())

#parameter for a pipeline 
month = int(sys.argv[1])


