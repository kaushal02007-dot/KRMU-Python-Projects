# Course            : Programming for Problem Solving using Python
#Assignment Title   :  End-to-End Energy Consumption Analysis and Visualization 
# Name              : Kaushal
# Roll no.          : 2501730085
# Section           : B
# School            : School of engineering technology(SOET)
# Submission date   : 4 Dec 2025

# Imports
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

# ---------------------------
# Task 1: Data Ingestion and Validation
# ---------------------------

data_path = Path("data")
csv_files = list(data_path.glob("*.csv"))

df_combined = pd.DataFrame()
log_messages = []

for file in csv_files:
    try:
        df = pd.read_csv(file, on_bad_lines='skip')  # Skip corrupt rows

        # Add metadata if not present
        if 'Building' not in df.columns:
            df['Building'] = file.stem.split('_')[0]
        if 'Month' not in df.columns:
            df['Month'] = file.stem.split('_')[1] if '_' in file.stem else 'Unknown'

        df_combined = pd.concat([df_combined, df], ignore_index=True)

    except FileNotFoundError:
        log_messages.append(f"File not found: {file}")
    except Exception as e:
        log_messages.append(f"Error reading {file}: {e}")

# Clean Timestamp column
df_combined['Timestamp'] = df_combined['Timestamp'].astype(str).str.strip()
df_combined = df_combined.dropna(subset=['Timestamp', 'kWh'])
df_combined['Timestamp'] = pd.to_datetime(df_combined['Timestamp'], format='%Y-%m-%d %H:%M')

# Print logs
for log in log_messages:
    print(log)

print("\nCombined DataFrame:")
print(df_combined.head())
print(f"Total rows combined: {len(df_combined)}")

# ---------------------------
# Task 2: Core Aggregation Logic
# ---------------------------

def calculate_daily_totals(df):
    daily = df.groupby(['Building', pd.Grouper(key='Timestamp', freq='D')])['kWh'].sum().reset_index()
    return daily

def calculate_weekly_totals(df):
    weekly = df.groupby(['Building', pd.Grouper(key='Timestamp', freq='W')])['kWh'].sum().reset_index()
    return weekly

def building_wise_summary(df):
    summary = df.groupby('Building')['kWh'].agg(['mean', 'min', 'max', 'sum']).reset_index()
    summary.rename(columns={'sum':'total'}, inplace=True)
    return summary

daily_totals = calculate_daily_totals(df_combined)
weekly_totals = calculate_weekly_totals(df_combined)
summary_table = building_wise_summary(df_combined)

print("\n--- Daily Totals ---")
print(daily_totals.head(), "\n")

print("--- Weekly Totals ---")
print(weekly_totals.head(), "\n")

print("--- Building-wise Summary ---")
print(summary_table)

# ---------------------------
# Task 3: Object-Oriented Modeling
# ---------------------------

class MeterReading:
    def __init__(self, timestamp, kwh):
        self.timestamp = timestamp
        self.kwh = kwh

class Building:
    def __init__(self, name):
        self.name = name
        self.meter_readings = []

    def add_reading(self, reading):
        self.meter_readings.append(reading)

    def calculate_total_consumption(self):
        return sum(r.kwh for r in self.meter_readings)

    def generate_report(self):
        total = self.calculate_total_consumption()
        print(f"{self.name} Total Consumption: {total:.2f} kWh")
        return total

class BuildingManager:
    def __init__(self):
        self.buildings = {}

    def add_building(self, building):
        self.buildings[building.name] = building

    def generate_all_reports(self):
        print("\n--- Building Reports ---")
        for b in self.buildings.values():
            b.generate_report()

# Populate buildings
manager = BuildingManager()
for building_name, group in df_combined.groupby('Building'):
    b = Building(building_name)
    for _, row in group.iterrows():
        b.add_reading(MeterReading(row['Timestamp'], row['kWh']))
    manager.add_building(b)

manager.generate_all_reports()

# ---------------------------
# Task 4: Visualization with Matplotlib
# ---------------------------

fig, axs = plt.subplots(3, 1, figsize=(12, 18))

# --- Chart 1: Daily Trend Line ---
for building in daily_totals['Building'].unique():
    df_b = daily_totals[daily_totals['Building'] == building]
    axs[0].plot(df_b['Timestamp'], df_b['kWh'], marker='o', label=building)
axs[0].set_title("Daily Electricity Consumption per Building")
axs[0].set_xlabel("Date")
axs[0].set_ylabel("kWh")
axs[0].legend()
axs[0].grid(True)

# --- Chart 2: Bar Chart of Average Weekly Usage ---
weekly_avg = weekly_totals.groupby('Building')['kWh'].mean().reset_index()
axs[1].bar(weekly_avg['Building'], weekly_avg['kWh'], color='skyblue')
axs[1].set_title("Average Weekly Consumption per Building")
axs[1].set_xlabel("Building")
axs[1].set_ylabel("Average kWh")
axs[1].grid(axis='y')

# --- Chart 3: Scatter Plot of Peak Hour Consumption ---
peak_hour = df_combined.groupby(['Building', 'Timestamp'])['kWh'].sum().reset_index()
axs[2].scatter(peak_hour['Timestamp'], peak_hour['kWh'], c='red', label='kWh')
axs[2].set_title("Peak-Hour Consumption")
axs[2].set_xlabel("Timestamp")
axs[2].set_ylabel("kWh")
axs[2].grid(True)

plt.tight_layout()
plt.savefig("dashboard.png")
plt.show()
print("\nDashboard saved as 'dashboard.png'")

# ---------------------------
# Task 5: Persistence and Executive Summary
# ---------------------------

output_folder = Path("output")
output_folder.mkdir(exist_ok=True)

# Export CSVs
df_combined.to_csv(output_folder / "cleaned_energy_data.csv", index=False)
summary_table.to_csv(output_folder / "building_summary.csv", index=False)

# Text summary
total_campus_consumption = df_combined['kWh'].sum()
highest_consuming_building = summary_table.loc[summary_table['total'].idxmax(), 'Building']
peak_time_row = df_combined.loc[df_combined['kWh'].idxmax()]
peak_time = peak_time_row['Timestamp']
peak_building = peak_time_row['Building']

summary_text = f"""
Campus Energy Consumption Summary
--------------------------------
Total Campus Consumption: {total_campus_consumption:.2f} kWh
Highest-Consuming Building: {highest_consuming_building}
Peak Load Time: {peak_time} (Building: {peak_building})

Daily and Weekly Trends:
- Number of days recorded: {daily_totals['Timestamp'].nunique()}
- Number of weeks recorded: {weekly_totals['Timestamp'].nunique()}
"""

with open(output_folder / "summary.txt", "w") as f:
    f.write(summary_text)

print("\n" + summary_text)
print(f"Cleaned data and summary saved in '{output_folder}' folder.")


