import numpy as np
import pandas as pd
carr=['bhargav','kushal','sunil']
carr=pd.Series(carr)
word_lengths = carr.apply(lambda i: len(i))
print(word_lengths)