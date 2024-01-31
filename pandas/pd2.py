import numpy as np
import pandas as pd
df = pd.Series([109, 720, 9630, 440, 250])
subset = df[df>=440]
subset2=df[df<=630]
print(subset)
print(subset2)