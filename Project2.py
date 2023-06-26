#libraries use
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#read data
data=pd.read_csv("Unemployment.csv")
print(data.head())

#to know information from the data
data.info
print(data.describe())

#to assign the value of data with new titles
data.columns=["State","Date","Frequency","Estimated Unemployment Rate","Estimated Employed",
              "Estimated Labour Participation Rate","Region","Longitude","Latitude"]
print(data)

#look the number of employes according to different region of India
data.columns=["State","Date","Frequency","Estimated Unemployment Rate","Estimated Employed",
              "Estimated Labour Participation Rate","Region","Longitude","Latitude"]
plt.title("Employment Rate in India")
sns.histplot(x="Estimated Employed",hue="Region",data=data)
plt.show()

#look the number of unemployment according to region in India
plt.figure(figsize=(12,10))
plt.title("Unemployment Rate in India")
sns.histplot(x="Estimated Unemployment Rate",hue="Region",data=data)
plt.show()

#to know the persentage in each region of india
Unemployment=data[["State","Region","Estimated Unemployment Rate"]]
figure=px.sunburst(Unemployment,path=["Region","State"],values="Estimated Unemployment Rate",
                   width=700,height=700,color_continuous_scale="RdylGn",title="Unemployment Rate in India")
figure.show()