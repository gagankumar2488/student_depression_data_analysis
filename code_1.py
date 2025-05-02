import numpy as np
import pandas as pd
df = pd.read_csv(r"student_depression_dataset.csv",index_col= 0 )
print(df.describe())
print(df.size)