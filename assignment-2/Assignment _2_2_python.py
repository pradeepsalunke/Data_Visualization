
import pandas as pd

from sqlalchemy import create_engine

out_engine = create_engine(r"sqlite:////Users/pradeepipol/Music/Data_Visualization/Assignment-2/Assignment-2-master/salesdata.db")

# Getting the table names 

sql = "select name from sqlite_master"
"where type = 'table';"

sales_data_out = pd.read_sql(sql, out_engine)

sales_data_out


sql_table = "select * from scores"

score_data_out = pd.read_sql(sql_table, out_engine)

score_data_out.head()

