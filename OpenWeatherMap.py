import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("globalAirQuality.csv")
 
print("----------------------------------")
print("OpenWeatherMap")
print("----------------------------------")
print("Check The weather info Of Your city")
print("----------------------------------")

Country=input("Enter the country name in short From : ").upper()
City=input("Enter the city name of that paticular country:  ")


result = df[(df["country"] == Country) & (df["city"] == City)]
 

 
if result.empty:
    print("Country not found")
else:
    print(f"Country: {result.iloc[0]['country']}")
    print(f"City: {result.iloc[0]['city']}")
    print(f"AQI: {result.iloc[0]['aqi']}")
    print(f"Humidity: {result.iloc[0]['humidity']}")
    print(f"Wind Speed: {result.iloc[0]['wind_speed']}")
    print(f"Temperature: {result.iloc[0]['temperature']}")

print("----------------------------------")
print("Thank you for visting ")
print("----------------------------------")