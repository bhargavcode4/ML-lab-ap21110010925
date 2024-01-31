import numpy as np
import pandas as pd
a=[x*5 for x in range(1,11)]
a=pd.Series(a)
pos = a[a % 5 == 0].index
print(pos)