# Jeeny Amman BI Optimization System

An Amman-focused Business Intelligence and operational optimization project for Jeeny ride-hailing data. The project combines Power BI, Python, and Streamlit to support descriptive, predictive, and prescriptive decision-making.

## Project Overview

This project analyzes Jeeny trip data to identify operational pressure, bottlenecks, risk patterns, and driver allocation needs. The main focus is Amman because it has the highest operational and financial impact in the dataset.

## Main Objectives

- Identify dominant cities and pickup zones.
- Detect bottlenecks in Amman, especially Airport operations.
- Analyze hourly demand pressure and peak periods.
- Study origin-destination route efficiency.
- Segment high-risk trips by zone, hour, route, and payment method.
- Build the Amman Bottleneck Index, ABI.
- Recommend driver allocation by zone and hour.
- Present monitoring outputs through Power BI and Streamlit.

## Amman Bottleneck Index, ABI

The ABI is a score from 0 to 100 that combines trip pressure, revenue pressure, duration pressure, distance pressure, risk pressure, and peak pressure. It is calculated at pickup-zone, zone-hour, and OD-pair levels.

## Repository Structure

```text
.
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── docs/
├── data/
├── scripts/
├── dashboard/
├── powerbi/
└── outputs/
```

## Tools Used

- Power BI
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit
- Plotly

## How to Run

Install the required packages:

```bash
pip install -r requirements.txt
```

Place the dataset inside the `data/` folder, then run the Python analytics script from the `scripts/` folder.

Run the Streamlit dashboard:

```bash
streamlit run dashboard/app.py
```

## Key Recommendations

The project recommends prioritizing Amman, building an Airport-centered operational playbook, repositioning drivers before peak hours, monitoring high-risk segments, reviewing weak OD corridors, and using Streamlit as a daily governorate monitoring layer.
