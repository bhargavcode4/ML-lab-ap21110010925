import numpy as np
import pandas as pd
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
series = pd.Series(data)

series.value_counts()

series[~series.isin(series.value_counts() .index[:1])] = 'Other'
print("Series after replacing other values with 'Other':")
print(series)
