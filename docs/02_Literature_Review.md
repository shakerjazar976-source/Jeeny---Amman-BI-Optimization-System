# Chapter 02: Literature Review

## Business Intelligence dashboards and decision-making

Business Intelligence has been widely defined as the process of transformation of data into information. In other words, BI is not merely about having data stored in an organization but about the capacity of that data to be integrated, cleaned, modeled, visualized, and interpreted with regard to certain business problems. According to Goncalves et al. (2023), BI tools assist executives, managers, and employees in making informed decisions. Based on this study, BI should underpin the development of Jeeny project.

One of the most typical examples of BI is a dashboard. Matheus et al. (2020) write that a dashboard is used to aggregate data for a certain goal and help users to see what is going on. Consistent with this idea, the Jeeny dashboard aggregates trips by city, zone, hours, risk, and revenue. It should be noted that researchers also warn about misleading data provided by dashboards in case of low quality of the data itself and lack of explanations about graphics' interpretation. That is why Jeeny project contains a separate page concerning data quality as well as an explanation regarding airport-city correction and efficiency measures of routes and bottlenecks scoring.

The dashboard will be designed based on questions from the business, not the charts themselves. For example, a chart showing trips by city would address the question of "Which governorate should we focus on?" A pickup-zone chart could answer "Which zone puts demand pressure on us?" An OD matrix could answer "Which routes play a dominant role in our network?" And a risk chart would answer "Where do we need to implement controls?" This is how the dashboard would ensure the relevance of visuals created using Power BI.

A great dashboard would classify data into strategic, tactical, and operational KPIs. The strategic KPIs would be Amman share, revenue share, and total valid trips. The tactical KPIs would be zone-hour demand pressure, airport demands, and route profitability. And the operational KPIs would include recommended drivers by hour, high risk trip patterns, and inefficient OD pairs.

## KPI design and performance monitoring

KPIs are what BI dashboards speak. Operational data is turned into indicators that could be measured, compared, and responded to. Picozzi et al. (2024) explain how BI tools can be employed to identify KPIs and develop a Power BI dashboard for the ongoing operational monitoring of business. Though applied to the field of maintenance management, their findings apply to operational processes in general since any such process needs specific indicators that would reveal its efficiency and potential for improvement.

The number of rides made on its own cannot provide a full picture for the purposes of Jeeny. Many rides in one zone could mean high profit. At the same time, they might result in increased waiting times, risks, and inefficient drivers. Low numbers of rides, however, do not necessarily mean that there is no point in paying attention to this zone since, among others, it could serve a connection with the airport, tourist site, university, or the road on the border. For this reason, a variety of KPIs will be used for ride-hailing analysis.

In addition, the KPIs need to be categorized into descriptive and decision KPIs. Descriptive KPIs provide answers about what happened, including the number of trips and revenue. Decision KPIs give answers about what needs to be done, which include ABI score, recommended drivers, route-efficiency level, and high-risk route. The latter category is more useful in the BI project as it enables the transition from analytics to decisions. For instance, in case of a route with numerous trips but a low revenue per minute, pricing needs to be analyzed again.

In literature on dashboards, interpretability is mentioned often. Goncalves et al. (2023) mention analyses that can easily be done and interpreted. Such an approach is essential when it comes to an operational setting in which management does not have time for studying hundreds of trip records. In other words, the Jeeny dashboard needs to rely on color coding, ranking, heat maps, as well as recommendation cards. Moreover, each KPI needs to have a business meaning behind it in order to identify what is good, bad, or questionable.

## Power BI as the descriptive and diagnostic layer

The usage of Power BI is justified by its ability to model data, establish relationships between variables, use measures, slicers, and provide visualizations, which enables descriptive and diagnostic capabilities. According to the project plan, Power BI will be utilized in creating executive dashboards, city comparison pages, Amman deep dive pages, airport analysis pages, risk intelligence pages, and route profitability pages. All of these pages allow exploring the same dataset from different angles without the need to re-code.

Scholarly articles prove the effectiveness of employing Power BI in building integrated dashboards. Goncalves et al. (2023) show that BI can use ETL processes, data warehousing, and dashboards to explore business metrics. Likewise, according to Picozzi et al. (2024), Power BI can assist in dynamic analysis and visualization of KPIs. Therefore, it is justified to choose this tool for report presentation. Dashboards can be refreshed when the dataset changes, making them scalable compared to images.

For the Jeeny project, the most suitable dashboard pages to use include the following: Executive Summary, Jordan Governorate Map, City Dominance, Amman Pickup/Drop off, Airport Operations Control, Hourly Demand and Revenue, OD Matrix, Risk Intelligence, Payment and Customer Segmentation, Route Profitability, and Before and After Pilot Evaluation. In total, these pages are adequate for the usual BI workflow starting from monitoring to operations intelligence.

Still, Power BI should not be viewed as the whole solution for analyzing data. It is very good for visualization and interacting with users but there are tasks that could better be done using Python. These tasks may include composite score calculation, driver simulation, forecasting, route classification, and creation of repeatable analytics in the form of reports.

## Ride-hailing demand prediction and spatiotemporal analytics

Urban ride-hailing demands are greatly influenced by the location and time. According to Jin et al. (2020), challenges in ride-hailing demands forecasting include capturing spatial-temporal dynamics, predicting real-time events, and combining non-linear features. Such problems are evident in Jeeny because rides differ by city, origin area, destination area, hour, day of the week, and risk condition. Hence, any successful forecasting model would consider the dynamics of demand as a spatiotemporal pattern rather than an aggregate number.

Saadi et al. (2017) provide an overview of different machine learning algorithms used in the short-term ride-hailing demand prediction, such as decision trees, bagged trees, random forest, boosting trees, and neural network methods. The article is vital in that it indicates how standard machine learning models can predict demand if data is broken down into spatial and temporal blocks. For Jeeny, such forecasting model can incorporate factors like city, origin area, trip hour, day of the week, weekend indicator, and previous trip counts.

Rahman and Rifaat (2021) expand on this by predicting demand as well as the difference between supply and demand. This point is important since it’s not necessarily an issue when there is very high demand for services if at the same time there is a high number of available drivers. The core issue here is the mismatch between where demand exists and where drivers operate. In the Jeeny project, this approach is captured in the allocation of drivers based on recommended share per trip by hour and zone.

Another aspect pointed out in the literature in relation to forecasting demands is the importance of granularity. According to Liu et al. (2022), "dynamic demand prediction is a key issue" and the authors explore various forms of granularity (spatial and temporal). It turns out that granularity does make a difference. From a Jeeny perspective, the chosen granularity is quite reasonable and easy to understand, namely country level for national comparison, zone level for Amman, hourly level for trip allocation, and OD pair level for trip routing.

## Origin-destination matrices and route-level intelligence

The OD analysis is a vital part of transportation analysis. An example of a BI that only captures pick-up locations would show where trips begin. However, the interaction between zones is not captured. OD matrices provide the structure of movements in a network: from airport to downtown, airport to business district, residential areas to malls, port to tourism zones, among others. For this reason, the project includes an Amman OD matrix and OD performance metrics.

Wang et al. (2024) describe the problem as one of “short-term ride-hailing OD demand prediction,” incorporating information fusion in space-time. The article is more sophisticated than the current BI, but it provides theoretical support for the OD concept. OD analysis can answer questions related to trip generation, revenue, trip duration, inefficiencies, and risks in a dashboard for businesses.

OD-based analytics also provides insight into the profitability of the routes. Two routes with an equal number of trips can generate varying levels of business benefits due to the fact that one route will generate more fare per kilometer, take less time per kilometer, or have less of a high-risk component. That’s why in the Jeeny project we use route efficiency metrics like revenue per minute or fare per kilometer to identify routes for adjustments.

There is another benefit of OD matrix that should not be overlooked – communication. It’s easy to spot high traffic in heatmaps even if a person does not understand anything about data processing. In addition, the image of a heat map speaks to the business manager better than a list of numbers, especially if this person sees the visual aid in the BI presentation.

## Supply-demand mismatch and driver repositioning

Ride-hailing companies need to constantly adjust their demand and supply. Too many drivers in low-demand areas mean higher waiting times for passengers in high-demand areas, lost opportunities for income for the driver, and potential loss of trips for the company. According to Dong et al. (2024), one possible solution to mitigate the imbalance between demand and supply involves strategic guidance, which is crucial for our module.

Repositioning drivers in our project is modeled through a much more manageable approach. Demand shares for each pickup zone for the chosen hour are calculated, adjusted according to the risk factor, and based on this data, drivers' positions in each area are recommended for this hour.

The airport use case illustrates the concept of repositioning logic. When airport demand reaches its peak during evening hours, drivers should be repositioned to airports before the peak occurs, and not after they have accumulated demand. This may be achieved through zone prompts, temporary incentives, waiting-zone logic, and notifications. The dashboard can evaluate metrics like airport wait proxy, total trips, high-risk share, and revenue per minute before and after repositioning.

The idea of repositioning must take into account the notion of risk. Repositioning based on demand only would result in drivers being deployed to high-risk zones without taking other factors into consideration, such as safety considerations and the payment option available, as well as the time needed to travel to the destination. In the Jeeny project, the risk share factor forms part of the ABI score and recommendation logic.

## Airport operations as a special node in ride-hailing networks

Special characteristics of airports as nodes include possible concentration, timing dependency, and connectivity to distant trips. The trips to the airport are affected by flights, night-time travel, luggage, tourist activity, payment by cash, and restricted areas for pick-up. The Jeeny case study regards the airport as a special node in the sense that the dashboard displays it as an important pick-up place in Amman and the airport route patterns are different from those of city routes.

Literature on ride-hailing demand spatiotemporal dynamics suggests such a categorization. As pointed out by Jin et al. (2020), urban space could be functionally segmented into passenger-transportation districts, touristic districts, etc. An airport could be seen as passenger transportation districts having a close connection to other types of zones – commercial, residential, and tourism. Hence, an airport should not be combined with ordinary residential-commercial spaces and deserves a special page.

The airport drilldown needs to contain hourly airport trips, hourly airport income, airport-zone OD flows, high-risk airport percentage, airport fare per kilometer, airport income per minute, and recommendation for driver allocation. This page will bring value to the BI project in that, it will change the broad conclusion that Amman is a key place to a more specific one, i.e., that the airport in Amman is an important operational node.

The BI project may generate a playbook from the dashboard. Some of the recommendations from the playbook may include pre-placing drivers ahead of evening peaks, monitoring high-risk airport trips, reviewing cheap airport routes, and implementing a fixed pickup lane or waiting zones.

## Risk-aware analytics and payment/customer segmentation

Risk segmentation is necessary since improvements in ride-hailing should not be considered solely through increased trips and revenues. If, on one hand, an operation causes an increase in the number of trips, but at the same time, a significant increase in high-risk events occurs, the effect of the operation becomes negative. Risk segmentation factors include general risk, payment type, gender, pick-up zone, drop-off zone, time period, cost, distance, and duration. This set allows assessing whether risk is disproportionately high in certain zones, times, routes, or payment types.

The general discussion on the topic in terms of dashboard research suggests that KPIs should reflect problem areas for the company and should allow for corrective actions. According to Matheus et al. (2020), incorrect interpretations and insufficient understanding of data may lead to errors in dashboards. The benefit of a risk dashboard is that risks become visible rather than hidden behind the number of total trips.

Payment segmentation would be helpful too. Perhaps a trip that involves cash is riskier compared to a wallet trip or a credit card one. The dashboard would help analyze trips based on the type of payment involved, revenue per payment segment, risk per payment segment, and the payment mix per zone. These analyses would help take action, such as implementing verification procedures or providing payment incentives. An airport cash trip at night will require different security measures compared to a wallet-based trip during the day in a business zone.

One must be very careful with customer segmentation. What we aim for here is not an overanalyzes of demographic factors but understanding overall trends that influence service planning. Thus, the project will focus more on operational segments like zone, time of the day, payment type, route, risk factor, and efficiency of the trips.

## Built environment, land use, and zone meaning

Demand for ride-hailing is not random but dependent on the built environment and the use of space. Si & Lin (2025) have conducted research on the factors affecting the demand for ride-hailing in Chengdu, finding out that some urban characteristics and socioeconomic factors could influence the demand level. Specifically, they suggest that population density, floor-area ratio, price of housing, road density, and proximity to the city center might correlate with the ride-hailing demand differently. The authors support the assumptions used in the current project that zones have a certain business character.

In the Jeeny project, the names of zones, including Downtown, Residential, Business District, Mall Area, Airport, Tourist Area, Port Area, University Area, and Industrial Zone, reflect different sources of demand generation. In particular, a business district may be a source of employment-related demand generation, while a mall area is a possible source of shopping leisure demand generation, etc.

Moreover, the built-environment angle could make Jordan map dashboard even stronger since there is a chance to demonstrate how those categories differ in terms of operational significance. For example, Amman could refer to the urban demand, while Aqaba refers to tourism and transportation via ports, Irbid refers to urban universities, Zarqa refers to industrial demand, and finally Madaba / Jerash refers to tourism-based movements. This would lead to a much more realistic BI story than a mere equal set of numbers in the dataset.

Finally, for the literature review, this would mean that the focus of the current research will go beyond the software part. The point is that this project will be devoted to the relation between data visualization and urban behavior in terms of mobility demands.

## Data quality and ethical interpretation

It should be noted that data quality is essential for BI. It is possible to create a misleading dashboard based on poor-quality data. According to Matheus et al. (2020), inadequate data quality and wrong interpretation are listed as risks and difficulties in using dashboards. Considering this statement, the importance of using a cleaned dataset becomes even clearer, as students may change, clean, or simulate data sets to reflect realistic behavior. Therefore, all cleaning rules need to be specified.

Some of the cleaning rules that are used in the Jeeny project include assigning zones that include the Airport to Amman city because according to the project's logic, picking up customers from airports belongs to the Amman operational area. It is also important to filter out good and bad trips, unify names of cities and zones, create new variables such as hourly, monthly, and daily, and derive some fields such as revenue per minute or fare per kilometer.

Ethical considerations should also be taken into account. Risk indicators can be used for operational purposes, but not for making unfounded allegations against individuals. Payment method, gender, or location should be analyzed in aggregate and only in the context of business operations. The current project should not imply the riskiness of a particular demographic group. Instead, it should emphasize the practicality of such risk indicators as night-time, cash, distance, and OD route.

A transparent BI project requires also having a limitations chapter. For instance, the dataset might not contain real figures related to the number of drivers, waiting times, cancellation percentages, traffic, weather conditions, and even schedules of flights. This means that the proposed driver assignment cannot guarantee the absolute optimality but is rather an estimate.

## From literature to the Jeeny BI framework

The existing literature has provided a good structure for the proposed project. BI dashboard literature proves the use of Power BI and KPI pages. KPI literature helps in measuring indicators to define KPIs. Ride-hailing demand forecasting literature proves the use of spatial and temporal characteristics. Demand research literature helps to develop route-level matrices. Driver repositioning literature proves the translation of demand evidence into allocation recommendations. Risk and data quality discussions prove the need for a responsible interpretation.

The Jeeny BI framework includes four layers. Layer 1 involves data preparation through data cleaning, validation, deriving indicators, and airport-city adjustment. Layer 2 involves dashboarding at various levels using Power BI. This involves dashboarding at city level, at zone level, per hour, risk analysis, payment analysis, revenue analysis, and OD matrix analysis. Layer 3 involves advanced analyses such as ABI score calculation, demand forecasting, route efficiency ranking, and scenarios simulation through Python scripting. Layer 4 involves decision actions.

The proposed approach enhances the project by addressing one of the major flaws associated with student dashboards that consists in presenting visuals but not making decisions. Every dashboard page must provide the answer, with city dominance identifying the place of priority, airport analysis providing the answer about where a playbook is needed, hourly analysis determining where pressure occurs, OD analysis identifying movements affecting the network, efficiency analysis pointing out what routes require checking, and risk analysis revealing where controls have to be implemented.

To conclude, the current literature study confirms the basic idea behind the project, namely, that a business intelligence solution for the operations of ride-hailing should include not only visualization but also predictive and prescriptive analytics. The Jeeny project can thus be considered to be theoretically grounded and practically meaningful because it involves using Power BI for data analysis, Python for recommendations, and KPI-driven decision stories for presentation of results.
