import pandas as pd
import numpy as np

att={
    'Name':['bhargav','kushal','sunil'],
    'attempts':[2,5,4]
}
att1=pd.DataFrame(att)

print(att1[att1['attempts']>2])