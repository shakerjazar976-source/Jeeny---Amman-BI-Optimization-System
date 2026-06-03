# Chapter 03: Research Methodology

## Research Problem Statement

The core of the business problem is that there is an uneven distribution of trip demands, revenue, risk exposure, and efficient travel paths across different cities, picking up zones, periods of the day, and origin destination pairs. Visualizing the past is easy using just a simple BI dashboard; however, a full BI project has to go further and identify the bottleneck, understand its importance, and suggest actionable insights.

For this purpose, the project integrates three separate components. The first component uses Power BI with features such as executive visualizations, slicers, KPI cards, city-level demand visualizations, dominance by zones, and city-level deep dive analysis. The second component uses Python for creating an analytics engine to clean the dataset, engineering new variables, finding bottleneck scores, identifying least efficient paths, suggesting better driver allocations, and exporting the results as reusable tables and charts. Finally, the third component is the Streamlit Dashboard, which shows all relevant visualizations including the Governorates Heatmap and operational KPIs.

This RM document outlines a methodology starting from the data processing step all the way through visualization and optimization output generation process. Also included in this document are the actual output table and chart names.

## Research Objectives

The main objective of this project is to convert trip records into actionable BI insights that support operational decisions. The project is not limited to descriptive graphs. It aims to connect Power BI exploration with Python-based optimization and a Streamlit executive dashboard.

The objectives below were used to guide the full methodology and output structure.

Identify which Jordanian cities and governorates dominate total trips and revenue.

Detect the strongest pickup-zone bottlenecks inside Amman, especially the Airport node.

Measure demand pressure by hour and highlight peak windows that need driver pre-positioning.

Rank OD pairs by trips, revenue, average duration, fare per kilometer, and revenue per minute.

Segment high-risk trips by pickup zone, dropoff zone, hour, payment method, and OD pair.

Build an Amman Bottleneck Index (ABI) that combines volume, revenue, duration, distance, risk, and peak pressure.

Generate driver allocation recommendations and what-if scenarios that convert the analysis into an operational plan.

Create a one-page Streamlit dashboard with a Jordan heatmap, KPIs, bottleneck rankings, and recommendations.

## BI Research Design

The research design applies an analytical research approach. The data set is considered to be an operational log of Jeeny's activities, while the study utilizes BI platforms to address the questions that arise. The research design includes three main steps – data preprocessing, followed by dashboard exploration and finally ending up in predictive/prescriptive modeling.

There is a layering strategy in place in order to achieve a complex research approach. Power BI is used to create visualization and storyboards for executives. Python is applied for cleansing, feature engineering, scoring and forecasting, and scenarios analysis. Finally, Streamlit provides an easy-to-use interface where the Jordan map, KPIs, risks and recommendations can all be found on the same page.

This approach makes the study different from a regular dashboard as the project moves from descriptive analytics towards diagnostics, predictive and prescriptive analytics.

Descriptive analytics: trips, revenue, average fare, zone shares, and hourly demand.

Diagnostic analytics: airport concentration, OD matrix, risk segmentation, and efficiency comparison.

Predictive analytics: hourly-zone demand estimation and demand pressure outputs.

Prescriptive analytics: driver allocation, what-if scenarios, and BI recommendations.

## Dataset Description

The data set which is used in the methodology consists of 79,626 observations with the following key columns: external_id, Gender, overall_risk_flag, payment method, avg_price, City, Trip_ID, Trip_Time, Fare, Trip_Duration_min, Distance_km, Pickup_Zone, Dropoff_Zone, Peak, IsValidTrip, TripHour, TripMonth, TripWeekday, IsWeekend, and InvalidReason.

The data set shows operation patterns where the city of Amman is dominant, Airport serves as the top pickup bottleneck, the evening time shows evident pressures, and the efficiency of route usage depends on OD pairs.

It can be used for business intelligence as it consists of both categorical dimensions and numeric measures.

**Table 1. City-level summary from the final working dataset.**

| City | Trips | Revenue | AvgFare | AvgDuration | AvgDistance | HighRiskPct |
| --- | --- | --- | --- | --- | --- | --- |
| Amman | 46,384 | 142,351.44 | 3.07 | 56.15 | 16.97 | 63.8 |
| Irbid | 10,703 | 19,428.48 | 1.82 | 28.65 | 9.45 | 51.3 |
| Zarqa | 8,340 | 18,734.73 | 2.25 | 34.33 | 11.74 | 53.1 |
| Aqaba | 6,142 | 31,432.94 | 5.12 | 31.31 | 14.58 | 44.1 |
| Karak | 3,535 | 5,681.01 | 1.61 | 27.25 | 8.77 | 51.3 |
| Madaba | 2,109 | 4,307.96 | 2.04 | 28.38 | 9.87 | 49.0 |
| Jerash | 1,624 | 3,177.48 | 1.96 | 27.05 | 9.22 | 50.1 |
| Mafraq | 789 | 991.92 | 1.26 | 25.14 | 10.59 | 64.8 |

## Data Dictionary and Variable Roles

Each of the fields was allocated a BI role. There were two categories: some of them were selected as dimensions to be filtered or grouped, others – as measures that would allow calculating the key performance indicators. It is essential to distinguish between these roles because Power BI and Python need them to perform the analysis and score operations.

For instance, the Trip_ID serves as a transaction ID. City, Pickup_Zone, and Dropoff_Zone represent spatial dimensions. As for temporal dimensions, these are Trip_Time and TripHour. Operational and financial performance is measured by such fields as Fare, Distance_km, and Trip_Duration_min. Risk intelligence is supported by risk flag and payment methods. IsValidTrip is set to filter out invalid data from further analysis.

**Table 2. Data dictionary and BI role mapping.**

| Column | BI Role | Use in the project |
| --- | --- | --- |
| City | Geographic dimension | Used for city dominance and Jordan heatmap analysis |
| Pickup_Zone | Operational dimension | Used for bottleneck, risk, and driver allocation analysis |
| Dropoff_Zone | Operational dimension | Used for OD flow and route efficiency analysis |
| Trip_Time / TripHour | Time dimension | Used for peak-hour demand and revenue analysis |
| Fare | Financial measure | Used for total revenue, average fare, and fare efficiency |
| Trip_Duration_min | Time measure | Used as congestion and efficiency proxy |
| Distance_km | Distance measure | Used for fare per km and duration per km |
| overall_risk_flag | Risk dimension | Used for high-risk segmentation |
| payment method | Customer/payment dimension | Used for risk and payment behavior analysis |

## Data Cleaning Methodology

The cleaning process follows the order of tasks for practical BI preparation steps. Python scripts start by loading the dataset from CSV format, normalizing text fields, verifying the presence of necessary columns, transforming numeric fields, parsing the date-time field of Trip_Time, and creating calculated measures. These actions ensure that Power BI and Streamlit receive structured datasets following the same logic and that the exported tables will be built based on the same logic.

One important cleaning rule was created for Airport trips records. All rows with the value Airport for Pickup Zone will have Amman as a city. This rule is necessary due to the business requirement stating that airport-related trips must be considered part of Amman's operations network. Otherwise, there would be an issue in the bottleneck analysis for Amman.

Data quality assurance is performed to ensure that invalid or unreasonable values (such as fares, distance, and duration being equal to zero or negative numbers) do not distort results. The data-quality reports from the code prove that the dashboard research does not rely on invalid raw data.

Normalize text columns and remove empty string artifacts.

Convert Fare, Trip_Duration_min, Distance_km, IsValidTrip, TripHour, TripMonth, TripWeekday, and IsWeekend into numeric fields.

Convert Trip_Time into datetime format and extract Hour, Month, Weekday, and Date.

Apply the Airport-to-Amman business rule.

Create Revenue_per_Minute, Fare_per_Km, Duration_per_Km, IsHighRisk, and IsPeak.

Export quality reports and cleaned analytical tables.

## Data Quality Checks

The data quality check stage is necessary because BI dashboard visualization can mislead users if the dataset has nulls, inconsistent text labels, wrong durations, duplicate IDs, and zeros. For this reason, the Python Engine provides two initial outputs: 00_data_quality_checks and 00_column_quality_report.

00_data_quality_checks provide information on checks related to the business logic, such as the number of observations, valid trips, invalid trips, duplicates, airport observations not belonging to Amman, zeros/minus in fare, zeros/minus in distance, and zeros/minus in duration. 00_column_quality_report provides a summary for every column in terms of number of missing, percentage of missing, number of unique, and datatype.

These two outputs are valuable during the final research as they show that the work is done following the steps of an organized analytics approach and not by directly constructing visuals out of raw data.

**Table 3. Data quality outputs used in the methodology.**

| Output / Check | Type | Purpose |
| --- | --- | --- |
| 00_data_quality_checks | CSV table | Overall validation checks before analysis |
| 00_column_quality_report | CSV table | Column-level missingness, uniqueness, and data type report |
| Zero or negative fare/distance/duration | Quality rule | Flags values that can distort efficiency metrics |

## Power BI Methodology

Power BI was chosen as the primary visual layer for executive dashboards. As can be seen from the dashboard screens, the report features slicers based on City, Gender, Payment Method, Risk Flag, and Trip_Time parameters. Slicers enable users to single out particular operation segments for comparison under different filters.

The Power BI dashboard features KPI cards that provide information about the number of valid trips, revenue, average fare and average distance, and a top pick-up zone. It also features bar charts of valid trips by pickup zone and valid trips by city. Thus, there is an instant overview of the demand concentration.

Zone Dominance features such information as the top pick-up zone, top zones' trips, the trip share %, pickup zone bars, and origin/destination matrix. City Deep Dive features logic in the decomposition tree form to break down the total number of trips to city, pickup zone, and drop-off zone level.

**Figure 1. Power BI executive dashboard showing KPIs, filters, pickup zones, and city trips.**

## Python Analytics Methodology

Python served as the analytic engine that powered the BI project. Although Power BI was used mainly for visualizing the BI, Python could be used more effectively for consistent data cleanup, feature engineering, scoring, predictions, driving allocation logic, and automatic exporting of results. The results generated by the scripts include CSV tables, PNG visuals, Excel files, and HTML files.

Two engines for Python were created. First was Jeeny Amman BI Optimization Engine which creates outputs such as bottleneck scoring, demand prediction, driver allocation, and what-if scenarios. The other engine created is the Jeeny Amman Full BI Analysis Engine which creates outputs in a more extensive analytical package of 30 graphs, 14 tables, Excel, HTML report, recommendations, and data improvements.

Using Python also increases the reliability of our analysis. In case our dataset changes, we may rerun the scripts to generate new tables and graphs under the same file names and structures.

**Table 4. Python and Streamlit components used in the methodology.**

| Component | Type | Main outputs |
| --- | --- | --- |
| Jeeny Amman BI Optimization Engine | Optimization-focused script | ABI, demand prediction, driver allocation, what-if scenarios, executive KPIs |
| Jeeny Amman Full BI Analysis Engine | Full analytical package | 30 charts, analysis tables, recommendations, Excel, HTML report |
| Streamlit Jordan BI Map Dashboard | Interactive app | One-page map, KPIs, heatmap, airport snapshot, driver allocation |

## Feature Engineering

Feature engineering converts raw trip fields into analytical measures. The project uses several derived indicators that are essential for business interpretation. Revenue per minute measures the financial return for each minute of driver time. Fare per kilometer measures price intensity. Duration per kilometer measures congestion or slowness. IsHighRisk converts the textual risk flag into a binary analytical field. IsPeak identifies peak-hour observations.

These features allow the project to move beyond simple trip counts. For example, a route may have many trips but weak revenue per minute, meaning it consumes driver time without strong financial return. Another route may have fewer trips but high fare per kilometer and low duration per kilometer, making it operationally attractive.

The feature engineering logic is applied consistently across Power BI exports, Python tables, and Streamlit dashboard calculations.

**Table 5. Engineered metrics used in the BI methodology.**

| Engineered metric | Formula / rule | Business meaning |
| --- | --- | --- |
| Revenue_per_Minute | Fare / Trip_Duration_min | Measures route profitability per time unit |
| Fare_per_Km | Fare / Distance_km | Measures pricing intensity by distance |
| Duration_per_Km | Trip_Duration_min / Distance_km | Measures congestion or slow movement |
| IsHighRisk | 1 if risk flag contains High | Supports risk segmentation |
| IsPeak | 1 if trip is in peak periods | Supports peak pressure and driver allocation |

## KPI Definitions

KPI layer is built to help the manager to understand the output easily. The same definitions of KPIs apply to both Power BI and Streamlit reports. Consistency is crucial because otherwise, the user would face different meanings of the same metric in different tools.

It is essential to highlight that the KPIs on the dashboard serve more than description purposes. They contribute to bottleneck analysis too. For instance, high Amman share reflects the presence of urban bias. Similarly, high airport share reflects the presence of zone bias. High average duration means time pressure. Risk share reflects operational exposure.

**Table 6. KPI definitions for Power BI and Streamlit.**

| KPI | Calculation | Business interpretation |
| --- | --- | --- |
| Valid Trips | Count of records where IsValidTrip = 1 | Total operational volume |
| Total Revenue | Sum of Fare | Financial size of the segment |
| Average Fare | Mean of Fare | Average earning per trip |
| Average Distance | Mean of Distance_km | Average trip length |
| Average Duration | Mean of Trip_Duration_min | Time cost and congestion proxy |
| High Risk Share | Mean of IsHighRisk | Risk exposure percentage |
| Top Pickup Zone | Pickup zone with highest trip count | Main demand concentration |

## Amman Bottleneck Index (ABI)

The Amman Bottleneck Index is the central analytical score in the project. It combines multiple pressure dimensions into one score from 0 to 100. The purpose is to rank zones, zone-hour combinations, and OD pairs by operational pressure rather than looking at one metric at a time.

The ABI uses weighted components: trip pressure, revenue pressure, duration pressure, distance pressure, risk pressure, and peak pressure. These components were min-max scaled so that different units can be compared. A high ABI score indicates that a segment has strong operational importance or pressure and should be prioritized for intervention.

The selected weights reflect the project logic. Trips and risk receive high weight because the business problem is about demand concentration and operational exposure. Revenue, duration, distance, and peak pressure provide additional context for prioritization.

**Table 7. ABI scoring components and weights.**

| ABI component | Weight | Reason for inclusion |
| --- | --- | --- |
| Trip pressure | 0.25 | How much demand is concentrated in the segment |
| Revenue pressure | 0.15 | How financially important the segment is |
| Duration pressure | 0.15 | How much time pressure the segment creates |
| Distance pressure | 0.10 | How much travel distance the segment consumes |
| Risk pressure | 0.20 | How much high-risk exposure is present |
| Peak pressure | 0.15 | How much the segment appears in peak windows |

## ABI Output Levels

The ABI was calculated at multiple analytical levels so that the business can act at different levels of detail. The pickup-zone ABI supports broad zone prioritization. The zone-hour ABI supports shift planning and driver pre-positioning. The OD-pair ABI supports route-specific intervention.

This is important because a single zone can be important overall but not equally important at every hour. Similarly, a zone may be acceptable overall but contain one or two weak OD routes that require pricing or dispatch review. Multi-level scoring prevents the analysis from being too general.

The project outputs three main ABI files: 07_abi_by_pickup_zone.csv, 08_abi_by_zone_hour.csv, and 09_abi_by_od_pair.csv. These tables should be inserted into the appendix or used to create additional Power BI visuals.

**Table 8. ABI output levels.**

| Output table | Level | Use in the research |
| --- | --- | --- |
| 07_abi_by_pickup_zone.csv | Pickup_Zone | Ranks Amman pickup zones by overall bottleneck pressure |
| 08_abi_by_zone_hour.csv | Pickup_Zone + Hour | Shows when each zone needs operational attention |
| 09_abi_by_od_pair.csv | Pickup_Zone + Dropoff_Zone | Ranks routes by bottleneck and efficiency pressure |

## Demand Prediction Methodology

Demand forecasting predicts the number of rides in each pickup zone for each hour. First, the script generates a table called daily_zone_hour containing all rides made in Amman on different days. Second, it tries to employ Random Forest Regression using the following features: pickup zone, hour of the day, weekday, and weekend. The code will fallback to historical demand average if the random forest regressor model is not available.

It is not meant to say that we have a sophisticated demand forecasting tool in this section. It is meant to demonstrate that the BI system can shift from the "what has happened" stage to the "what will happen" stage in order to assist in better driver planning, as Jeeny needs to position drivers beforehand.

**Table 10_hourly_zone_demand_prediction will contain forecasted demand per pickup zone and hour.**

Input features: Pickup_Zone, Hour, Weekday, and IsWeekend.

Target variable: daily-zone-hour trip count.

Primary model: RandomForestRegressor with one-hot encoding for pickup zones.

Fallback model: historical average by zone and hour.

Output: predicted trips by zone-hour segment.

## Driver Allocation Recommendation

The driver allocation model determines the allocation recommendation based on the calculated demand level and ABI pressure. It is the part that gives recommendations and therefore is prescriptive. Rather than just stating that the Airport has a high demand level, it offers a driver allocation recommendation on an hourly basis for each zone.

The driver allocation score calculation requires demand and bottleneck scores to be combined using weights. Demand scores are calculated based on predictions while bottleneck scores are calculated based on zone-hour ABIs. An allocation score is then converted into a driver allocation recommendation expressed as a percentage and as the number of drivers.

One of the key deliverables of the project is the table titled "table 11_driver_allocation_recommendation.csv".

**Table 9. Driver allocation methodology fields.**

| Field | Calculation | Interpretation |
| --- | --- | --- |
| DemandScore | Scaled predicted trips | Captures expected demand volume |
| BottleneckScore | Scaled ABI score | Captures operational pressure |
| AllocationScore | 0.65*DemandScore + 0.35*BottleneckScore | Balances demand and risk/pressure |
| Recommended_Driver_Share_% | Segment score / total hour score | Percent of available drivers by hour |
| Recommended_Drivers | Driver share * total drivers | Operational staffing recommendation |

## What-if Scenario Analysis

What-if scenarios are designed to prove how the BI solution would assist with decision making in managing business processes. These scenarios are not meant to substitute experiments in reality; rather, they are meant to give managers an idea of what effects their activities may cause in terms of business performance.

Among others, the optimization engine contains what-if scenarios for Airport driver pre-positioning, low-efficiency route fare or incentive revision, risk control policy, and peak hour dispatch campaigns. They each contain Business Logic, Affected Segment, Hypothesis, Additional Trips/Revenue from Hypothesis, and BI Recommendations.

The output table 12_what_if_scenarios.csv should be included in the report.

**Table 10. What-if scenario structure.**

| Scenario | Affected segment | Purpose |
| --- | --- | --- |
| Airport driver pre-positioning +20% | Airport pickups | Estimate added trips and revenue from better supply positioning |
| Low-efficiency route fare/incentive review | Bottom OD pairs by revenue/minute | Estimate revenue improvement from pricing or incentive action |
| Risk-control policy | High-risk Amman trips | Estimate reduction in high-risk exposure |
| Peak-hour dispatch campaign | Top demand hours | Estimate added trips from targeted driver prompts |

## Streamlit Jordan BI Map Dashboard

Streamlit Dashboard was created with the idea of developing it in the form of an executive one-page interface. It differs from Power BI, where there may be several pages for one report. The Streamlit Dashboard allows you to show the most important information from maps and KPIs on one page. It helps in rapid operation monitoring or demonstrations.

The Streamlit application features a reduced Jordan map based on polygon coordinates. The map can be painted according to Trips, Revenue, High Risk %, Average Fare, Average Distance, or Average Duration. There are also filters such as governorates, pickup zone, risk flag, payment type, and trip hour available in the dashboard.

Governorate KPIs, Amman share, Airport trips share, high-risk share, top bottleneck governorates, Airport control snapshot, hourly demand, risk by governorate, top OD pairs, driver allocation, and automatic BI recommendations were calculated within the Streamlit dashboard.

Interactive Jordan governorate heatmap.

Executive KPI grid.

Airport Control Snapshot.

Top Bottleneck Governorates table.

Risk by Governorate table.

Top Origin-Destination pairs.

Driver allocation recommendation by selected hour.

Downloadable governorate KPI table.

## Colab Deployment Methodology

The design of the Streamlit dashboard was made such that it would run on Google Colab. The Google Colab code would install the required packages including Streamlit, pandas, numpy, matplotlib, and cloudflared. Then, the Streamlit app would be run on port 8501, and a temporary public tunnel set up by cloudflared.

It will be convenient for the students since it eliminates issues with installing locally. In addition, the Streamlit dashboard will be shown using a link from a browser. All that the user needs is to upload the Python file with the dashboard code and the final CSV file.

When running the Colab code, the output will wait for a trycloudflare.com URL to appear. Once it shows, the dashboard can be accessed directly. Otherwise, one can try rerunning the Colab cell or viewing its ports.

**Table 11. Streamlit Colab deployment components.**

| File / component | Role |
| --- | --- |
| jeeny_jordan_map_dashboard.py | Streamlit application file |
| final_realistic_trip_dataset_wide_gaps.csv | Final dataset used by the dashboard |
| run_jeeny_map_dashboard_colab.py | Colab run script |
| cloudflared tunnel | Temporary public dashboard link |
