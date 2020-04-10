import pandas as pd
Location = "/Users/pradeepipol/Music/Data_Visualization/datasets/gradedata.csv"
data_out = pd.read_csv(Location)
data_out.head()
data_out = data_out.sort_values(by=['fname','age','grade'],
ascending=[True, True,True])
data_out.head()

