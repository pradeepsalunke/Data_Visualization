

import pandas as pd
out = pd.read_csv(r"Users/pradeepipol/Music/Data_Visualization/Assignment-4/Assignment-4-master/gradedata.csv")
out.head()

bins = [0, 80, 100]
# Create names for the four groups
group_names = ['Fail', 'Pass']


out['Pass/Fail'] = out.cut(df['grade'], bins,
labels=group_names, right=False)


out.head()

