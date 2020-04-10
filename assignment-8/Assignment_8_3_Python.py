import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
location = "/Users/pradeepipol/Music/Data_Visualization/datasets/gradedata.csv"
df = pd.read_csv(location)
df.head()
plt.scatter(df.hours, df.grade)
plt.show()
