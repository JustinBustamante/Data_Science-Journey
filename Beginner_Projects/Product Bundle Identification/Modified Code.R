# Load necessary libraries
library(cluster)
library(cclust)
library(fastcluster)
library(caret)
library(mlbench)
library(Rcmdr)
library(pmml)
library(kohonen)
library(factoextra)
library(magrittr)
library(mclust)
library(NbClust)

# Function to perform clustering and visualize results
perform_clustering <- function(data, k) {
  set.seed(123)
  # Compute K-means clustering
  km.res <- kmeans(data, k, nstart = 25)
  
  # Visualize
  fviz_cluster(km.res, data = data,
               ellipse.type = "convex",
               palette = "jco",
               ggtheme = theme_minimal())
  
  # Compute PAM
  pam.res <- pam(data, k)
  
  # Visualize
  fviz_cluster(pam.res)
  
  # Compute hierarchical clustering
  res.hc <- data %>%
    scale() %>%
    dist(method = "euclidean") %>%
    hclust(method = "ward.D2")
  
  # Visualize using factoextra
  fviz_dend(res.hc, k = k, cex = 0.5, k_colors = c("#2E9FDF", "#00AFBB", "#E7B800", "#FC4E07"),
            color_labels_by_k = TRUE, rect = TRUE)
  
  # Assess clustering tendency
  gradient.color <- list(low = "steelblue",  high = "white")
  data %>%
    scale() %>%
    get_clust_tendency(n = 50, gradient = gradient.color)
  
  # Determine the optimal number of clusters
  res.nbclust <- data %>%
    scale() %>%
    NbClust(distance = "euclidean", min.nc = 2, max.nc = 10, method = "complete", index = "all")
  
  # Visualize
  fviz_nbclust(res.nbclust, ggtheme = theme_minimal())
  
  # Silhouette analysis
  res.hc <- data %>%
    scale() %>%
    eclust("hclust", k = k, graph = FALSE)
  fviz_silhouette(res.hc)
}

# Load the dataset
df <- read.csv('https://archive.ics.uci.edu/ml/machine-learning-databases/00396/Sales_Transactions_Dataset_Weekly.csv')

# Perform clustering and visualization on raw dataset (r_df1)
raw_data <- df[, 2:53]
perform_clustering(raw_data, k = 6)

# Perform clustering and visualization on normalized dataset (r_df)
normalized_data <- df[, 56:107]
perform_clustering(normalized_data, k = 6)
