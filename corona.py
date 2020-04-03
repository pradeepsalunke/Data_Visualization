import pandas as pd
import folium
sf_map = folium.Map(location=[0,0])
out = pd.read_csv(r'/Users/pradeepipol/Music/Data_Visualization/COVID-19-master/02-22-2020.csv')
out = out[['Lat','Long_','Confirmed','Deaths']]
out = out.dropna(axis=0)

out = out[(out['Lat']!=0) & (out['Long_']!=0)]
out.shape


for lat, lng, case, deaths in zip(df.Lat, df.Long_, df.Confirmed, df.Deaths):
    folium.CircleMarker(location = [lat,lng], radius=(case/10000), color='red', fill=True, fill_color='red', fill_opacity=0.6,
                       popup = {'Confirmed' : case, 'Deaths' : deaths}).add_to(sf_map)
sf_map