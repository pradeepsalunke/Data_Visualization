

import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,-2,77,78,101]
GradeList = zip(names,grades)
out = pd.DataFrame(data = list(GradeList), columns=['Names', 'Grades'])
out


out.loc[df['Grades'] <= 100]



out.loc[(df['Grades'] >= 100,'Grades')] = 100
df


out.loc[(df['Grades'] <= 0,'Grades')] = 0
out

