
import pandas as pd
Location = "/Users/pradeepipol/Music/Data_Visualization/datasets/gradedata.csv"
data_out = pd.read_csv(Location)
data_out.head()

import statsmodels.formula.api as sm
result = sm.ols(
formula='grade ~ age + exercise + hours',
data=data_out).fit()
result.summary()



data_out['numGender'] = [1 if x =='female' else 0 for x in data_out['gender']] 


data_out



import statsmodels.formula.api as sm
result = sm.ols(
formula='grade ~ age + exercise + hours + numGender',
data=data_out).fit()
result.summary()

