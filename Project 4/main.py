# Course            : Programming for Problem Solving using Python
# Assignment Title  : Object-Oriented Design and Robust Programming in a Library Management System
# Name              : Kaushal
# Roll no.          : 2501730085
# Section           : B
# School            : School of engineering technology(SOET)
# Submission date   : 4 Dec 2025

# ------------------ Task 1 & 2 ------------------

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV fileaa
df = pd.read_csv("delhi_weather.csv")   # Make sure the CSV is in the same folder

# Show first 5 rows
print("----- First 5 rows -----")
print(df.head())

# Show dataset info
print("\n----- Dataset Info -----")
print(df.info())

# Show summary statistics
print("\n----- Summary Statistics -----")
print(df.describe())

# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Optional: filter only relevant columns
df = df[['date', 'meantemp', 'humidity', 'wind_speed']]

# Display cleaned dataset
print("\n----- Cleaned Data (first 5 rows) -----")
print(df.head())
print("\n----- Data Types After Conversion -----")
print(df.dtypes)


# ------------------ Task 3: Statistical Analysis ------------------

# Daily statistics are already in the dataset (each row is a day)

# Monthly statistics
df['month'] = df['date'].dt.month
monthly_stats = df.groupby('month')[['meantemp','humidity','wind_speed']].agg(
    ['mean', 'min', 'max', 'std']
)
print("\n----- Monthly Statistics -----")
print(monthly_stats)

# Yearly statistics
df['year'] = df['date'].dt.year
yearly_stats = df.groupby('year')[['meantemp','humidity','wind_speed']].agg(
    ['mean', 'min', 'max', 'std']
)
print("\n----- Yearly Statistics -----")
print(yearly_stats)


# ------------------ Task 4: Visualization ------------------
import matplotlib.pyplot as plt

# 1️⃣ Line chart: Daily Temperature Trend
plt.figure(figsize=(12,5))
plt.plot(df['date'], df['meantemp'], color='orange')
plt.title("Daily Mean Temperature")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.tight_layout()
plt.savefig("daily_temperature.png")  # Save plot as PNG
plt.show()

# 2️⃣ Bar chart: Average Humidity by Month
monthly_humidity = df.groupby('month')['humidity'].mean()
plt.figure(figsize=(10,5))
monthly_humidity.plot(kind='bar', color='skyblue')
plt.title("Average Humidity by Month")
plt.xlabel("Month")
plt.ylabel("Humidity (%)")
plt.grid(axis='y')
plt.tight_layout()
plt.savefig("monthly_humidity.png")  # Save plot as PNG
plt.show()

# 3️⃣ Scatter plot: Humidity vs. Temperature
plt.figure(figsize=(10,5))
plt.scatter(df['meantemp'], df['humidity'], alpha=0.6, color='green')
plt.title("Humidity vs. Mean Temperature")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.grid(True)
plt.tight_layout()
plt.savefig("scatter_humidity_temp.png")  # Save plot as PNG
plt.show()

# 4️⃣ Combined Figure: Temperature and Humidity Trends
fig, ax1 = plt.subplots(figsize=(12,5))

ax1.plot(df['date'], df['meantemp'], color='orange', label='Temperature (°C)')
ax1.set_xlabel("Date")
ax1.set_ylabel("Temperature (°C)", color='orange')
ax1.tick_params(axis='y', labelcolor='orange')

ax2 = ax1.twinx()
ax2.plot(df['date'], df['humidity'], color='blue', alpha=0.6, label='Humidity (%)')
ax2.set_ylabel("Humidity (%)", color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

plt.title("Daily Temperature & Humidity")
fig.tight_layout()
plt.savefig("combined_temp_humidity.png")  # Save plot as PNG
plt.show()


# ------------------ Task 5: Grouping & Aggregation ------------------

# 1️⃣ Define a function to map month to season
def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8, 9]:
        return 'Monsoon'
    else:
        return 'Autumn'

# Add 'season' column
df['season'] = df['month'].apply(get_season)

# 2️⃣ Monthly Aggregation
monthly_agg = df.groupby('month')[['meantemp', 'humidity', 'wind_speed']].agg(
    ['mean', 'min', 'max', 'std']
)
print("\n----- Monthly Aggregated Stats -----")
print(monthly_agg)

# 3️⃣ Seasonal Aggregation
seasonal_agg = df.groupby('season')[['meantemp', 'humidity', 'wind_speed']].agg(
    ['mean', 'min', 'max', 'std']
)
print("\n----- Seasonal Aggregated Stats -----")
print(seasonal_agg)

# 4️⃣ Optional: Export aggregated stats to CSV
monthly_agg.to_csv("monthly_aggregated_stats.csv")
seasonal_agg.to_csv("seasonal_aggregated_stats.csv")

print("\nMonthly and seasonal aggregated CSV files saved successfully!")


# ------------------ Export Cleaned Dataset ------------------

df.to_csv("cleaned_weather_data.csv", index=False)
print("Cleaned dataset saved as 'cleaned_weather_data.csv'")




