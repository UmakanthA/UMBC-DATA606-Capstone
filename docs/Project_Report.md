## Title and Author

- Unveiling Health Patterns through Socio-Demographic Analysis using Databricks and Streamlit
- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang
- Umakanth Ayalasomayajula
- Github: https://github.com/UmakanthA
- LinkedIn: https:www.linkedin.com/in/umakanth1997
- Presentation:
- Youtube:

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


## EDA

![image](https://github.com/UmakanthA/UMBC-DATA606-Capstone/assets/113398977/166affd1-9b65-4f18-981a-759fa90575e6)

![image](https://github.com/UmakanthA/UMBC-DATA606-Capstone/assets/113398977/b0af9f57-8828-4d60-9047-a094e1637048)

![image](https://github.com/UmakanthA/UMBC-DATA606-Capstone/assets/113398977/0d3b77be-9818-4b19-acc6-0327f014dc6a)

![image](https://github.com/UmakanthA/UMBC-DATA606-Capstone/assets/113398977/463666bd-aac4-49cb-99c1-7bcd366694a9)

![image](https://github.com/UmakanthA/UMBC-DATA606-Capstone/assets/113398977/891ec5b7-df72-495a-b1ee-c116d9f89150)


