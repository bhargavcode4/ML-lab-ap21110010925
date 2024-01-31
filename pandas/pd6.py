import pandas as pd
import numpy as np
dataf = {'YearMonth': ['2003-11', '2003-08', '2004-12', '2004-04']}
df = pd.DataFrame(dataf)
specified_day = 15
df['Date'] = pd.to_datetime(df['YearMonth'] + '-' + str(specified_day), format='%Y-%m-%d')
print("DataFrame after converting year-month string to dates:")
print(df)