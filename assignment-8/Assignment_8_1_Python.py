import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "/Users/pradeepipol/Music/Data_Visualization/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()
df.hist(column="age", by="gender")





