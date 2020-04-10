import matplotlib.pyplot as plt
import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
status = ['Senior','Freshman','Sophomore','Senior','Junior']
grades = [76,95,77,78,99]
GradeList = zip(status,grades)
data_out = pd.DataFrame(data = GradeList,columns=['Status', 'Grades'])
get_ipython().run_line_magic('matplotlib', 'inline')
data_out.plot(kind='bar')
data_out2 = data_out.set_index(data_out['Status'])
data_out2.plot(kind="bar")

