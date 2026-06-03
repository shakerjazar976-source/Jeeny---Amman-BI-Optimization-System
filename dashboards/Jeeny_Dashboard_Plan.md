# Jeeny Multi-Page Dashboard Implementation Plan

## Scope and Goal
Build a professional, dark-themed, executive Power BI report that answers the primary question: **which pickup zone has the most trips** (overall and per city), while also surfacing operational insights on time, fare, distance, payment behavior, and risk segmentation.

Data sources:
- `final_realistic_trip_dataset.csv`
- `GP_Proposal.docx`

## Data Model Design (Single Fact + Date Table)
- Use one fact table: `Trips` from the CSV.
- Create a `Date` dimension from `Trip_Time` (day/month/quarter/year hierarchy).
- Keep star-like simplicity: `Date` (1) -> `Trips` (*) via date key.
- Keep categorical dimensions inside fact for first version: `City`, `Pickup_Zone`, `Dropoff_Zone`, `Gender`, `payment method`, `overall_risk_flag`, `Peak`.

## Power Query Pipeline (in order)
1. Load CSV and enforce UTF-8 parsing.
2. Remove blank rows, promote headers, trim/clean text.
3. Normalize missing markers to null: `""`, `NA`, `N/A`, `null`, `-`.
4. Set data types:
   - Whole number: `Trip_ID`, `Trip_Duration_min`, `Peak`
   - Decimal: `Fare`, `Distance_km`, `avg_price`
   - Date/Time: `Trip_Time`
   - Text: remaining categorical fields
5. Remove duplicates on `Trip_ID` (or fallback to composite key if duplicates are legitimate).
6. Filter invalid operational records:
   - `Fare < 0`, `Distance_km < 0`, `Trip_Duration_min <= 0`, null `Trip_Time`
7. Add quality columns:
   - `IsValidTrip` (1/0)
   - `TripHour`, `TripMonth`, `TripWeekday`, `IsWeekend`
8. Keep a separate `InvalidTrips` query (reference) for audit page.

## Core DAX Measures
- `Total Trips = COUNTROWS(Trips)`
- `Valid Trips = CALCULATE([Total Trips], Trips[IsValidTrip] = 1)`
- `Trip Share % = DIVIDE([Valid Trips], CALCULATE([Valid Trips], ALL(Trips[Pickup_Zone])))`
- `Total Revenue = SUM(Trips[Fare])`
- `Avg Fare = AVERAGE(Trips[Fare])`
- `Avg Distance = AVERAGE(Trips[Distance_km])`
- `Avg Duration = AVERAGE(Trips[Trip_Duration_min])`
- `Trips Peak = CALCULATE([Valid Trips], Trips[Peak] = 1)`
- `Peak Share % = DIVIDE([Trips Peak], [Valid Trips])`
- `Top Pickup Zone = CONCATENATEX(TOPN(1, VALUES(Trips[Pickup_Zone]), [Valid Trips], DESC), Trips[Pickup_Zone], ", ")`
- `Top Zone Trips = MAXX(TOPN(1, VALUES(Trips[Pickup_Zone]), [Valid Trips], DESC), [Valid Trips])`

## 7-Page Dashboard Blueprint

## Page 1 - Executive Overview
- KPI cards: `Valid Trips`, `Total Revenue`, `Avg Fare`, `Avg Distance`, `Top Pickup Zone`.
- Bar chart: trips by `Pickup_Zone` (descending).
- Clustered bar: trips by `City`.
- Slicers: `City`, `Gender`, `payment method`, `overall_risk_flag`, date range.

## Page 2 - Zone Dominance (Primary Objective)
- Main visual: ranked bar of `Pickup_Zone` by `Valid Trips`.
- Matrix: `City` x `Pickup_Zone` with trips and share %.
- Heatmap-style matrix (conditional formatting) to show high-demand zones.
- Card callout: top zone per current filter + trips + share %.

## Page 3 - City Deep Dive
- Decomposition tree or drillable visual: `City -> Pickup_Zone -> Dropoff_Zone` by trips.
- Small multiples: zone demand pattern per city.
- Compare KPIs by city: trips, fare, distance, peak share.

## Page 4 - Time Intelligence
- Line chart: monthly trend of `Valid Trips`.
- Line/area by hour: demand curve across 24h (`TripHour`).
- Weekday vs weekend comparison.
- Peak vs non-peak trip distribution.

## Page 5 - Financial & Efficiency
- Scatter: `Distance_km` vs `Fare` (size by trips, color by city/zone).
- Box/column proxy: fare distribution by zone.
- Duration efficiency: avg duration by zone/city and potential outliers.

## Page 6 - Customer & Risk Segmentation
- Stacked bars: trips by `Gender` within city/zone.
- Payment mix (`Cash/Visa/Wallet`) by zone and city.
- Risk profile view: `overall_risk_flag` by zone and payment.
- Interaction focus: identify whether top zones are tied to specific risk/payment patterns.

## Page 7 - Data Quality & Audit
- KPI cards: total records, valid records, invalid records, duplicate count removed.
- Breakdown chart of invalid reasons (negative fare, negative distance, null time, non-positive duration).
- Table of sample invalid trips for transparency.

## Interaction and UX Standards
- Global slicer panel (synced where relevant): date, city, gender, payment, risk.
- Drill-through target page for zone details (`Pickup_Zone` context).
- Consistent dark theme, semantic color palette (e.g., highlight top zones in accent color).
- Dynamic titles reflecting slicer context (e.g., "Top Pickup Zones - Amman - 2024").

## Validation and Acceptance Criteria
- Primary question answered in <=10 seconds: top pickup zone overall and per city.
- All KPI totals reconcile with filtered table counts.
- Time trend and zone rankings remain consistent under slicers.
- Invalid records excluded from business KPIs but visible on audit page.

## Delivery Sequence
1. Power Query cleaning + quality flags.
2. Date table + relationships + DAX measures.
3. Build pages 1-2 first (core objective), validate with stakeholder.
4. Build pages 3-7 and finalize theme/interactions.
5. Final QA and performance tuning (remove unnecessary columns, optimize visuals/measures).
