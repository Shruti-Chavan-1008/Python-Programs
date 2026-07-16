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
    print("4. ")
    print("5. Check the highest aqi city ")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "6":
        print("Exiting program. Goodbye!")
        break

    if choice in ["1", "2", "3","4"]:
        country = input("Enter Country (e.g., US, IN): ").strip()
        city = input("Enter City: ").strip()

        # Filter data and limit to top 10 rows using .head(10)
        result = df[
            (df["country"].str.lower() == country.lower())
            & (df["city"].str.lower() == city.lower())
        ].head(10)

    if choice == "1":
        if result.empty:
            print("Country or City not found!")
        else:
            print(f"\nCountry: {result.iloc['country']}")
            print(f"City: {result.iloc['city']}")
            print(f"AQI: {result.iloc['aqi']}")
            print(f"Humidity: {result.iloc['humidity']}")
            print(f"Wind Speed: {result.iloc['wind_speed']}")
            print(f"Temperature: {result.iloc['temperature']}")

    elif choice == "2":
        if result.empty:
            print("No data found!")
        else:
            result.plot(y=["aqi", "temperature"], kind="bar")
            plt.title(f"AQI vs Temp for {city.title()}, {country.title()} (Top 10)")
            plt.ylabel("Values")
            plt.tight_layout()
            plt.show()

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

    elif choice == "4":
        if result.empty:
            print("No data found!")
        else:
            aqi_value=result.iloc['aqi']
            if 50 <= aqi_value <= 60:
                print("The Perfect Window")
                print("This narrow window is highly safe and requires no restrictions, only positive actions.")

                print("======Precaution======")
                print("Air Status : Very clean, crisp, and safe.")
                print("Action 1: Open all doors and windows to fully ventilate your house.")
                print("Action 2: Schedule your hardest outdoor workouts, running, or sports during this time.")
                print("Action 3: No masks or air purifiers are needed at all.")
            elif 60 < aqi_value <= 80: 
                print("The Caution Window")
                print("This narrow window is highly safe and requires no restrictions, only positive actions.")

                print("======Precaution======")
                print("Air Status: Dust and vehicle exhaust are starting to hang in the air.")
                print("Action 1: If you have asthma or allergies, avoid heavy running or lifting weights outdoors.")
                print("Action 2: Close windows during peak morning and evening traffic rush hours to keep fumes out.")
                print("Action 3: Switch to indoor exercises (like home workouts or gym sessions) if you are feeling a dry throat.")




    elif choice == "5":
         
         filtered_df=df[df['aqi']>200][['country','city','aqi']] 
         print(tabulate(filtered_df, headers='keys', tablefmt='grid', showindex=False))


    else:
        print("Invalid choice! Please select 1, 2, 3, 4 or 5.")
