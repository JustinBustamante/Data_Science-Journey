Improved Clustering Analysis
Overview
This notebook focuses on clustering analysis to segment customers based on their buying behavior. The notebook explores different clustering techniques and metrics to find the optimal number of clusters.

Data Source
The dataset used is the Sales Transactions Dataset Weekly, which can be found here.

Key Features
Data Preprocessing
Standardization of the data using StandardScaler.
Exploratory Data Analysis (EDA)
Summary statistics
Data visualizations
Clustering Techniques
K-Means Clustering: Uses the Elbow Method and Silhouette Score to determine the optimal number of clusters.
DBSCAN: Density-Based Spatial Clustering of Applications with Noise (Not implemented but imported for potential use).
Metrics
Within-Cluster Sum of Squares (WCSS): Used in the Elbow Method to find the optimal number of clusters.
Silhouette Score: Measures how similar an object is to its own cluster compared to other clusters.
Cluster Interpretation
Mean values of features for each cluster are calculated to interpret the characteristics of each cluster.
How to Use
Run the Notebook: Execute all cells in the notebook.
Interpret Results: The notebook will output the optimal number of clusters and the characteristics of each cluster.
Libraries Used
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn