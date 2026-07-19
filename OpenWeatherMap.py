import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tabulate import tabulate

# Load dataset
df = pd.read_csv("globalAirQuality.csv")
df.columns = df.columns.str.strip()

while True:
    print("\n===== OpenWeatherMap =====")
    print("1. Show All Info")
    print("2. Graph AQI vs Temperature (Max 10)")
    print("3. Graph Humidity vs Wind Speed (Max 10)")
    print("4. Percaution for your city")
    print("5. Check the highest aqi city ")
    print("6. Exit")

    choice = input("Enter your choice: ")


     # it will help to exist  for program
    if choice == "6":
        print("Exiting program. Goodbye!")
        break


    #it take the user input 
    if choice in ["1", "2", "3","4"]:
        country = input("Enter Country (e.g., US, IN): ").strip()
        city = input("Enter City: ").strip()

        # Filter data and limit to top 10 rows using .head(10)
        result = df[
            (df["country"].str.lower() == country.lower())
            & (df["city"].str.lower() == city.lower())
        ].head(10)
    # it will describe the basic infromation related city
    if choice == "1":
     if result.empty:
        print("Country or City not found!")
     else:
        # Pull the column first, then grab the first row [0]
        print(f"\nCountry: {result['country'].iloc[0]}")
        print(f"City: {result['city'].iloc[0]}")
        print(f"AQI: {result['aqi'].iloc[0]}")
        print(f"Humidity: {result['humidity'].iloc[0]}")
        print(f"Wind Speed: {result['wind_speed'].iloc[0]}")
        print(f"Temperature: {result['temperature'].iloc[0]}")
        print(f'Date of analysis {df['timestamp'].iloc[0]}')
   

    #shows the graph api vs temperture
    elif choice == "2":
        if result.empty:
            print("No data found!")
        else:
            result.plot(y=["aqi", "temperature"], kind="bar")
            plt.title(f"AQI vs Temp for {city.title()}, {country.title()} (Top 10)")
            plt.ylabel("Values")
            plt.tight_layout()
            plt.show()

    #it shows the garph of the humidity vs wind_speed
    elif choice == "3":
        if result.empty:
            print("No data found!")
        else:
            result.plot(
                y=["humidity", "wind_speed"], kind="bar", color=["blue", "green"]
            )
            plt.title(f"Humidity vs Wind Speed for {city.title()}, {country.title()} (Top 10)")
            plt.ylabel("Values")
            plt.tight_layout()
            plt.show()
 

    #it checks the aqi info and tell the Percaution to user
    elif choice == "4":
      if result.empty:
        print("No data found!")
      else:
        # Safely extracts the first matching row's AQI
        aqi_value = result.iloc[0]['aqi']
        print(f"\nCurrent AQI: {aqi_value}")
         
        if aqi_value < 50:
            print("The Elite Window")
            print("The air is pristine. Absolutely perfect conditions.")
            print("===============================================Precaution=========================================")
            print("Air Status : Exceptionally clean and crisp.")
            print("Action 1   : Open all doors and windows to fully flush your house with fresh air.")
            print("Action 2   : Perfect day for long runs, hiking, or any intense outdoor sports.")
            print("Action 3   : No masks or purifiers needed.")

        elif 50 <= aqi_value <= 60:
            print("The Perfect Window")
            print("This narrow window is highly safe and requires no restrictions.")
            print("============================================Precaution============================================")
            print("Air Status : Clean and safe for almost everyone.")
            print("Action 1   : Great time to ventilate your indoor living spaces.")
            print("Action 2   : Schedule standard outdoor workouts or sports during this time.")
            print("Action 3   : No restrictions needed for general public.")

        elif 60 < aqi_value <= 100: 
            print("The Caution Window")
            print("The air is acceptable, but pollutants are beginning to accumulate.")
            print("=======================================Precaution=====================================")
            print("Air Status : Dust and vehicle exhaust are starting to hang in the air.")
            print("Action 1   : Sensitive groups (asthma/allergies) should avoid heavy outdoor cardio.")
            print("Action 2   : Close windows during peak morning and evening traffic rush hours.")
            print("Action 3   : Switch to indoor gym exercises if you experience any throat irritation.")

        else: # Covers everything greater than 100
            print("The Danger Window")
            print("The air quality is poor and unhealthy for active outdoor exposure.")
            print("=============================Precaution===============================================")
            print("Air Status : High levels of pollution/smog detected.")
            print("Action 1   : Keep all windows firmly closed to protect indoor air quality.")
            print("Action 2   : Move all athletic activities and workouts strictly indoors.")
            print("Action 3   : Wear an N95 mask if you must spend extended time outside.")


    # it display the country and city having different aqi
    elif choice == "5":
         
         filtered_df=df[df['aqi']>200][['country','city','aqi']] 
         print(tabulate(filtered_df, headers='keys', tablefmt='grid', showindex=False))


    else:
        print("Invalid choice! Please select 1, 2, 3, 4 or 5.")
