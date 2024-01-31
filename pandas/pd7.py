import pandas as pd
import numpy as np
data = {
    'Name': ['bhargav', 'kushal', 'sunil', 'nitesh'],
    'Age': [25, 30, 22, 28],
    'City': ['Guntur', 'Gurgaon', 'Delhi', 'Mumbai']
}
ilabels = ['Person1', 'Person2', 'Person3', 'Person4']
df11 = pd.DataFrame(data, index=ilabels)
print (df11)
