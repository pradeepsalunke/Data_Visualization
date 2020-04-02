
import pandas as pd
import numpy as np
import glob
data = pd.DataFrame()
for i in glob.glob(r"/Users/pradeepipol/Music/Data_Visualization/Assignment-2/Assignment-2-master.xlsx"):
    out = pd.read_excel(i)
    data = data.append(out,ignore_index=True)
data.head()

