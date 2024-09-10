# Project Overview

This project focuses on analyzing a telecom dataset from TellCo, a mobile service provider in the Republic of Pefkakia. The dataset provides detailed insights into user behavior, session data, and application usage. The goal is to deliver meaningful recommendations to a wealthy investor who is considering purchasing TellCo. The analysis includes exploratory data analysis (EDA), user behavior segmentation, and various statistical and machine learning techniques to extract insights from the data. The findings will be presented in a web-based dashboard built using Streamlit.

## Business Need 

TellCo, a mobile service provider, has shared its user data for analysis. Our investor is interested in evaluating the profitability of purchasing TellCo and identifying growth opportunities. This analysis will provide insights into user behavior and potential areas for revenue growth by analyzing the xDR (Data Sessions Detail Record) to understand user engagement with various applications and services.

## Data

The dataset consists of a month’s worth of xDR records, which include the following:
- Handset information
- Data on user activity across applications like Social Media, Google, Email, YouTube, Netflix, and Gaming
- Metrics such as session duration, total data downloaded (DL), uploaded (UL), and total data volume per session

## Features

This project is structured to deliver insights into various aspects of telecom user data. Below is a breakdown of features by the main objectives:

### User Overview Analysis:
- **Handset Analysis**: Identified the top 10 handsets and top 3 manufacturers used by customers. Provided insights into the top 5 handsets per manufacturer and recommendations for marketing teams.
- **User Data Aggregation**: Collected and analyzed xDR session data, including session count, duration, and total data (DL + UL). Segmented users into deciles based on session duration and calculated total data usage per decile.
- **Application Usage**: Aggregated data usage across specific applications (Social Media, YouTube, Netflix, etc.) to understand user engagement and behavior trends.
- **Exploratory Data Analysis**: Performed data cleaning, handled missing values and outliers, and conducted both graphical and non-graphical univariate analysis on variables such as session duration and data usage.
- **Bivariate & Correlation Analysis**: Analyzed relationships between application usage and total data consumption. Calculated a correlation matrix to understand interactions between applications like Social Media, Google, YouTube, and Netflix.
- **Dimensionality Reduction**: Performed Principal Component Analysis (PCA) to reduce data dimensions and interpret key components that influence user satisfaction and behavior.

### User Engagement Analysis:
- Aggregated metrics per customer ID (MSISDN) and report the top 10 customers per engagement metric.
- Normalized each engagement metric and applied k-means clustering (k=3) to classify customers into three engagement groups.
- Computed minimum, maximum, average, and total non-normalized metrics for each cluster. Interpret results visually with accompanying text.
- Aggregated total traffic per application and derive the top 10 most engaged users per application.
- Plotted the top 3 most used applications using appropriate charts.
- Used k-means clustering to group users into k engagement clusters based on the engagement metrics. Determine the optimized value of k using the elbow method and interpret findings.

### User Experience
### User Satisfaction

## Requirements

Before running the project, make sure you have the following dependencies installed:
- `pandas`
- `numpy`
- `scikit-learn`
- `streamlit`
- `SQLAlchemy`
- `psycopg2-binary`
- `matplotlib`
- `seaborn`
- `pytest`

These dependencies are listed in the `requirements.txt` file and can be installed easily using:

pip install -r requirements.txt


## Installation

Clone the repository: git clone https://github.com/nejat-sultan/Telecommunication-Data-Analysis cd Telecommunication-Data-Analysis

- Set up a virtual environment and activate it:
- python -m venv venv source venv/bin/activate

Open the Jupyter notebook for analysis:
Once the dependencies are installed, you can start exploring the data through the provided Jupyter notebooks or by running the analysis scripts.

## Testing

To ensure the correctness of the code, you can run the unit tests provided in the tests/ folder. Run the tests with: pytest




