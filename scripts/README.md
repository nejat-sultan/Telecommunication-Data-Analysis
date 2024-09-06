This folder contains Python scripts for analyzing telecom user behavior. The key functionalities are:

- **`top_10_handsets(df)`**
  - Identifies the top 10 handsets used by customers.

- **`top_3_manufacturers(df)`**
  - Finds the top 3 handset manufacturers.

- **`top_5_handsets_per_manufacturer(df)`**
  - Lists the top 5 handsets for each of the top 3 manufacturers.

- **`aggregate_user_data(df)`**
  - Aggregates user data, including number of sessions, session duration, and total data volume.

- **`handle_missing_values(df)`**
  - Replaces missing values with column means.

- **`perform_eda(df)`**
  - Performs exploratory data analysis with basic metrics.

- **`perform_pca(df)`**
  - Reduces dimensionality using Principal Component Analysis (PCA).

- **`compute_engagement_metrics(df)`**
  - Computes engagement metrics and identifies top 10 engaged users.

- **`run_kmeans_clustering(df, k=3)`**
  - Clusters users into `k` groups using K-means clustering.
