
import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,83,77,78,95]
GradeList = zip(names,grades)
data_out = pd.DataFrame(data = GradeList,columns=['Names', 'Grades'])
data_out.head()
import matplotlib.pyplot as plt
plt.plot('Names','Grades',data=data_out)
y= data_out['Grades'][data_out['Names']=='Bob']
plt.annotate('Wow!',xy=('Bob',y.values),xytext=(y.index.values+0.4,y.values),arrowprops=dict(facecolor='black',shrink=0.05))
plt.show()




