# CAPSTONE PROJECT: Campus Energy Dashboard

**Submitted by:** Kaushal 

**Roll Number:** 2501730085

**Course:** Programming for Problem Solving using Python 

**Assignment Title:**  End-to-End Energy Consumption Analysis and Visualization

**Submission Date:** 4 Dec, 2025

## Objective
The goal of this project is to analyze and visualize electricity consumption across campus buildings. By building a Python-based end-to-end dashboard, we provide insights into energy usage patterns, peak consumption periods, and building-wise summaries to support energy-saving decisions.

---

## Dataset
The project uses CSV files containing meter readings for each building per month. Each CSV file includes the following columns:

- `Timestamp` – Date and time of the meter reading (format: YYYY-MM-DD HH:MM)
- `kWh` – Electricity consumption in kilowatt-hours
- `Building` – Name of the building
- `Month` – Month of the reading

**Sample CSV files included in `/data/` folder:**

- `BuildingA_Jan.csv`
- `BuildingA_Feb.csv`
- `BuildingB_Feb.csv`

---

## Methodology

1. **Data Ingestion and Cleaning (Task 1)**  
   - Automatically read all CSV files in the `/data/` folder.
   - Handle missing or corrupt rows.
   - Add metadata for building name and month if not present.
   - Clean timestamps and remove invalid rows.

2. **Aggregation Logic (Task 2)**  
   - Calculate daily and weekly electricity consumption per building.
   - Generate building-wise summary statistics (mean, min, max, total).

3. **Object-Oriented Modeling (Task 3)**  
   - Implement `MeterReading`, `Building`, and `BuildingManager` classes.
   - Store readings per building and generate reports.

4. **Visualization (Task 4)**  
   - Create a single dashboard PNG with:
     - Trend Line: Daily consumption per building
     - Bar Chart: Average weekly usage
     - Scatter Plot: Peak-hour consumption

5. **Persistence and Executive Summary (Task 5)**  
   - Export cleaned data and summary statistics as CSV files in `/output/`.
   - Generate a concise text report (`summary.txt`) including:
     - Total campus consumption
     - Highest-consuming building
     - Peak load time
     - Number of days/weeks recorded

---

## Files in the Repository

Campus_Energy_Dashboard/
├── data/
├── output/
│   ├── cleaned_energy_data.csv
│   ├── building_summary.csv
│   └── summary.txt
├── task1_ingest.py

├── dashboard.png

