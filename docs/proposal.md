## Title and Author

- Unveiling Health Patterns through Socio-Demographic Analysis using Databricks and Streamlit
- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang
- Umakanth Ayalasomayajula
- Github: https://github.com/UmakanthA
- LinkedIn: https:www.linkedin.com/in/umakanth1997
- Presentation:
- Youtube:

# Unveiling Health Patterns through Socio-Demographic Analysis using Databricks and Streamlit

## Introduction
This project aims to analyze and visualize socio-demographic factors and health metrics related to nutrition, physical activity, and obesity using data obtained from the Behavioral Risk Factor Surveillance System (BRFSS) by the Centers for Disease Control and Prevention (CDC).The ultimate goal is to develop interactive dashboards using Streamlit to empower users to explore and understand health disparities and trends, filtering by location, ethnicity, and socio-economic status.

## Background
The Nutrition, Physical Activity, and Obesity dataset provides crucial insights into adults' dietary habits, physical activity levels, and weight status. This dataset offers comprehensive national and state-specific information on obesity prevalence, nutrition patterns and physical activity trends. It serves as a valuable resource for understanding and addressing public health challenges related to nutrition, physical activity, and obesity across the United States.

## Dataset
The dataset it sourced from Data.gov, consisting of approximately 94000 rows and 33 columns. Each row of the dataset includes information on adults' diet, physical activity and weight status of multiple demographies of each and every state of the USA. 

Dataset link - https://catalog.data.gov/dataset/nutrition-physical-activity-and-obesity-behavioral-risk-factor-surveillance-system.

## Dataset Overview
**Data Source and Scope**:
The dataset originates from the Behavioral Risk Factor Surveillance System (BRFSS) by the Centers for Disease Control and Prevention (CDC).It encompasses information on adult nutrition, physical activity and weight status.

**Temporal Coverage**:
The dataset spans from the years 2011 to 2022, providing longitudinal insights into health-related behaviors and outcomes over time.It includes data updates as recent as December 7, 2023, ensuring relevance and currency in health analysis.

**Variable Composition**:
The dataset comprises 33 columns, encompassing a variety of socio-demographic indicators and health metrics.Key variables include YearStart, LocationAbbr, Class, Topic, Question, Data_Value, Sample_Size, Income, Race/Ethnicity, and GeoLocation, among others.

**Missing Data and Quality**:
There are several columns with a substantial amount of missing data, such as Data_Value_Unit, Data_Value_Footnote, Total, Age(years), Education, Gender, Income, and Race/Ethnicity.Data cleaning is necessary to address missing data and ensure the reliability of analysis outcome.

## Tools and Technologies
**PostgreSQL**: advanced open source database for data storage, efficient querying, manipulating and managing the data.

**Databricks**: open analytics platform for building and deploying machine learning tasks. to perform initial data analysis, for cleaning and preprosessing the dataset and for creating and running machine learning models.

**Snowflake**: cloud based analytics service.

**Streamlit**: open-source Python framework for creating interactive data apps in minutes.

## Proposed workflow
1. **Data Collection**: download the CDC Nutrition, Physical Activity, and Obesity - Behavioral Risk Factor Surveillance System dataset and store it in PostgreSQL.
2. **Exploratory Data Analysis and model development**: we use databricks to perform initial data analysis, for cleaning and preprosessing the dataset and also for creating and running machine learning models. We try to predict obesity rates, classify health behaviour etc.
3. **Data Visualization**: using Snowflake for data visualization, we visualize the data based on the most relevant parameters.
4. **Web application**: with the help of Streamlit, we create and represent interactive dashboards like obesity prevalence dashboard, health disparity dashboard by region etc.These dashboards can provide valuable insights into the relationships between socio-demographic factors and health outcomes, helping users understand health disparities and trends and informing public health interventions and policy-making efforts.

## Conclusion
The project aims to contribute to the collective efforts in driving positive change in the realm of public health. With the interactive dashboards generated through our workflow, we aspire to facilitate data-driven dialogue and inspire impactful interventions to address the pressing health challenges faced by communities across the nation.

## Future Scope
Describe the current status of overweight/obesity, physical activity and nutrition in the Obesity, Physical Activity and Nutrition in each of the annual state health reports.
Evaluate the health of the state population by monitoring chronic diseases, infectious diseases, nutrition, physical activity, obesity.
Provide relevant data to the respective state healthcare departments.



