
import pandas as pd
import numpy as np
Location = "/Users/pradeepipol/Music/Data_Visualization/datasets/gradedata.csv"
data_out = pd.read_csv(Location)
data_out.tail()
data_out.take(np.random.permutation(len(df))[:500])




