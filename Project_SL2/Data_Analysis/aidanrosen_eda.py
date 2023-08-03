import pandas as pd 
import sys
import numpy as np
pd.options.plotting.backend = "plotly"

csvPath = 'C:/Users/phuro/UCSD/DSC-190-IoT/Project_SL2/Data/processed_data.csv'

def makeDF(csvPath):
    df = pd.read_csv(csvPath, usecols=["Humidity (%)", "Temperature (F)", "Motion", "Time"])
    return df

#dateLower = sys.argv[2]
#dateUpper = sys.argv[3]

# print(sys.argv[1])
# df = makeDF(sys.argv[1])

df = pd.read_csv(csvPath, usecols=["Humidity (%)", "Temperature (F)", "Motion", "Time"])

#df[df.date.between(dateLower, dateUpper)]
print(df) 
print(df.describe())
fig = df.plot(x="Time", y="Humidity (%)")
figTemp = df.plot(x="Time", y="Temperature (F)")
figMotion = df.plot(x="Time", y="Motion")
 
fig.show()
figTemp.show()
figMotion.show()

#2023-08-01 20:03:27 <-- shoot the space is gonna make it a little difficult 
#2023-08-02 12:05:27