## Title and Author

- Unveiling Health Patterns through Socio-Demographic Analysis using Tableau and Streamlit
- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang
- Umakanth Ayalasomayajula
- Github: [Umakanth_A_Project](https://github.com/UmakanthA/UMBC-DATA606-Capstone/tree/main)
- LinkedIn: [Linkedin](https://www.linkedin.com/in/umakanth1997)
- Presentation: [Presentation](https://docs.google.com/presentation/d/1KqISIock8gKCqZ27LiqEUtQAZYpg8EgK/edit#slide=id.p1)
- Youtube: [Youtube](https://youtu.be/kFmML8x4nEc?si=Si5YXF3TyoB9zMQ7)

## Background

This project aims to analyze and visualize socio-demographic factors and health metrics related to nutrition, physical activity, and obesity using data obtained from the Behavioral Risk Factor Surveillance System (BRFSS) by the Centers for Disease Control and Prevention (CDC).The ultimate goal is to develop interactive dashboards using Streamlit to empower users to explore and understand health disparities and trends, filtering by location, ethnicity, and socio-economic status.

The Nutrition, Physical Activity, and Obesity dataset provides crucial insights into adults' dietary habits, physical activity levels, and weight status. This dataset offers comprehensive national and state-specific information on obesity prevalence, nutrition patterns and physical activity trends. It serves as a valuable resource for understanding and addressing public health challenges related to nutrition, physical activity, and obesity across the United States.

## Data
- Data sources: Data.gov![https://catalog.data.gov/dataset/nutrition-physical-activity-and-obesity-behavioral-risk-factor-surveillance-system.]
- Data size: 33MB
- Data shape: Columns - 33, Rows - 94000
- Time period: 2011 to 2023
- Data dictionary:

| Column Name             | Description                                   |
|-------------------------|-----------------------------------------------|
| YearStart               | Year start                                    |
| YearEnd                 | Year End (for single-year indicator, year end=year start) |
| LocationAbbr            | Location abbreviation                         |
| LocationDesc            | Location description                          |
| Datasource              | Name or abbreviation of Data Source           |
| Class                   | Class Description                             |
| Topic                   | Topic Description                             |
| Question                | Question Description                          |
| Data_Value_Unit         | Description of unit e.g. %, etc               |
| Data_Value_Type         | Description of type of data e.g. Value, Percentage, Number |
| Data_Value              | Data value (percentage, text)                 |
| Data_Value_Alt          | Numeric representation of data value          |
| Data_Value_Footnote_Symbol | Symbol that would be used to flag footnotes |
| Data_Value_Footnote     | Footnote text                                 |
| Low_Confidence_Limit   | Low 95% Confidence Interval value             |
| High_Confidence_Limit  | High 95% Confidence Interval value            |
| Sample_Size             | Sample Size                                   |
| Total                   | Total/Overall breakout category               |
| Age(years)              | Age (years) breakout category                 |
| Education               | Education breakout category                   |
| Gender                  | Gender breakout category                      |
| Income                  | Income breakout category                      |
| Race/Ethnicity          | Race/Ethnicity breakout category              |
| GeoLocation             | Latitude & Longitude to be provided for formatting GeoLocation or Geocode in the format (latitude, longitude) |
| ClassID                 | Lookup identifier value for Class             |
| TopicID                 | Lookup identifier value for Topic             |
| QuestionID              | Lookup identifier value for Question          |
| DataValueTypeID         | Lookup identifier value for Data_Value_type   |
| LocationID              | Lookup identifier value for Location          |
| StratificationCategory1 | Lookup Identification value, such as Age Group, Gender |
| Stratification1         | Data stratified by this value, such as Male, Female, Total |
| StratificationCategoryId1 | Lookup identifier value for Stratification1 |
| StratificationID1       | Lookup identifier value for StratificationCategory1 |


## Exploratory Data Analysis

Below image shows the average data value for each of the questions of the survey, from 2011 to 2022


![Average Data value for each question](https://github.com/UmakanthA/UMBC-DATA606-Capstone/assets/113398977/8568c1f7-7d20-41bb-94f1-aafa7e72de30)

Below dashboard shows the health stats by education, income, and race.


![Dashboard1 - Socio Demographic response based on sample size](https://github.com/UmakanthA/UMBC-DATA606-Capstone/assets/113398977/5731c948-e696-4388-8428-52ce0fa1bd8a)

Below dashboard shows the average education, income and the age categories of the average sample size


![Dashboard 3](https://github.com/UmakanthA/UMBC-DATA606-Capstone/assets/113398977/555cccbf-501e-4c9a-838c-64dcf62bf3cc)

Below dashboard shows the stats based on demography


![Dashboard 2 - Statistics by region](https://github.com/UmakanthA/UMBC-DATA606-Capstone/assets/113398977/a06b12d9-d4e1-47fc-b1d9-7cdb154ec8bd)


## Model building

The ARIMA time series model has been selected for the datset. The model can be used to predict the datavalue, which is the target variable, for any question and any location accurately.


![image](https://github.com/UmakanthA/UMBC-DATA606-Capstone/assets/113398977/1d91ac96-dde9-44b3-a34c-df2b32658de9)

## Application of shared model

Developed a web application to deploy the ARIMA model.


![image](https://github.com/UmakanthA/UMBC-DATA606-Capstone/assets/113398977/36e89a21-7d93-447e-a74c-9da422adf266)

## Conclusion

Geographic disparities exist in obesity and overweight rates across states, emphasizing the need for tailored interventions based on regional trends.

Encouraging regular physical activity and healthy eating habits, such as consuming fruits and vegetables, can significantly reduce the risk of obesity and related health complications.

States with higher rates of physical activity demonstrate lower obesity prevalence, highlighting the importance of promoting an active lifestyle at the population level.

Long-term public health strategies should focus on addressing behavioral factors, improving access to healthy foods, and creating environments that support physical activity to combat the obesity epidemic effectively.











