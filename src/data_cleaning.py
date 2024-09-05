import pandas as pd # type: ignore
import numpy as np
from scipy.stats import zscore # type: ignore

def remove_outliers(df, column, z_threshold=3):
    z_scores = zscore(df[column].dropna())
    df = df[(np.abs(z_scores) < z_threshold)]
    return df

def preprocess_data(df):
    df.fillna(df.mean(), inplace=True)
    
    for column in df.select_dtypes(include=[np.number]).columns:
        df = remove_outliers(df, column)
    
    return df