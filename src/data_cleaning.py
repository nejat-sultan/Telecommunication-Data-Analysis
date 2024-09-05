import pandas as pd
import numpy as np
from scipy.stats import zscore

def remove_outliers(df, column, z_threshold=3):
    z_scores = zscore(df[column].dropna())
    df = df[(np.abs(z_scores) < z_threshold)]
    return df

def preprocess_data(df):
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    
    for column in numeric_cols:
        df = remove_outliers(df, column)
    
    return df
