import pytest # type: ignore
import pandas as pd # type: ignore
from scripts.telecom_analysis import (top_10_handsets, top_3_manufacturers, top_5_handsets_per_manufacturer, 
                               aggregate_user_data, handle_missing_values, 
                               perform_eda, perform_pca, compute_engagement_metrics, 
                               run_kmeans_clustering)

# Sample data for testing
@pytest.fixture
def sample_data():
    data = {
        'MSISDN': ['123', '456', '789', '123', '456'],
        'Handset': ['A', 'B', 'C', 'A', 'B'],
        'Manufacturer': ['X', 'Y', 'X', 'X', 'Y'],
        'Social Media': [100, 200, 300, 400, 500],
        'Google': [50, 60, 70, 80, 90],
        'Email': [30, 20, 10, 20, 30],
        'YouTube': [200, 300, 400, 500, 600],
        'Netflix': [150, 250, 350, 450, 550],
        'Gaming': [80, 90, 100, 110, 120],
        'Other': [20, 30, 40, 50, 60],
        'Session Duration': [10, 15, 20, 25, 30],
        'Download (DL)': [500, 600, 700, 800, 900],
        'Upload (UL)': [100, 200, 300, 400, 500]
    }
    return pd.DataFrame(data)

def test_top_10_handsets(sample_data):
    result = top_10_handsets(sample_data)
    assert len(result) == 10

def test_top_3_manufacturers(sample_data):
    result = top_3_manufacturers(sample_data)
    assert len(result) == 3

def test_top_5_handsets_per_manufacturer(sample_data):
    result = top_5_handsets_per_manufacturer(sample_data)
    assert len(result) == 5

def test_aggregate_user_data(sample_data):
    result = aggregate_user_data(sample_data)
    assert 'number_of_sessions' in result.columns
    assert 'total_data_volume' in result.columns

def test_handle_missing_values(sample_data):
    result = handle_missing_values(sample_data)
    assert result.notnull().all().all()

def test_perform_eda(sample_data):
    result = perform_eda(sample_data)
    assert 'mean_session_duration' in result
    assert 'median_download' in result

def test_perform_pca(sample_data):
    result = perform_pca(sample_data)
    assert 'explained_variance_ratio_' in result

def test_compute_engagement_metrics(sample_data):
    result = compute_engagement_metrics(sample_data)
    assert 'top_10_customers' in result

def test_run_kmeans_clustering(sample_data):
    result = run_kmeans_clustering(sample_data)
    assert 'cluster_centers_' in result
