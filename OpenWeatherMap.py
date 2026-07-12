import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load dataset
df = pd.read_csv("globalAirQuality.csv")
df.columns = df.columns.str.strip()

while True:
    print("\n===== OpenWeatherMap =====")
    print("1. Show All Info")
    print("2. Graph AQI vs Temperature (Max 10)")
    print("3. Graph Humidity vs Wind Speed (Max 10)")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "4":
        print("Exiting program. Goodbye!")
        break

    if choice in ["1", "2", "3"]:
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

    else:
        print("Invalid choice! Please select 1, 2, 3, or 4.")
