# ============================================================
# Jeeny Amman Full BI Analysis Engine - Fixed Complete Version
# Generates 30 charts, analysis tables, recommendations,
# Excel file, HTML report, and zipped outputs.
# ============================================================

import os
import glob
import zipfile
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")


# ============================================================
# 1. CONFIGURATION
# ============================================================

TARGET_CITY = "Amman"
OUTPUT_DIR = "/content/jeeny_full_bi_outputs"
MIN_OD_TRIPS = 20

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(f"{OUTPUT_DIR}/charts").mkdir(parents=True, exist_ok=True)
Path(f"{OUTPUT_DIR}/tables").mkdir(parents=True, exist_ok=True)
Path(f"{OUTPUT_DIR}/reports").mkdir(parents=True, exist_ok=True)


def find_input_file():
    possible_files = [
        "/content/sample_data/JennyData.csv",
        "/content/sample_data/JeenyData.csv",
        "/content/JennyData.csv",
        "/content/JeenyData.csv",
        "JennyData.csv",
        "JeenyData.csv",
    ]

    for file in possible_files:
        if os.path.exists(file):
            print(f"Dataset found: {file}")
            return file

    all_csv_files = glob.glob("/content/**/*.csv", recursive=True)

    jeeny_like_files = [
        file for file in all_csv_files
        if "jeeny" in os.path.basename(file).lower()
        or "jenny" in os.path.basename(file).lower()
    ]

    if jeeny_like_files:
        selected = jeeny_like_files[0]
        print(f"Dataset found automatically: {selected}")
        return selected

    if all_csv_files:
        selected = max(all_csv_files, key=os.path.getsize)
        print("Exact Jeeny/Jenny file name was not found.")
        print(f"Using largest CSV file instead: {selected}")
        return selected

    raise FileNotFoundError(
        "No CSV file found. Upload JennyData.csv or JeenyData.csv to Colab."
    )


INPUT_FILE = find_input_file()


# ============================================================
# 2. HELPER FUNCTIONS
# ============================================================

def save_chart(fig, name):
    path = f"{OUTPUT_DIR}/charts/{name}.png"
    fig.tight_layout()
    fig.savefig(path, dpi=180, bbox_inches="tight")
    plt.close(fig)
    return path


def save_table(df, name):
    path = f"{OUTPUT_DIR}/tables/{name}.csv"
    df.to_csv(path, index=False, encoding="utf-8-sig")
    return path


def safe_divide(a, b):
    a = pd.to_numeric(a, errors="coerce").fillna(0)
    b = pd.to_numeric(b, errors="coerce").fillna(0)
    return np.where(b == 0, 0, a / b)


def min_max_scale(s):
    s = pd.to_numeric(s, errors="coerce").fillna(0)
    if s.max() == s.min():
        return pd.Series(np.zeros(len(s)), index=s.index)
    return (s - s.min()) / (s.max() - s.min())


def clean_text_columns(df):
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype(str).str.strip()
        df[col] = df[col].replace({"nan": np.nan, "None": np.nan, "": np.nan})
    return df


def bar_chart(df, x, y, title, xlabel, ylabel, filename, top=None, horizontal=False):
    data = df.copy()

    if top:
        data = data.head(top)

    fig, ax = plt.subplots(figsize=(10, 6))

    if horizontal:
        data = data.sort_values(y)
        ax.barh(data[x].astype(str), data[y])
    else:
        ax.bar(data[x].astype(str), data[y])
        ax.tick_params(axis="x", rotation=45)

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    return save_chart(fig, filename)


def line_chart(df, x, y, title, xlabel, ylabel, filename):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df[x], df[y], marker="o")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True, alpha=0.3)
    return save_chart(fig, filename)


def scatter_chart(df, x, y, size_col, title, xlabel, ylabel, filename):
    fig, ax = plt.subplots(figsize=(9, 6))

    sizes = min_max_scale(df[size_col]) * 600 + 50
    ax.scatter(df[x], df[y], s=sizes, alpha=0.65)

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True, alpha=0.3)

    for _, row in df.head(10).iterrows():
        ax.annotate(str(row.get("Pickup_Zone", "")), (row[x], row[y]), fontsize=8)

    return save_chart(fig, filename)


# ============================================================
# 3. LOAD AND CLEAN DATA
# ============================================================

if not os.path.exists(INPUT_FILE):
    raise FileNotFoundError(f"File not found: {INPUT_FILE}")

df = pd.read_csv(INPUT_FILE, low_memory=False)
df = clean_text_columns(df)

print("Dataset loaded successfully")
print("Rows:", len(df))
print("Columns:", list(df.columns))


required_cols = [
    "City",
    "Trip_Time",
    "Fare",
    "Trip_Duration_min",
    "Distance_km",
    "Pickup_Zone",
    "Dropoff_Zone",
    "overall_risk_flag",
    "payment method",
    "IsValidTrip",
    "TripHour",
    "TripMonth",
    "TripWeekday",
    "IsWeekend",
]

missing_cols = [c for c in required_cols if c not in df.columns]

if missing_cols:
    raise ValueError(f"Missing required columns: {missing_cols}")


numeric_cols = [
    "Fare",
    "Trip_Duration_min",
    "Distance_km",
    "IsValidTrip",
    "TripHour",
    "TripMonth",
    "TripWeekday",
    "IsWeekend",
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")


df["Trip_Time"] = pd.to_datetime(df["Trip_Time"], errors="coerce")


# Airport business rule
airport_mask = df["Pickup_Zone"].astype(str).str.contains("airport", case=False, na=False)
df.loc[airport_mask, "City"] = TARGET_CITY


# Feature engineering
df["Hour"] = df["Trip_Time"].dt.hour.fillna(df["TripHour"]).fillna(0).astype(int)
df["Month"] = df["Trip_Time"].dt.month.fillna(df["TripMonth"]).fillna(1).astype(int)
df["Weekday"] = df["Trip_Time"].dt.weekday.fillna(df["TripWeekday"]).fillna(0).astype(int)
df["Date"] = df["Trip_Time"].dt.date

df["Revenue_per_Minute"] = safe_divide(df["Fare"], df["Trip_Duration_min"])
df["Fare_per_Km"] = safe_divide(df["Fare"], df["Distance_km"])
df["Duration_per_Km"] = safe_divide(df["Trip_Duration_min"], df["Distance_km"])

df["IsHighRisk"] = (
    df["overall_risk_flag"]
    .astype(str)
    .str.lower()
    .str.contains("high", na=False)
    .astype(int)
)

if "Peak" in df.columns:
    df["IsPeak"] = pd.to_numeric(df["Peak"], errors="coerce").fillna(0).astype(int)
else:
    df["IsPeak"] = df["Hour"].isin([7, 8, 9, 16, 17, 18, 19]).astype(int)


valid_df = df[df["IsValidTrip"] == 1].copy()
amman = valid_df[valid_df["City"].astype(str).str.lower() == TARGET_CITY.lower()].copy()

print("Valid trips:", len(valid_df))
print("Amman trips:", len(amman))

if amman.empty:
    raise ValueError("No Amman trips found after filtering. Check City values or Airport rule.")


# ============================================================
# 4. DATA QUALITY REPORT
# ============================================================

quality_rows = []

for col in df.columns:
    quality_rows.append({
        "Column": col,
        "Missing_Count": int(df[col].isna().sum()),
        "Missing_Percentage": round(df[col].isna().mean() * 100, 2),
        "Unique_Values": int(df[col].nunique(dropna=True)),
        "Data_Type": str(df[col].dtype),
    })

quality_report = pd.DataFrame(quality_rows)

quality_checks = pd.DataFrame([
    {"Check": "Total Rows", "Value": len(df)},
    {"Check": "Valid Trips", "Value": len(valid_df)},
    {"Check": "Invalid Trips", "Value": int((df["IsValidTrip"] != 1).sum())},
    {"Check": "Missing Trip_Time", "Value": int(df["Trip_Time"].isna().sum())},
    {"Check": "Zero or Negative Fare", "Value": int((df["Fare"] <= 0).sum())},
    {"Check": "Zero or Negative Distance", "Value": int((df["Distance_km"] <= 0).sum())},
    {"Check": "Zero or Negative Duration", "Value": int((df["Trip_Duration_min"] <= 0).sum())},
    {
        "Check": "Airport rows not Amman after rule",
        "Value": int(
            (
                df["Pickup_Zone"].astype(str).str.contains("airport", case=False, na=False)
                & (df["City"] != TARGET_CITY)
            ).sum()
        ),
    },
])

save_table(quality_report, "00_column_quality_report")
save_table(quality_checks, "00_data_quality_checks")


# ============================================================
# 5. CORE ANALYSIS TABLES
# ============================================================

city_summary = valid_df.groupby("City", dropna=False).agg(
    Trips=("City", "count"),
    Revenue=("Fare", "sum"),
    AvgFare=("Fare", "mean"),
    AvgDuration=("Trip_Duration_min", "mean"),
    AvgDistance=("Distance_km", "mean"),
    HighRiskShare=("IsHighRisk", "mean"),
    PeakShare=("IsPeak", "mean"),
).reset_index()

city_summary["TripShare_%"] = 100 * city_summary["Trips"] / city_summary["Trips"].sum()
city_summary["RevenueShare_%"] = 100 * city_summary["Revenue"] / city_summary["Revenue"].sum()
city_summary = city_summary.sort_values("Trips", ascending=False)


zone_summary = amman.groupby("Pickup_Zone").agg(
    Trips=("Pickup_Zone", "count"),
    Revenue=("Fare", "sum"),
    AvgFare=("Fare", "mean"),
    AvgDuration=("Trip_Duration_min", "mean"),
    AvgDistance=("Distance_km", "mean"),
    Revenue_per_Minute=("Revenue_per_Minute", "mean"),
    Fare_per_Km=("Fare_per_Km", "mean"),
    Duration_per_Km=("Duration_per_Km", "mean"),
    HighRiskShare=("IsHighRisk", "mean"),
    PeakShare=("IsPeak", "mean"),
).reset_index()

zone_summary["TripShare_%"] = 100 * zone_summary["Trips"] / zone_summary["Trips"].sum()
zone_summary["RevenueShare_%"] = 100 * zone_summary["Revenue"] / zone_summary["Revenue"].sum()
zone_summary = zone_summary.sort_values("Trips", ascending=False)


hourly_summary = amman.groupby("Hour").agg(
    Trips=("Hour", "count"),
    Revenue=("Fare", "sum"),
    AvgFare=("Fare", "mean"),
    AvgDuration=("Trip_Duration_min", "mean"),
    AvgDistance=("Distance_km", "mean"),
    HighRiskShare=("IsHighRisk", "mean"),
    PeakShare=("IsPeak", "mean"),
).reset_index()


weekday_summary = amman.groupby("Weekday").agg(
    Trips=("Weekday", "count"),
    Revenue=("Fare", "sum"),
    AvgFare=("Fare", "mean"),
    HighRiskShare=("IsHighRisk", "mean"),
).reset_index()

weekday_map = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}
weekday_summary["Weekday_Name"] = weekday_summary["Weekday"].map(weekday_map)


month_summary = amman.groupby("Month").agg(
    Trips=("Month", "count"),
    Revenue=("Fare", "sum"),
    AvgFare=("Fare", "mean"),
    HighRiskShare=("IsHighRisk", "mean"),
).reset_index()


od_summary = amman.groupby(["Pickup_Zone", "Dropoff_Zone"]).agg(
    Trips=("Pickup_Zone", "count"),
    Revenue=("Fare", "sum"),
    AvgFare=("Fare", "mean"),
    AvgDuration=("Trip_Duration_min", "mean"),
    AvgDistance=("Distance_km", "mean"),
    Revenue_per_Minute=("Revenue_per_Minute", "mean"),
    Fare_per_Km=("Fare_per_Km", "mean"),
    Duration_per_Km=("Duration_per_Km", "mean"),
    HighRiskShare=("IsHighRisk", "mean"),
    PeakShare=("IsPeak", "mean"),
).reset_index()

od_summary["TripShare_%"] = 100 * od_summary["Trips"] / od_summary["Trips"].sum()
od_summary["RevenueShare_%"] = 100 * od_summary["Revenue"] / od_summary["Revenue"].sum()
od_summary = od_summary.sort_values("Trips", ascending=False)


payment_summary = amman.groupby("payment method", dropna=False).agg(
    Trips=("payment method", "count"),
    Revenue=("Fare", "sum"),
    AvgFare=("Fare", "mean"),
    AvgDuration=("Trip_Duration_min", "mean"),
    HighRiskShare=("IsHighRisk", "mean"),
).reset_index().sort_values("Trips", ascending=False)


risk_zone = amman.groupby("Pickup_Zone").agg(
    Trips=("Pickup_Zone", "count"),
    HighRiskTrips=("IsHighRisk", "sum"),
    HighRiskShare=("IsHighRisk", "mean"),
    Revenue=("Fare", "sum"),
    AvgDuration=("Trip_Duration_min", "mean"),
).reset_index()

risk_zone["HighRiskShare_%"] = risk_zone["HighRiskShare"] * 100
risk_zone = risk_zone.sort_values("HighRiskShare_%", ascending=False)


zone_hour = amman.groupby(["Pickup_Zone", "Hour"]).agg(
    Trips=("Pickup_Zone", "count"),
    Revenue=("Fare", "sum"),
    AvgFare=("Fare", "mean"),
    AvgDuration=("Trip_Duration_min", "mean"),
    AvgDistance=("Distance_km", "mean"),
    HighRiskShare=("IsHighRisk", "mean"),
    PeakShare=("IsPeak", "mean"),
).reset_index()


save_table(city_summary, "01_city_summary")
save_table(zone_summary, "02_amman_zone_summary")
save_table(hourly_summary, "03_hourly_summary")
save_table(weekday_summary, "04_weekday_summary")
save_table(month_summary, "05_month_summary")
save_table(od_summary, "06_od_summary")
save_table(payment_summary, "07_payment_summary")
save_table(risk_zone, "08_risk_by_zone")
save_table(zone_hour, "09_zone_hour_summary")


# ============================================================
# 6. BOTTLENECK INDEX
# ============================================================

abi = zone_summary.copy()

abi["TripPressure"] = min_max_scale(abi["Trips"])
abi["RevenuePressure"] = min_max_scale(abi["Revenue"])
abi["DurationPressure"] = min_max_scale(abi["AvgDuration"])
abi["DistancePressure"] = min_max_scale(abi["AvgDistance"])
abi["RiskPressure"] = min_max_scale(abi["HighRiskShare"])
abi["PeakPressure"] = min_max_scale(abi["PeakShare"])

abi["ABI"] = (
    0.25 * abi["TripPressure"]
    + 0.15 * abi["RevenuePressure"]
    + 0.15 * abi["DurationPressure"]
    + 0.10 * abi["DistancePressure"]
    + 0.20 * abi["RiskPressure"]
    + 0.15 * abi["PeakPressure"]
)

abi["ABI_0_100"] = (abi["ABI"] * 100).round(2)

abi["Bottleneck_Level"] = pd.cut(
    abi["ABI_0_100"],
    bins=[-1, 35, 60, 100],
    labels=["Low", "Medium", "High"],
)

abi = abi.sort_values("ABI_0_100", ascending=False)
save_table(abi, "10_amman_bottleneck_index")


# ============================================================
# 7. DEMAND PRESSURE TABLE
# ============================================================

demand_pressure = zone_hour.copy()

demand_pressure["TripPressure_%"] = demand_pressure.groupby("Hour")["Trips"].transform(
    lambda x: 100 * x / x.sum()
)

demand_pressure["RiskPressure_%"] = demand_pressure["HighRiskShare"] * 100

demand_pressure["OperationalPressureScore"] = (
    0.50 * min_max_scale(demand_pressure["Trips"])
    + 0.25 * min_max_scale(demand_pressure["Revenue"])
    + 0.25 * min_max_scale(demand_pressure["HighRiskShare"])
) * 100

demand_pressure = demand_pressure.sort_values("OperationalPressureScore", ascending=False)
save_table(demand_pressure, "11_hourly_zone_demand_pressure")


# ============================================================
# 8. DRIVER ALLOCATION RECOMMENDATION
# ============================================================

TOTAL_AVAILABLE_DRIVERS = 100

driver_alloc = demand_pressure.copy()

driver_alloc["DemandScore"] = min_max_scale(driver_alloc["Trips"])
driver_alloc["RiskScore"] = min_max_scale(driver_alloc["HighRiskShare"])
driver_alloc["RevenueScore"] = min_max_scale(driver_alloc["Revenue"])

driver_alloc["AllocationScore"] = (
    0.60 * driver_alloc["DemandScore"]
    + 0.25 * driver_alloc["RiskScore"]
    + 0.15 * driver_alloc["RevenueScore"]
)

driver_alloc["Hour_TotalScore"] = driver_alloc.groupby("Hour")["AllocationScore"].transform("sum")
driver_alloc["Recommended_Driver_Share_%"] = 100 * safe_divide(
    driver_alloc["AllocationScore"], driver_alloc["Hour_TotalScore"]
)

driver_alloc["Recommended_Drivers"] = np.ceil(
    TOTAL_AVAILABLE_DRIVERS * driver_alloc["Recommended_Driver_Share_%"] / 100
).astype(int)

driver_alloc = driver_alloc.sort_values(["Hour", "Recommended_Drivers"], ascending=[True, False])
save_table(driver_alloc, "12_driver_allocation_recommendation")


# ============================================================
# 9. BUSINESS RECOMMENDATIONS
# ============================================================

recommendations = []

top_zone = abi.iloc[0]["Pickup_Zone"] if not abi.empty else "N/A"
top_hour = hourly_summary.sort_values("Trips", ascending=False).iloc[0]["Hour"] if not hourly_summary.empty else "N/A"
top_payment = payment_summary.iloc[0]["payment method"] if not payment_summary.empty else "N/A"

recommendations.append({
    "Area": "Driver Allocation",
    "Finding": f"The strongest operational pressure appears in {top_zone}.",
    "Recommendation": "Increase driver availability in high-ABI zones during peak hours.",
    "Expected Impact": "Lower waiting time, better trip capture, and higher revenue.",
})

recommendations.append({
    "Area": "Peak Hour Management",
    "Finding": f"The highest demand hour is {top_hour}.",
    "Recommendation": "Use targeted driver incentives 30-45 minutes before the peak hour.",
    "Expected Impact": "Better supply-demand balance during demand pressure.",
})

recommendations.append({
    "Area": "Airport Operations",
    "Finding": "Airport pickups were forced into Amman based on the business rule.",
    "Recommendation": "Create a dedicated Airport staging and dispatch policy.",
    "Expected Impact": "Improved airport response time and higher customer satisfaction.",
})

recommendations.append({
    "Area": "Risk Management",
    "Finding": "Some zones have high operational risk share.",
    "Recommendation": "Apply stricter monitoring for high-risk zone-hour combinations.",
    "Expected Impact": "Reduced operational exposure and improved safety.",
})

recommendations.append({
    "Area": "OD Profitability",
    "Finding": "Some OD routes have low revenue per minute.",
    "Recommendation": "Review pricing, driver incentives, or dispatch priority for weak OD corridors.",
    "Expected Impact": "Better driver profitability and route efficiency.",
})

recommendations.append({
    "Area": "Payment Strategy",
    "Finding": f"The dominant payment method is {top_payment}.",
    "Recommendation": "Compare risk and revenue behavior by payment method.",
    "Expected Impact": "Better payment policy and reduced risk exposure.",
})

recommendations_df = pd.DataFrame(recommendations)
save_table(recommendations_df, "13_business_recommendations")


# ============================================================
# 10. DATA IMPROVEMENT SUGGESTIONS
# ============================================================

data_improvements = pd.DataFrame([
    {
        "Data Area": "GPS Coordinates",
        "Current Issue": "Pickup and dropoff zones are categorical only.",
        "Suggested Improvement": "Add pickup_latitude, pickup_longitude, dropoff_latitude, dropoff_longitude.",
        "BI Value": "Enables real heatmaps, route clustering, and spatial bottleneck detection.",
    },
    {
        "Data Area": "Driver Information",
        "Current Issue": "No driver ID, driver acceptance rate, cancellation rate, or availability.",
        "Suggested Improvement": "Add Driver_ID, Driver_Status, Acceptance_Rate, Cancellation_Rate, Online_Minutes.",
        "BI Value": "Supports accurate driver allocation and supply-demand matching.",
    },
    {
        "Data Area": "Customer Information",
        "Current Issue": "Limited customer segmentation.",
        "Suggested Improvement": "Add Customer_ID, Customer_Type, Loyalty_Level, Trip_Frequency.",
        "BI Value": "Improves customer behavior and retention analysis.",
    },
    {
        "Data Area": "Trip Lifecycle",
        "Current Issue": "Only trip time and duration are available.",
        "Suggested Improvement": "Add request_time, driver_accept_time, pickup_time, dropoff_time.",
        "BI Value": "Measures waiting time, pickup delay, and service reliability.",
    },
    {
        "Data Area": "Cancellation Data",
        "Current Issue": "Cancelled trips may not be deeply analyzed.",
        "Suggested Improvement": "Add Cancellation_Flag, Cancellation_Reason, Cancelled_By.",
        "BI Value": "Identifies lost demand and reasons behind failed trips.",
    },
    {
        "Data Area": "Traffic Conditions",
        "Current Issue": "No traffic congestion score.",
        "Suggested Improvement": "Add Traffic_Index or Congestion_Level by zone-hour.",
        "BI Value": "Explains long duration and low route efficiency.",
    },
    {
        "Data Area": "Weather",
        "Current Issue": "Weather effect is not captured.",
        "Suggested Improvement": "Add Weather_Status, Rain_Flag, Temperature.",
        "BI Value": "Improves demand prediction and peak pressure interpretation.",
    },
    {
        "Data Area": "Fare Breakdown",
        "Current Issue": "Fare is available but not detailed.",
        "Suggested Improvement": "Add base_fare, distance_fare, time_fare, surge_multiplier, discount.",
        "BI Value": "Supports pricing analysis and profitability optimization.",
    },
    {
        "Data Area": "Promotions",
        "Current Issue": "No promotion or coupon tracking.",
        "Suggested Improvement": "Add Promo_Code, Discount_Value, Campaign_Name.",
        "BI Value": "Measures marketing effectiveness and revenue leakage.",
    },
    {
        "Data Area": "Service Quality",
        "Current Issue": "No rating or complaint information.",
        "Suggested Improvement": "Add Customer_Rating, Driver_Rating, Complaint_Flag.",
        "BI Value": "Connects operational performance with customer satisfaction.",
    },
    {
        "Data Area": "Data Validation",
        "Current Issue": "Some records may include zero or invalid values.",
        "Suggested Improvement": "Apply automated validation rules for fare, distance, duration, and time.",
        "BI Value": "Improves dashboard trust and analysis accuracy.",
    },
    {
        "Data Area": "Demand Forecasting",
        "Current Issue": "Limited predictive features.",
        "Suggested Improvement": "Add event calendar, holidays, university hours, mall events, airport arrivals.",
        "BI Value": "Improves demand prediction and driver planning.",
    },
])

save_table(data_improvements, "14_data_improvement_suggestions")


# ============================================================
# 11. CREATE 30 CHARTS
# ============================================================

bar_chart(city_summary, "City", "Trips", "Valid Trips by City", "Trips", "City", "01_valid_trips_by_city", horizontal=True)

bar_chart(city_summary, "City", "Revenue", "Revenue by City", "Revenue", "City", "02_revenue_by_city", horizontal=True)

bar_chart(city_summary, "City", "TripShare_%", "Trip Share by City", "Trip Share %", "City", "03_trip_share_by_city", horizontal=True)

bar_chart(zone_summary, "Pickup_Zone", "Trips", "Amman Trips by Pickup Zone", "Trips", "Pickup Zone", "04_amman_trips_by_zone", top=15, horizontal=True)

bar_chart(zone_summary, "Pickup_Zone", "Revenue", "Amman Revenue by Pickup Zone", "Revenue", "Pickup Zone", "05_amman_revenue_by_zone", top=15, horizontal=True)

bar_chart(zone_summary.sort_values("AvgFare", ascending=False), "Pickup_Zone", "AvgFare", "Average Fare by Zone", "Average Fare", "Pickup Zone", "06_avg_fare_by_zone", top=15, horizontal=True)

bar_chart(zone_summary.sort_values("AvgDuration", ascending=False), "Pickup_Zone", "AvgDuration", "Average Duration by Zone", "Average Duration", "Pickup Zone", "07_avg_duration_by_zone", top=15, horizontal=True)

bar_chart(zone_summary.sort_values("AvgDistance", ascending=False), "Pickup_Zone", "AvgDistance", "Average Distance by Zone", "Average Distance", "Pickup Zone", "08_avg_distance_by_zone", top=15, horizontal=True)

bar_chart(zone_summary.sort_values("Revenue_per_Minute", ascending=False), "Pickup_Zone", "Revenue_per_Minute", "Revenue per Minute by Zone", "Revenue per Minute", "Pickup Zone", "09_revenue_per_minute_by_zone", top=15, horizontal=True)

bar_chart(zone_summary.sort_values("Fare_per_Km", ascending=False), "Pickup_Zone", "Fare_per_Km", "Fare per KM by Zone", "Fare per KM", "Pickup Zone", "10_fare_per_km_by_zone", top=15, horizontal=True)

line_chart(hourly_summary, "Hour", "Trips", "Amman Demand by Hour", "Hour", "Trips", "11_hourly_demand")

line_chart(hourly_summary, "Hour", "Revenue", "Amman Revenue by Hour", "Hour", "Revenue", "12_hourly_revenue")

line_chart(hourly_summary, "Hour", "AvgFare", "Average Fare by Hour", "Hour", "Average Fare", "13_avg_fare_by_hour")

line_chart(hourly_summary, "Hour", "HighRiskShare", "High Risk Share by Hour", "Hour", "High Risk Share", "14_high_risk_by_hour")

bar_chart(weekday_summary, "Weekday_Name", "Trips", "Trips by Weekday", "Weekday", "Trips", "15_trips_by_weekday")

bar_chart(weekday_summary, "Weekday_Name", "Revenue", "Revenue by Weekday", "Weekday", "Revenue", "16_revenue_by_weekday")

bar_chart(month_summary, "Month", "Trips", "Trips by Month", "Month", "Trips", "17_trips_by_month")

bar_chart(payment_summary, "payment method", "Trips", "Trips by Payment Method", "Payment Method", "Trips", "18_trips_by_payment_method", horizontal=True)

bar_chart(payment_summary, "payment method", "Revenue", "Revenue by Payment Method", "Payment Method", "Revenue", "19_revenue_by_payment_method", horizontal=True)

bar_chart(risk_zone, "Pickup_Zone", "HighRiskShare_%", "High Risk Share by Zone", "High Risk Share %", "Pickup Zone", "20_high_risk_share_by_zone", top=15, horizontal=True)

bar_chart(abi, "Pickup_Zone", "ABI_0_100", "Amman Bottleneck Index by Zone", "ABI Score", "Pickup Zone", "21_abi_by_zone", top=15, horizontal=True)

scatter_chart(
    zone_summary.sort_values("Trips", ascending=False).head(20),
    "AvgDuration",
    "Revenue_per_Minute",
    "Trips",
    "Zone Efficiency: Duration vs Revenue per Minute",
    "Average Duration",
    "Revenue per Minute",
    "22_zone_efficiency_scatter",
)

scatter_chart(
    zone_summary.sort_values("Trips", ascending=False).head(20),
    "AvgDistance",
    "AvgFare",
    "Trips",
    "Zone Pricing: Distance vs Average Fare",
    "Average Distance",
    "Average Fare",
    "23_zone_pricing_scatter",
)

top_od = od_summary[od_summary["Trips"] >= MIN_OD_TRIPS].sort_values("Trips", ascending=False).head(15).copy()
top_od["OD"] = top_od["Pickup_Zone"].astype(str) + " → " + top_od["Dropoff_Zone"].astype(str)
bar_chart(top_od, "OD", "Trips", "Top OD Pairs by Trips", "Trips", "OD Pair", "24_top_od_by_trips", horizontal=True)

top_od_rev = od_summary[od_summary["Trips"] >= MIN_OD_TRIPS].sort_values("Revenue", ascending=False).head(15).copy()
top_od_rev["OD"] = top_od_rev["Pickup_Zone"].astype(str) + " → " + top_od_rev["Dropoff_Zone"].astype(str)
bar_chart(top_od_rev, "OD", "Revenue", "Top OD Pairs by Revenue", "Revenue", "OD Pair", "25_top_od_by_revenue", horizontal=True)


# Chart 26 - OD Matrix
od_matrix = od_summary.pivot_table(
    index="Pickup_Zone",
    columns="Dropoff_Zone",
    values="Trips",
    aggfunc="sum",
    fill_value=0,
)

fig, ax = plt.subplots(figsize=(10, 8))
im = ax.imshow(od_matrix.values)
ax.set_title("OD Matrix - Trips")
ax.set_xticks(np.arange(len(od_matrix.columns)))
ax.set_yticks(np.arange(len(od_matrix.index)))
ax.set_xticklabels(od_matrix.columns, rotation=45, ha="right")
ax.set_yticklabels(od_matrix.index)
fig.colorbar(im, ax=ax, label="Trips")
save_chart(fig, "26_od_matrix_trips")


# Chart 27 - Zone-Hour Heatmap
zone_hour_matrix = zone_hour.pivot_table(
    index="Pickup_Zone",
    columns="Hour",
    values="Trips",
    aggfunc="sum",
    fill_value=0,
)

fig, ax = plt.subplots(figsize=(12, 7))
im = ax.imshow(zone_hour_matrix.values, aspect="auto")
ax.set_title("Zone-Hour Demand Heatmap")
ax.set_xlabel("Hour")
ax.set_ylabel("Pickup Zone")
ax.set_xticks(np.arange(len(zone_hour_matrix.columns)))
ax.set_yticks(np.arange(len(zone_hour_matrix.index)))
ax.set_xticklabels(zone_hour_matrix.columns)
ax.set_yticklabels(zone_hour_matrix.index)
fig.colorbar(im, ax=ax, label="Trips")
save_chart(fig, "27_zone_hour_demand_heatmap")


# Chart 28 - Fare Distribution
fig, ax = plt.subplots(figsize=(10, 5))
ax.hist(amman["Fare"].dropna(), bins=40)
ax.set_title("Fare Distribution - Amman")
ax.set_xlabel("Fare")
ax.set_ylabel("Frequency")
save_chart(fig, "28_fare_distribution")


# Chart 29 - Duration Distribution
fig, ax = plt.subplots(figsize=(10, 5))
ax.hist(amman["Trip_Duration_min"].dropna(), bins=40)
ax.set_title("Trip Duration Distribution - Amman")
ax.set_xlabel("Duration Minutes")
ax.set_ylabel("Frequency")
save_chart(fig, "29_duration_distribution")


# Chart 30 - Distance Distribution
fig, ax = plt.subplots(figsize=(10, 5))
ax.hist(amman["Distance_km"].dropna(), bins=40)
ax.set_title("Trip Distance Distribution - Amman")
ax.set_xlabel("Distance KM")
ax.set_ylabel("Frequency")
save_chart(fig, "30_distance_distribution")


# ============================================================
# 12. EXCEL OUTPUT
# ============================================================

excel_path = f"{OUTPUT_DIR}/reports/jeeny_full_bi_analysis.xlsx"

with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
    quality_checks.to_excel(writer, sheet_name="Quality Checks", index=False)
    quality_report.to_excel(writer, sheet_name="Column Quality", index=False)
    city_summary.to_excel(writer, sheet_name="City Summary", index=False)
    zone_summary.to_excel(writer, sheet_name="Zone Summary", index=False)
    hourly_summary.to_excel(writer, sheet_name="Hourly Summary", index=False)
    weekday_summary.to_excel(writer, sheet_name="Weekday Summary", index=False)
    month_summary.to_excel(writer, sheet_name="Month Summary", index=False)
    od_summary.to_excel(writer, sheet_name="OD Summary", index=False)
    payment_summary.to_excel(writer, sheet_name="Payment Summary", index=False)
    risk_zone.to_excel(writer, sheet_name="Risk By Zone", index=False)
    abi.to_excel(writer, sheet_name="ABI", index=False)
    demand_pressure.to_excel(writer, sheet_name="Demand Pressure", index=False)
    driver_alloc.to_excel(writer, sheet_name="Driver Allocation", index=False)
    recommendations_df.to_excel(writer, sheet_name="Recommendations", index=False)
    data_improvements.to_excel(writer, sheet_name="Data Improvements", index=False)


# ============================================================
# 13. HTML EXECUTIVE REPORT
# ============================================================

kpis = {
    "Total Records": f"{len(df):,}",
    "Valid Trips": f"{len(valid_df):,}",
    "Amman Trips": f"{len(amman):,}",
    "Amman Share": f"{100 * len(amman) / len(valid_df):.1f}%" if len(valid_df) else "0%",
    "Total Revenue": f"{valid_df['Fare'].sum():,.2f} JOD",
    "Amman Revenue": f"{amman['Fare'].sum():,.2f} JOD",
    "Top Pickup Zone": str(top_zone),
    "Top Demand Hour": str(top_hour),
}

html = f"""
<html>
<head>
    <meta charset="utf-8">
    <title>Jeeny Amman BI Report</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 30px;
            background: #f7f9fb;
            color: #222;
        }}
        h1, h2 {{
            color: #1f2d3d;
        }}
        .kpi-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 14px;
            margin: 20px 0;
        }}
        .kpi {{
            background: white;
            padding: 16px;
            border-radius: 12px;
            border: 1px solid #ddd;
            box-shadow: 0 2px 6px rgba(0,0,0,0.06);
        }}
        .kpi-title {{
            font-size: 13px;
            color: #666;
        }}
        .kpi-value {{
            font-size: 22px;
            font-weight: bold;
            margin-top: 8px;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            background: white;
            margin-bottom: 25px;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
            font-size: 13px;
        }}
        th {{
            background: #e9eef5;
        }}
        .box {{
            background: #fff8d6;
            padding: 15px;
            border-left: 5px solid #d4b000;
            margin-top: 20px;
        }}
    </style>
</head>
<body>

<h1>Jeeny Amman BI Optimization Report</h1>
<p>This report presents a full Python-based business intelligence analysis for Jeeny trips, focusing on Amman operational performance, bottlenecks, risk, demand pressure, OD behavior, and improvement recommendations.</p>

<h2>Executive KPIs</h2>
<div class="kpi-grid">
    {''.join([f'<div class="kpi"><div class="kpi-title">{k}</div><div class="kpi-value">{v}</div></div>' for k, v in kpis.items()])}
</div>

<h2>Top Bottleneck Zones</h2>
{abi.head(10).to_html(index=False)}

<h2>Top Driver Allocation Recommendations</h2>
{driver_alloc.head(15).to_html(index=False)}

<h2>Business Recommendations</h2>
{recommendations_df.to_html(index=False)}

<h2>Data Improvement Suggestions</h2>
{data_improvements.to_html(index=False)}

<div class="box">
<b>Main Recommendation:</b> Start with an Amman pilot focusing on high-ABI zones, airport pickup management, peak-hour driver allocation, and high-risk zone-hour monitoring.
</div>

</body>
</html>
"""

html_path = f"{OUTPUT_DIR}/reports/jeeny_full_bi_report.html"

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)


# ============================================================
# 14. ZIP OUTPUTS
# ============================================================

zip_path = "/content/jeeny_full_bi_outputs.zip"

with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(OUTPUT_DIR):
        for file in files:
            full_path = os.path.join(root, file)
            relative_path = os.path.relpath(full_path, OUTPUT_DIR)
            zipf.write(full_path, relative_path)


# ============================================================
# 15. FINAL PRINT
# ============================================================

print("\nAnalysis completed successfully.")
print("Output folder:", OUTPUT_DIR)
print("\nImportant outputs:")
print("1. Charts folder:", f"{OUTPUT_DIR}/charts")
print("2. Tables folder:", f"{OUTPUT_DIR}/tables")
print("3. Excel file:", excel_path)
print("4. HTML report:", html_path)
print("5. ZIP file:", zip_path)
print("\nTotal charts generated: 30")
