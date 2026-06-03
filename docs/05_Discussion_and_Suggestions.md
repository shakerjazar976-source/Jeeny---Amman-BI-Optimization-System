# Chapter 05: Discussion Overview and Suggestions

## Solution Evidence Baseline

To recommend the proposed steps for solving the problem, the findings need to be put into a baseline format. The baseline will verify where the solution can begin from, as well as which variables need to be tracked throughout the process. It is crucial to conclude that Amman should be chosen to implement the solution due to its significant trip share and revenue share.

**Table 13. City evidence supporting the improvement pilot.**

| City | Trips | Revenue (JOD) | Trip Share | Revenue Share | High Risk Share |
| --- | --- | --- | --- | --- | --- |
| Amman | 44,802 | 135,458.99 | 56.27% | 68.15% | 0.51 |
| Irbid | 11,273 | 19,240.94 | 14.16% | 9.68% | 0.43 |
| Zarqa | 8,887 | 16,731.40 | 11.16% | 8.42% | 0.43 |
| Aqaba | 5,912 | 13,683.18 | 7.42% | 6.88% | 0.43 |
| Karak | 3,639 | 5,561.49 | 4.57% | 2.80% | 0.42 |

Interpretation. The Airport zone has an ABI score of 85.48, which is far above Downtown and Business District. This means the solution should not be written as a general recommendation only. It should become a practical airport-centered program that can later be scaled to other zones and governorates.

**Table 14. Baseline bottleneck evidence by pickup zone.**

## Solutions structure

**Table 15. Solution structure used in this chapter.**

| Solution Step | Main Decision | Operational Purpose |
| --- | --- | --- |
| Step 1 | Distribute the sufficient number of drivers | Reduce demand-supply mismatch by zone and hour. |
| Step 2 | Segment customers/trips into risk groups | Make dispatch and monitoring risk-aware. |
| Step 3 | Check whether fare and revenue cover operational cost | Identify weak corridors and pricing/incentive review needs. |
| Step 4 | Monitor governorates through Streamlit | Keep Amman and other cities visible in one executive control page. |
| Step 5 | Adopt peak-hour plans as a pilot | Test pre-positioning before scaling the model. |

In this Section, the above solutions are put into well-defined implementation steps. The section utilizes the findings made by the project so far such as: Amman is the best improvement pilot city; Airport is the most significant bottleneck; peak hour issues are confined to specific time intervals; OD flows need profit analysis; and finally, risk should be considered when making decisions.

| Final solution direction Start with an Amman Airport pilot, distribute drivers before peak demand, classify trips by risk, review low-efficiency fare corridors, and use Streamlit as the daily governorate monitoring layer. |
| --- |

## Step 1: Distribution of the Sufficient Number of Drivers

Driver allocation represents the prescriptive portion of the BI solution. It translates the results of demand and bottleneck analysis to action plans. As opposed to stating that Airport has very high demand, the table will indicate how many drivers should be allocated to each zone for the chosen hour.

**Table 16. Recommended driver allocation at Hour 21.**

| Pickup_Zone | Hour | Trips | Revenue | HighRiskShare | OperationalPressureScore | Recommended_Driver_Share_% | Recommended_Drivers |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Airport | 21 | 1,224 | 5,437.69 | 0.66 | 95.53 | 37.70 | 38 |
| Downtown | 21 | 607 | 1,637.35 | 0.46 | 46.46 | 18.33 | 18 |
| Business District | 21 | 526 | 1,480.80 | 0.48 | 42.98 | 16.96 | 17 |
| Mall Area | 21 | 447 | 1,163.93 | 0.43 | 36.23 | 14.30 | 14 |
| Residential | 21 | 328 | 833.74 | 0.49 | 32.22 | 12.71 | 13 |

**Figure 12. Recommended Driver Share by Zone - Hour 21.**

**Figure 12 and Table 16 illustrate an example of the operational use of the proposed logic. At Hour 21, the highest percentage of drivers recommended for deployment is at Airport, followed by other stronger zones. It is essential to note that it enables the translation of BI results into staffing decisions. Such information can be useful for dispatch managers in deciding where driver prompts, incentives, and staging instructions should be deployed.**

The suggested allocation model needs to be implemented as support to managerial decision-making process, not as a mandatory model. In practice, it would require adjustment of suggested percentages based on the number of active drivers, cancellations, traffic, and flights' arrivals. Nevertheless, the existing allocation model, regardless of the inclusion of additional factors, represents a good basis for mitigating the issue of supply-demand mismatch.

## Step 2: Customer and Trip Segmentation Based on Risk

Addressing the problem. A demand-only approach could generate additional issues when drivers who enter high-risk sectors in higher numbers are not regulated. The report demonstrates that Airport is the area with the largest proportion of high-risk drivers, therefore, the enhancement strategy needs to categorize rides based on their level of risk.

**Table 17. Risk evidence by pickup zone.**

| Pickup Zone | Trips | High Risk Trips | High Risk Share | Revenue | Avg Duration |
| --- | --- | --- | --- | --- | --- |
| Airport | 15,352 | 9,716 | 63.29% | 64,162.06 | 64.39 |
| Mall Area | 7,182 | 3,177 | 44.24% | 16,990.55 | 35.23 |
| Residential | 4,932 | 2,180 | 44.20% | 11,386.35 | 34.21 |
| Downtown | 9,362 | 4,125 | 44.06% | 22,699.22 | 36.32 |
| Business District | 7,974 | 3,509 | 44.01% | 20,220.81 | 38.38 |

**Table 18. Proposed risk-based customer/trip groups.**

| Risk Group | Classification Logic | Operational Treatment |
| --- | --- | --- |
| Group A: Low Risk | Non-peak, normal distance, non-risk flag, stable payment behavior. | Standard dispatch with normal monitoring. |
| Group B: Medium Risk | Normal route but peak-hour pressure, or moderate risk share in the zone. | Monitor zone-hour dashboard and keep backup support. |
| Group C: High Risk | High-risk flag, Airport pickup, long duration/distance, or risky OD corridor. | Add verification/support logic and prioritize experienced drivers. |
| Group D: Critical Watch | High-risk trip during late night or peak Airport corridor with cash/payment concern. | Operational alert, supervisor monitoring, and post-trip review. |

This segmentation should be used at the aggregate level. The goal is not to judge individual customers. The goal is to identify risky patterns by zone, hour, route, and payment behavior. This makes the improvement plan safer and more realistic because it protects service reliability while still capturing demand.

**Table 19. Risk controls connected to the dashboard.**

| Control Area | Dashboard Signal | Required Action |
| --- | --- | --- |
| Zone risk | High-risk share by pickup zone | Escalate Airport and Airport Road for closer monitoring. |
| Time risk | High-risk share by hour | Add controls during late-night and peak-hour windows. |
| OD risk | High-risk share by route | Flag Airport corridors and long-distance routes. |
| Payment risk | Risk by payment method | Review cash-heavy risky segments and promote safer payment behavior. |
| Driver support | Repeated high-risk segments | Assign trained drivers or add in-app support procedures. |

| Decision output of Step 2 A risk-group table that classifies trips into Low, Medium, High, and Critical Watch levels. The dispatch decision should consider risk in addition to demand and revenue. |
| --- |

## Step 3: Fare and Revenue Suitability / Cost-Coverage Review

Issue that is being solved. A high level of revenue does not necessarily guarantee a high level of profitability. In some cases, there is considerable total revenue because many journeys take place along the route; however, a lot of driving time and distance are required to complete the route.

**Table 20. Airport route efficiency evidence.**

| Route | Trips | Revenue | Avg Duration | Avg Distance | Risk | Rev/Min | Fare/Km | ABI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Airport -> Downtown | 3,631 | 15,319.98 | 64.96 | 26.04 | 0.64 | 0.07 | 0.16 | 90.26 |
| Airport -> Business District | 3,250 | 13,759.92 | 65.0 | 26.07 | 0.63 | 0.07 | 0.16 | 84.7 |
| Airport -> Mall Area | 3,119 | 13,108.27 | 64.92 | 25.98 | 0.64 | 0.07 | 0.16 | 84.09 |
| Airport -> Residential | 3,153 | 13,277.99 | 64.93 | 26.08 | 0.64 | 0.07 | 0.16 | 83.04 |
| Airport -> Airport | 1,829 | 7,707.76 | 65.11 | 26.01 | 0.64 | 0.07 | 0.16 | 72.27 |

The repeated value of around 0.07 JOD per minute and 0.16 JOD per kilometer in the Airport corridors is a warning signal. These corridors may be important to the company, but they also require a pricing or incentive review because long-duration routes can reduce driver’s willingness to accept trips.

**Table 21. Cost-coverage review logic.**

| Question | Indicator | Decision Rule |
| --- | --- | --- |
| Is the route generating enough return per driver time? | Revenue per Minute | If low, review fare, incentive, or dispatch priority. |
| Is the route priced fairly for distance? | Fare per Kilometer | If low, review distance-based fare or airport surcharge logic. |
| Is the route slow compared with its distance? | Duration per Kilometer | If high, consider traffic/route delay and driver compensation. |
| Is the route risky? | High Risk Share | If high, add risk controls or support procedures. |
| Is the route strategically important? | Trips, Revenue, ABI | If high ABI, do not remove service; redesign the operating rule. |

**Table 22. Recommended fare/revenue actions.**

| Condition | Action | Expected Business Effect |
| --- | --- | --- |
| High trips + low revenue/minute | Add targeted driver incentive during peak windows. | Improves acceptance without changing all prices. |
| Long Airport corridors + low fare/km | Review airport surcharge or distance/time fare weight. | Protects driver profitability on long routes. |
| High-risk route + long duration | Add monitoring and driver support logic. | Reduces exposure while keeping route coverage. |
| Low demand + low efficiency | Avoid unnecessary driver allocation. | Prevents supply waste in weak segments. |
| High revenue + high ABI | Treat route as strategic and monitor daily. | Maintains service quality in important corridors. |

| Decision output of Step 3 A route review list showing which OD corridors need fare adjustment, targeted driver incentive, or risk-control procedures. The objective is not only more trips, but trips that are financially and operationally sustainable. |
| --- |

## Step 4: Monitoring Governorates Through Streamlit

Issue being solved. This should not be based only on the images from Power BI and exporting tables. There should be an interactive part that monitors the process of improving things. In this case, Streamlit is chosen to be the operating executive page since it can present all the data such as Jordan Heatmap, Key Performance Indicators, performance per city, airport status, driver allocation, and recommendations.

**Figure 13. Monitoring Governorates Through Streamlit.**

| Decision output of Step 4 A Streamlit governorate control page that allows management to monitor Jordan-wide demand while keeping the Amman Airport pilot visible as the main operational intervention. |
| --- |

## Sol Step 5: Adoption of Peak-Hour Plans as an Experimental Pilot

Problem addressed. The peak-hour solution should not be implemented across the whole company immediately. The safer approach is to test it as an experimental pilot in the Airport segment, measure before-and-after KPIs, and then scale only if the pilot improves performance.

**Figure 14. Airport Peak Pressure Segments.**

| Decision output of Step 5 A controlled Airport peak-hour pilot that tests driver pre-positioning and monitors whether bottleneck pressure decreases without damaging revenue, risk, or service coverage. |
| --- |

## Integrated Solution Model

The five solution steps should be connected rather than treated as separate recommendations. Driver distribution handles supply, risk grouping protects safety and reliability, fare/revenue review protects profitability, Streamlit monitoring keeps the whole Jordan network visible, and the peak-hour pilot proves whether the proposed actions work in practice.

**Table 23. Integrated solution model.**

| Layer | Main Input | Main Output | Responsible Tool |
| --- | --- | --- | --- |
| Data Layer | Clean trips, city, zone, hour, fare, distance, duration, risk. | Reliable analytical baseline. | Python / Power Query |
| Scoring Layer | ABI, revenue/minute, fare/km, high-risk share, demand score. | Ranked zones, hours, and routes. | Python Optimization Engine |
| Decision Layer | Driver share, risk group, route review flag. | Operational action list. | Python + Streamlit |
| Monitoring Layer | Governorate heatmap, KPIs, Airport snapshot. | Daily visibility and control. | Streamlit Dashboard |
| Evaluation Layer | Before/after KPIs and pilot comparison. | Decision to scale, adjust, or stop. | Power BI + Streamlit |

**Table 24. Final implementation roadmap.**

| Phase | Action | Output |
| --- | --- | --- |
| Phase 1: Validate | Confirm data quality, airport-to-Amman rule, and KPI definitions. | Clean baseline and trusted indicators. |
| Phase 2: Build Solution Tables | Create allocation, risk groups, and OD efficiency review tables. | Action-ready recommendation files. |
| Phase 3: Airport Pilot | Apply pre-positioning and monitor Airport corridors. | Reduced pressure and improved trip capture. |
| Phase 4: Streamlit Control | Use heatmap and KPI dashboard for governorate monitoring. | Daily BI monitoring layer. |
| Phase 5: Fare/Risk Review | Adjust incentives or fare logic for weak high-risk corridors. | Better profitability and risk control. |
| Phase 6: Scale | Transfer successful rules to Downtown, Business District, Irbid, Zarqa, and Aqaba. | Measurable expansion plan. |

The recommended solution is to begin with an Amman Airport operational pilot. The pilot should distribute enough drivers before the strongest peak windows, classify customer/trip segments by risk, review whether fare and revenue are suitable for long and slow Airport corridors, monitor governorates through the Streamlit heatmap and KPI page, and evaluate the results through before-and-after KPIs. This structure turns the project from a descriptive BI dashboard into a practical decision-support system for route efficiency, driver allocation, and risk-aware operations.
