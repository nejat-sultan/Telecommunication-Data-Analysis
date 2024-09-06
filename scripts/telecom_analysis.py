import pandas as pd # type: ignore
from sklearn.decomposition import PCA # type: ignore
from sklearn.cluster import KMeans # type: ignore

def top_10_handsets(df):
    return df['Handset'].value_counts().head(10)

def top_3_manufacturers(df):
    return df['Manufacturer'].value_counts().head(3)

def top_5_handsets_per_manufacturer(df):
    top_manufacturers = top_3_manufacturers(df).index
    return df[df['Manufacturer'].isin(top_manufacturers)]['Handset'].value_counts().head(5)

def aggregate_user_data(df):
    df['total_data_volume'] = df['Download (DL)'] + df['Upload (UL)']
    return df.groupby('MSISDN').agg(
        number_of_sessions=('MSISDN', 'count'),
        session_duration=('Session Duration', 'sum'),
        total_data_volume=('total_data_volume', 'sum')
    ).reset_index()

def handle_missing_values(df):
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    non_numeric_cols = df.select_dtypes(exclude=['float64', 'int64']).columns
    
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    
    for col in non_numeric_cols:
        df[col] = df[col].fillna(df[col].mode()[0])
    
    return df


def perform_eda(df):
    result = {
        'mean_session_duration': df['Session Duration'].mean(),
        'median_download': df['Download (DL)'].median()
    }
    return result

def perform_pca(df):
    pca = PCA(n_components=2)
    numeric_df = df.select_dtypes(include=['float64', 'int64']).fillna(0)  # Handle NaNs
    df_pca = pca.fit_transform(numeric_df)
    return {
        'explained_variance_ratio_': pca.explained_variance_ratio_
    }

def compute_engagement_metrics(df):
    df = df.copy()  # Avoid changing the original DataFrame
    df['total_data_volume'] = df['Download (DL)'] + df['Upload (UL)']
    engagement_metrics = {
        'top_10_customers': df.groupby('MSISDN').agg(
            sessions_frequency=('MSISDN', 'count'),
            session_duration=('Session Duration', 'sum'),
            total_traffic=('total_data_volume', 'sum')
        ).sort_values(by='total_traffic', ascending=False).head(10)
    }
    return engagement_metrics

def run_kmeans_clustering(df, k=3):
    kmeans = KMeans(n_clusters=k)
    df = df.copy()  # Avoid changing the original DataFrame
    df['total_data_volume'] = df['Download (DL)'] + df['Upload (UL)']
    df['cluster'] = kmeans.fit_predict(df[['Session Duration', 'total_data_volume']].fillna(0))  # Handle NaNs
    return {
        'cluster_centers_': kmeans.cluster_centers_
    }