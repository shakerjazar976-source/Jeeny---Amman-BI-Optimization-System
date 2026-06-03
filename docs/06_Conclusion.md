# Chapter 06: Conclusion

## Project Summary

This project developed a Business Intelligence framework that analyzes the performance of Jeeny trips and derives useful managerial insights by transforming trip level data to business decisions. The project went beyond mere descriptive visuals to develop an integrated solution that uses Power BI, Python, and Streamlit to provide decision-making support for operational improvements.

The primary objective of this research was to identify regions in terms of high trip demand, the most appropriate city, pickup zone creating bottlenecks, critical times in terms of operations, OD pair efficiency or inefficiency, and trip segments requiring risk management measures. This would help in developing relevant solutions to make the company better, particularly in driver allocation, airport pre-positioning, route analysis, and risk-aware operations.

The data had 79,626 trips, including city, pickup_zone, dropoff_zone, trip_time, fare, trip_duration_min, distance_km, payment_mode, risk_flag, and validity status. With this rich data set, we were able to analyze the business from various dimensions, namely geographic, time-based, finance-based, operation-oriented, customer/payment-related, and risk-oriented.

## Main Findings

The first major insight that we can take from the data is that Amman is the primary operational city in terms of the total number of trips as well as revenue generation in comparison with other cities like Irbid, Zarqa, Aqaba, Karak, Madaba, Jerash, and Mafraq. Thus, the project makes the choice of improving the performance of Amman a justified one as opposed to allocating resources evenly throughout the regions.

The second important insight that can be gained from the data is related to the operational bottlenecks in Amman. As seen from the statistics, the Airport zone in Amman has the highest trip volumes and revenues. Moreover, there are long trips and distances associated with Airport as well as the highest risks for drivers. Therefore, Airport cannot be treated like any other standard pickup zone. Airport operations must have a specialized approach including its own playbook, driver staging, rules for monitoring and analyzing route efficiency.

The third insight is the dependence of Jeeny demand on time. The analysis of demands in hourly increments showed that certain periods of the day, particularly the evenings, were characterized by an increase in demand pressure. The analysis suggests that the static strategy used to distribute drivers will need to change as it leads to increased waiting times and, thus, inefficiency.

The fourth important observation is that the analysis of OD-pairs can provide much better information about the traffic structure than the analysis of pickup zones alone. While the latter is focused on determining where trips started, OD analysis provides much deeper insight into the connections between different zones. From our data, it follows that Airport OD-pairs form an important part of Amman route infrastructure. Nevertheless, some of these OD-pairs can prove inefficient based on revenue/minute, fare/km and duration/km.

The fifth major insight is that we need to include risk management into the scope of operations. A demand-only focus will maximize the number of trips but also expose drivers to the increased risks associated with them. Thus, the BI system contains risk factors that are calculated by pickup zone, dropoff zone, time, payment type, and OD-pair.

## Contribution of the BI Solution

The key contributions of the project include transitioning from basic dashboarding to decision support analytics. The development of executive dashboards, visuals on city dominance, zone analysis, OD analysis, risk intelligence, and filtering functionality was done using Power BI. Data quality tables, BI analysis tables, 30 charts, Excel and HTML reporting, bottleneck scores, demand pressure tables, driver allocation recommendation, what if scenarios were developed using Python. Streamlit was introduced as a one-page executive monitoring dashboard.

The key analytical contribution comes from Amman Bottleneck Index (ABI). The index combines multiple pressures into a single metric, namely: trip pressure, revenue pressure, duration pressure, distance pressure, risk pressure, and peak pressure. As such, the managers have a better means of ranking zones, zone-hours combinations, and OD pairs based on their operational pressure. The use of ABI replaces decision-making based on the number of trips alone.

Driver allocation recommendation logic represents another significant analytical contribution. Based on the demand and bottleneck pressures, recommendations on driver allocation are provided by zone and hour of operation. It is the transition from basic BI reporting system to operational decision support system.

## Recommended Improvement Plan

Based on the results, the recommended improvement plan should start with an Amman Airport pilot. The pilot should include five main steps.

First, Jeeny should distribute a sufficient number of drivers based on zone-hour demand pressure. Airport should receive the highest driver share during the strongest peak hours, while other zones such as Downtown, Business District, Mall Area, and Residential should receive allocations based on their demand and bottleneck scores.

Second, customers and trips should be segmented based on risk. High-risk segments should be monitored by pickup zone, dropoff zone, hour, payment method, and OD pair. This ensures that operational improvement does not increase risk exposure.

Third, fare and revenue should be evaluated against operational cost. Routes with low revenue per minute, low fare per kilometer, long duration, or long distance should be reviewed. These routes may need fare adjustment, incentive redesign, dispatch-priority changes, or operational intervention.

Fourth, governorates should be monitored through the Streamlit dashboard. Streamlit gives management a fast way to view the Jordan map, compare governorates, inspect Amman share, track airport performance, monitor risk, and download KPI outputs.

Fifth, peak-hour plans should be adopted as a pilot. Driver pre-positioning should be tested before peak demand periods. The results should be measured using before-and-after indicators such as trips, revenue, waiting-time proxy, high-risk share, revenue per minute, and driver allocation effectiveness.

## Limitations

The project has some limitations. The dataset does not include all operational variables that would be needed for a perfect optimization model. For example, it does not include actual driver locations, driver online minutes, acceptance rate, cancellation rate, customer waiting time, traffic conditions, weather conditions, flight arrival schedules, or real operating costs. Therefore, the driver allocation model should be interpreted as a decision-support recommendation rather than an exact operational command.

Another limitation is that the risk flag is used at an aggregate level. The project does not make individual-level judgments about customers or drivers. Risk is treated as an operational indicator that helps management identify segments requiring monitoring, not as a tool for unfair classification.

## Final Conclusion

The Jeeny BI project demonstrates that ride-hailing operations require more than basic reporting. The analysis shows that operational pressure is spatial, temporal, financial, and risk-related. Amman is the main city to prioritize, Airport is the strongest bottleneck, peak hours require proactive driver planning, OD pairs reveal route-level efficiency gaps, and risk intelligence must be part of any improvement plan.

The final recommendation is to use the BI system as a continuous decision-support tool. Jeeny should prioritize Amman, build an Airport operational playbook, use ABI to rank bottlenecks, apply hourly driver allocation, review weak OD routes, and integrate risk controls into dispatch decisions. By combining Power BI, Python, and Streamlit, the project provides a practical and scalable framework for improving ride-hailing performance in Jordan.
