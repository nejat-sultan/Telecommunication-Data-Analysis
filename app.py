import streamlit as st # type: ignore
import pandas as pd # type: ignore
import numpy as np
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore
from sklearn.cluster import KMeans # type: ignore
from sklearn.preprocessing import StandardScaler # type: ignore

@st.cache
def load_data():
    telecom_data = pd.read_csv('data/Week2_challenge_data_source(CSV).csv')
    return telecom_data
    
data = load_data()

st.sidebar.title("Telecom Data Dashboard")
section = st.sidebar.selectbox("Select Analysis", ["Overview", "User Engagement", "User Experience", "Customer Satisfaction"])

if section == "Overview":
    st.title("User Overview Analysis")

    st.subheader("Top 10 Handsets Used")
    top_10_handsets = data['Handset Type'].value_counts().head(10)
    st.write(top_10_handsets)

    st.subheader("Top 3 Handset Manufacturers")
    top_3_manufacturers = data['Handset Manufacturer'].value_counts().head(3)
    st.write(top_3_manufacturers)

    st.subheader("Top 5 Handsets Per Manufacturer")
    for manufacturer in top_3_manufacturers.index:
        st.write(f"Manufacturer: {manufacturer}")
        top_5_handsets = data[data['Handset Manufacturer'] == manufacturer]['Handset Type'].value_counts().head(5)
        st.write(top_5_handsets)

if section == "User Engagement":
    st.title("User Engagement Analysis")

    engagement_metrics = data.groupby('IMSI').agg(
        total_sessions=('Activity Duration DL (ms)', 'sum'),
        total_duration=('Activity Duration UL (ms)', 'sum'),
        total_data=('Total DL (Bytes)', 'sum')
    ).reset_index()

    st.subheader("Top 10 Customers by Engagement Metrics")
    top_10_sessions = engagement_metrics.nlargest(10, 'total_sessions')
    top_10_duration = engagement_metrics.nlargest(10, 'total_duration')
    top_10_data = engagement_metrics.nlargest(10, 'total_data')

    st.write("Top 10 Customers by Sessions")
    st.write(top_10_sessions)

    st.write("Top 10 Customers by Duration")
    st.write(top_10_duration)

    st.write("Top 10 Customers by Data Usage")
    st.write(top_10_data)

    st.subheader("Customer Engagement Clusters")
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(engagement_metrics[['total_sessions', 'total_duration', 'total_data']])

    kmeans = KMeans(n_clusters=3)
    engagement_metrics['Cluster'] = kmeans.fit_predict(scaled_data)

    st.write(engagement_metrics[['IMSI', 'Cluster']])

    st.write("Cluster Stats")
    cluster_stats = engagement_metrics.groupby('Cluster').agg({
        'total_sessions': ['mean', 'max', 'min'],
        'total_duration': ['mean', 'max', 'min'],
        'total_data': ['mean', 'max', 'min']
    })
    st.write(cluster_stats)

if section == "User Experience":
    st.title("User Experience Analysis")

    experience_metrics = data.groupby('IMSI').agg(
        avg_tcp_dl=('TCP DL Retrans. Vol (Bytes)', 'mean'),
        avg_tcp_ul=('TCP UL Retrans. Vol (Bytes)', 'mean'),
        avg_rtt_dl=('Avg RTT DL (ms)', 'mean'),
        avg_rtt_ul=('Avg RTT UL (ms)', 'mean'),
        avg_bearer_tp_dl=('Avg Bearer TP DL (kbps)', 'mean'),
        avg_bearer_tp_ul=('Avg Bearer TP UL (kbps)', 'mean'),
        handset=('Handset Type', lambda x: x.mode()[0] if not x.mode().empty else 'Unknown')  
    ).reset_index()

    st.subheader("Top and Bottom Experience Metrics")
    st.write("Top 10 Average TCP DL Retransmission")
    st.write(experience_metrics.nlargest(10, 'avg_tcp_dl'))

    st.write("Bottom 10 Average TCP DL Retransmission")
    st.write(experience_metrics.nsmallest(10, 'avg_tcp_dl'))

    st.write("Top 10 Average RTT DL")
    st.write(experience_metrics.nlargest(10, 'avg_rtt_dl'))

    st.write("Top 10 Average Throughput DL")
    st.write(experience_metrics.nlargest(10, 'avg_bearer_tp_dl'))

    st.subheader("User Experience Clustering")
    scaler_exp = StandardScaler()
    exp_scaled = scaler_exp.fit_transform(experience_metrics[['avg_tcp_dl', 'avg_rtt_dl', 'avg_bearer_tp_dl']])
    kmeans_exp = KMeans(n_clusters=3)
    experience_metrics['Cluster'] = kmeans_exp.fit_predict(exp_scaled)

    st.write("Experience Clusters")
    st.write(experience_metrics[['IMSI', 'Cluster']])

    st.write("Cluster Statistics")
    exp_cluster_stats = experience_metrics.groupby('Cluster').agg({
        'avg_tcp_dl': ['mean', 'max', 'min'],
        'avg_rtt_dl': ['mean', 'max', 'min'],
        'avg_bearer_tp_dl': ['mean', 'max', 'min']
    })
    st.write(exp_cluster_stats)

if section == "Customer Satisfaction":
    st.title("Customer Satisfaction Analysis")

    if 'engagement_metrics' not in locals() or 'experience_metrics' not in locals():
        st.error("Please generate User Engagement and User Experience metrics first.")
    else:
        st.subheader("Engagement and Experience Scores")

        engagement_metrics['Engagement_Score'] = np.sqrt(
            (engagement_metrics['total_sessions'] - engagement_metrics['total_sessions'].min())**2 +
            (engagement_metrics['total_duration'] - engagement_metrics['total_duration'].min())**2 +
            (engagement_metrics['total_data'] - engagement_metrics['total_data'].min())**2
        )

        experience_metrics['Experience_Score'] = np.sqrt(
            (experience_metrics['avg_tcp_dl'] - experience_metrics['avg_tcp_dl'].max())**2 +
            (experience_metrics['avg_rtt_dl'] - experience_metrics['avg_rtt_dl'].max())**2 +
            (experience_metrics['avg_bearer_tp_dl'] - experience_metrics['avg_bearer_tp_dl'].max())**2
        )

        satisfaction_data = pd.merge(engagement_metrics[['IMSI', 'Engagement_Score']],
                                     experience_metrics[['IMSI', 'Experience_Score']],
                                     on='IMSI')

        satisfaction_data['Satisfaction_Score'] = satisfaction_data[['Engagement_Score', 'Experience_Score']].mean(axis=1)

        st.write("Top 10 Satisfied Customers")
        st.write(satisfaction_data.nlargest(10, 'Satisfaction_Score'))

        st.subheader("Satisfaction Clustering")
        kmeans_sat = KMeans(n_clusters=2)
        satisfaction_data['Satisfaction_Cluster'] = kmeans_sat.fit_predict(satisfaction_data[['Engagement_Score', 'Experience_Score']])

        st.write("Satisfaction Clusters")
        st.write(satisfaction_data[['IMSI', 'Satisfaction_Cluster']])

        st.write("Cluster Stats")
        satisfaction_stats = satisfaction_data.groupby('Satisfaction_Cluster').agg({
            'Satisfaction_Score': ['mean', 'max', 'min'],
            'Engagement_Score': ['mean', 'max', 'min'],
            'Experience_Score': ['mean', 'max', 'min']
        })
        st.write(satisfaction_stats)
