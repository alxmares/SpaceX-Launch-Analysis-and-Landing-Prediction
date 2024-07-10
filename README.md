# SpaceX Launch Analysis and Landing Prediction

## Overview

Analyze SpaceX's historical launch data to identify factors influencing rocket landing success using data analysis and machine learning.

![](/assets/spaceximg.png)

## Table of Contents
- [Introduction](#introduction)
- [Methodology](#methodology)
- [Results](#results)
- [Conclusion](#conclusion)
- [Appendix](#appendix)

## Introduction

### Objective
Investigate:
- Factors affecting rocket landing success
- Predict future landing success
- Identify trends and patterns in launch data

## Methodology

### Data Sources
- **SpaceX API**: Historical launch data
- **Web Scraping**: Falcon 9 and Falcon Heavy launch tables

### Key Steps
1. **Data Collection**: API queries and web scraping for launch details
2. **Data Wrangling**: Cleaning and transforming data
3. **Exploratory Data Analysis (EDA)**: Visualizations and SQL analysis
4. **Predictive Modeling**: Building and evaluating classification models

## Results

### Highlights
- **Interactive Dashboards**: Dynamic data visualization
- **Predictive Models**: Achieved 83% accuracy with Logistic Regression, SVM, and KNN
- **Key Insights**:
  - High success rates at CCAFS SLC 40
  - Payload mass and launch site influence success

### Visualizations
- **Maps**: Launch and landing sites visualization
- **Charts**: Success rates and payload outcomes analysis

## Conclusion

Significant improvement in landing success rates over the years, showcasing SpaceX's technological advancements. Interactive visualizations and predictive models provide actionable insights.

## Appendix

### Notebooks
- [Data Collection - API](https://github.com/alxmares/-SpaceX-Launch-Analysis-and-Landing-Prediction/blob/main/01-Collecting_data.ipynb)
- [Data Collection - Web Scraping](https://github.com/alxmares/-SpaceX-Launch-Analysis-and-Landing-Prediction/blob/main/02-WebScraping.ipynb)
- [Data Wrangling](https://github.com/alxmares/-SpaceX-Launch-Analysis-and-Landing-Prediction/blob/main/03-DataWrangling.ipynb)
- [EDA with SQL](https://github.com/alxmares/-SpaceX-Launch-Analysis-and-Landing-Prediction/blob/main/04-EDA_SQL.ipynb)
- [Data Visualization](https://github.com/alxmares/-SpaceX-Launch-Analysis-and-Landing-Prediction/blob/main/05-EDA2.ipynb)
- [Interactive Maps](https://github.com/alxmares/-SpaceX-Launch-Analysis-and-Landing-Prediction/blob/main/06-Maps.ipynb)
- [Plotly Dash Dashboard](https://github.com/alxmares/-SpaceX-Launch-Analysis-and-Landing-Prediction/blob/main/07-Dashboard.py)
- [Predictive Modeling](https://github.com/alxmares/-SpaceX-Launch-Analysis-and-Landing-Prediction/blob/main/08-ML_to_predict_land.ipynb)

### Data URLs
- [SpaceX Rockets API](https://api.spacexdata.com/v4/rockets/)
- [SpaceX Launchpads API](https://api.spacexdata.com/v4/launchpads/)
- [SpaceX Payloads API](https://api.spacexdata.com/v4/payloads/)
- [SpaceX Cores API](https://api.spacexdata.com/v4/cores/)

