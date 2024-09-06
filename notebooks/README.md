This folder contains Jupyter notebooks used to perform a detailed analysis of telecom user behavior based on xDR (data session) records. Below is an overview of the tasks and methods applied.

# Handset Usage Analysis:
    * Top 10 Handsets: Identified the most popular handsets used by customers.
    * Top 3 Handset Manufacturers: Analyzed and selected the top 3 manufacturers based on user preferences.
    * Top 5 Handsets per Manufacturer: Listed the top 5 handsets for each of the top 3 manufacturers.

# Task 1.1 - User Behavior Overview
Aggregated Data:
    * Number of xDR sessions, session duration, total download (DL), and upload (UL) data per user.

# Task 1.2 - Exploratory Data Analysis (EDA)
Variable Overview: Described all relevant variables and data types.
Missing Values & Outliers: Identified and replaced missing values and outliers with the mean.
User Segmentation: Divided users into the top five decile classes based on session duration and computed total data per decile.

Basic Metrics:
   * Mean, Median, Variance, Standard Deviation: Computed key statistics to describe user behavior and understand data variability.
Univariate Analysis:
    * Non-Graphical: Analyzed dispersion measures like range, variance, and standard deviation for session duration, download, and upload data.
    * Graphical: Visualized data using histograms to identify distribution patterns and outliers.
Bivariate Analysis:
    * Application Usage vs Data Consumption: Examined the relationship between application usage (e.g., Social Media, YouTube) and total data (DL + UL).
Correlation Analysis:
    * Correlation Matrix: Analyzed relationships between different applications' data (Social Media, Google, YouTube, etc.) to identify key interactions.
Dimensionality Reduction:
    * PCA: Reduced data dimensions to highlight key variables and trends, improving analysis efficiency and interpretability.
