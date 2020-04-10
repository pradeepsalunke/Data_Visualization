import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
names = ['Bob','Jessica','Mary','John','Mel']
absences = [3,0,1,0,8]
detentions = [2,1,0,0,1]
warnings = [2,1,5,1,2]
GradeList = zip(names,absences,detentions,warnings)
columns=['Names', 'Absences', 'Detentions','Warnings']
data_out = pd.DataFrame(data = GradeList, columns=columns)
data_out
data_out['TotalDemerits'] = data_out['Absences'] + data_out['Detentions'] + data_out['Warnings']
data_out
plt.pie(data_out['TotalDemerits'])
plt.pie(data_out['TotalDemerits'],
labels=data_out['Names'],
explode=(0,0,0,0.15,0),
startangle=90,
autopct='%1.1f%%',)
plt.axis('equal')
plt.show()

