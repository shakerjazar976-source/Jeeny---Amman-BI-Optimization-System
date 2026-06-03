# Chapter 04: Results

The Executive Dashboard is the opening page of the BI report. It is intended for decision makers who need a quick summary of the operational picture. The page shows that the dataset contains approximately 80K valid trips, total revenue around 226.11K JOD, average fare around 2.84 JOD, average distance around 14.46 km, and Airport as the top pickup zone.

This page answers the question: what is the overall state of Jeeny trips in the selected period? It combines high-level KPIs with city and pickup-zone charts. In a final research report, this page should be discussed as the descriptive baseline before moving to deeper bottleneck diagnosis.

The most important interpretation from this page is that Airport and Amman are not isolated details. They dominate the operational story and therefore justify the deeper Amman bottleneck methodology.

**Table 12. Executive dashboard KPI interpretation.**

| KPI card | Interpretation |
| --- | --- |
| Valid Trips | Counts total valid operational trips |
| Total Revenue | Shows the financial scale of the dataset |
| Average Fare | Gives a base fare-efficiency indicator |
| Average Distance | Shows average trip length |
| Top Pickup Zone | Identifies the first visible demand concentration |

## City Dominance

Zone Dominance provides an analysis from general city to operational pressure. The page concentrates on the pick-up zones and their correlation with drop-off zones. From the snapshot below, the Airport has been identified as the main pick-up zone, with about 20K trips for the top zone and 100% trip share in the chosen scope.

OD Matrix is key to this page, since OD matrix gives the flow of structure and not just the picks-up. In some zones, there are many picks up, but at the same time they are less profitable, risky or take more time depending on the destination point of the passengers. Thus, the OD Matrix serves as the link between the visualization analysis and route efficiency in Python.

This page reinforces the claim of our research, in which case Jeeny should not consider all zones as one.

**Figure 2. Power BI zone dominance page with pickup-zone ranking and OD matrix.**

The city dominance data indicate Amman as shown in the figures 2 and 3 to be the dominating operational city within the database. For the wide-gap city dominance data, Amman consists of 46,384 trips, which are far higher than Irbid, Zarqa, Aqaba, Karak, Madaba, Jerash, and Mafraq. The difference between cities allows us to understand the project choice to optimize the program starting with Amman.

The city revenue data also allow us to make a similar conclusion. First, Amman produces the highest total revenue, whereas Aqaba demonstrates better fare behavior relative to some low-demand cities. Thus, the project can consider both aspects simultaneously.

Based on the BI results, the project cannot evenly implement the first optimization pilot within the cities considered. Amman should be prioritized because its potential operational and financial impact is significantly higher.

**Figure 3. Valid trips by city from the wide-gaps dataset.**

Decomposition tree logic is applied in the design of the page called City Deep Dive to decompose the total trips based on city, pickup zone, and drop-off zone.

Value of such a page lies in its ability to enable interactive diagnosis. That means the analysis will start with total valid trips, then move on to choose a city, and further see the zones of pick-up and drop-off that define that city. From a BI perspective, the page demonstrates that it is possible to shift from monitoring to root cause analysis.

In the context of the Jeeny case, it indicates the scalability of the research approach since the focus is on Amman, yet the same dashboard can be used for analyzing data in other cities like Irbid, Zarqa, Aqaba, Karak, Madaba, Jerash, and Mafraq.

**Figure 4. Power BI city deep-dive view using a decomposition-style analysis path.**

## Amman Pickup Zone Dominance

Airport is the number one pickup spot within Amman. Based on the final data set, Airport has approximately 19,607 pickups compared to Downtown, Business District, Mall Area and Residential which has way fewer pickups. It is therefore easy to see that Airport becomes a bottleneck in this scenario.

The Airport findings justify an Airport playbook. Such a playbook would include staging of drivers, airport wait zone rules, peak hour notifications, and airport-zone OD pair tracking. The Airport should be viewed as a unique business node rather than just a regular pick-up location.

Conclusively, both the pickup zone dashboard and the Python tables reveal that Amman is the primary city while Airport is the major bottleneck in this case.

**Figure 5. Amman trips by pickup zone from the wide-gaps dataset.**

## Hourly Demand Pressure

However, the hourly demand graph indicates peaks, particularly in the mornings and evenings. The data set for analysis was purposely designed in such a way as to prevent any form of flat demand. The largest peaks were observed at 8:00, 17:00, 18:00, 20:00, and 21:00, with 21:00 showing peak demand.

**Figure 6. Amman demand by hour showing strong peak gaps.**

## OD Flow

The chart below shows that the highest number of trips is from Airport to Downtown, indicating that the airport is a major demand point in Amman’s Jeeny network.

Most of the top OD pairs are connected to the airport, downtown, and business district, which suggests the need for better driver allocation in these areas to reduce bottlenecks and improve service efficiency.

**Figure 7. Top Origin-Destination Trip Pairs in Amman.**

The chart shows that Airport → Downtown generates the highest revenue, making it the most valuable route in the network.

**Figure 8. Top Origin-Destination Pairs by Revenue in Amman.**

The OD analysis shows how pickup zones connect to dropoff zones. This is more valuable than only counting pickups because it reveals the actual movement network. Airport to Downtown, Airport to Business District, Airport to Mall Area, and Airport to Residential appear as important operational corridors.

Route efficiency is measured using revenue per minute, fare per kilometer, duration per kilometer, average duration, and risk share. The final dataset creates strong efficiency gaps. For example, Airport routes have low revenue per minute because they are long, slow, and underpriced relative to the time they consume. Business District to Downtown and Business District to Mall Area show much higher revenue per minute.

This result supports a route-level recommendation: weak Airport OD routes should be reviewed for fare, driver incentive, dispatch priority, or airport staging policy.

**Figure 9. Revenue per minute by OD pair showing clear efficiency gaps.**

Fare per kilometer provides another view of pricing efficiency. In the final dataset, Business District routes have much higher fare per kilometer than several Airport routes. This gap is useful because it shows that two routes can have different financial quality even if both generate trips.

The gap between high fare-per-km routes and low fare-per-km routes supports a pricing review. Routes with long duration, long distance, and weak fare per kilometer may create low driver profitability and poor supply motivation. In a ride-hailing context, drivers may avoid routes that consume too much time for too little return.

The report should therefore discuss pricing gaps as an operational problem, not only a revenue issue.

**Figure 10. Fare per kilometer by OD pair showing clear pricing gaps.**

## Risk Intelligence

Risk intelligence is one of the most valuable assets added to the BI project. In the final data set, we can see that Airport has an exceptionally high high-risk ratio compared to other Amman pick-up points. This high-risk ratio reaches around 83.5%, based on the wide gaps working data set. Therefore, Airport is not only a bottleneck from a demand perspective, but also from a risk perspective.

It should be recommended within the scope of the project that any optimization efforts at Airport should take into account risk management measures. Adding more drivers without controlling risks would be adding unnecessary operational exposure. Potential risk management measures include monitoring payments, dispatch policy, driver assistance, and reviews of late-night flights from Airport.

The Risk Intelligence dashboard should be used to advocate for risk-aware decision making in BI.

**Figure 11. High-risk share by Amman pickup zone showing wide risk gaps.**
