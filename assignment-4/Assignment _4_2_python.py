

import pandas as pd
out = pd.read_csv(r"Users/pradeepipol/Music/Data_Visualization/Assignment-4/Assignment-4-master/gradedata.csv")
out.head()


import numpy as np
out['timemgmt']=np.where((out['exercise']>3)&(out['hours']>17),'busy','idle')

out.tail()

