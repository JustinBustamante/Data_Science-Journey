Key Changes Made
Package Loading: Redundant package loading statements have been removed, and packages are loaded at the beginning of the script for clarity.

Data Preprocessing: The code is structured to allow the same clustering and visualization steps to be applied to both raw and normalized datasets. This reduces code duplication and enhances maintainability.

Comments and Structure: Comments have been added to explain the purpose of each code section. The code is organized into functions and sections to improve readability.

Variable Naming: Variable names have been made more descriptive.

Consistency: Consistency has been maintained in function calls and data processing techniques.

Clustering Methods: The code provides examples of various clustering methods, including K-means, PAM, and hierarchical clustering. Results are visualized using the factoextra package.

Optimal Cluster Number: The code includes the determination of the optimal number of clusters based on clustering tendency and silhouette analysis.

Usage
Load the dataset using read.csv.

Use the perform_clustering function to perform clustering and visualize results. You can specify the dataset and the desired number of clusters (k).

Adjust the k value to experiment with different numbers of clusters.

Analyze the visualizations and clustering results to gain insights from your data.

