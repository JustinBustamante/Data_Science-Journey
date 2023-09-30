# Install and load necessary libraries in a specific order

# Install the required packages (add this line)
install.packages(c("recommenderlab", "ggplot2", "data.table", "reshape2", "dplyr", "tidyr"))

# Load the libraries
library(recommenderlab)
library(ggplot2)
library(data.table)
library(reshape2)
library(dplyr)
library(tidyr)

# Specify file paths for your data
movies_file <- "C:/Users/Justin & Janie/Documents/GitHub/Data_Science-Journey/Beginner_Projects/Movie Recommendation System - Enhanced Efficiency and Clarity/Original Project/IMDB-Dataset/movies.csv"
ratings_file <- "C:/Users/Justin & Janie/Documents/GitHub/Data_Science-Journey/Beginner_Projects/Movie Recommendation System - Enhanced Efficiency and Clarity/Original Project/IMDB-Dataset/ratings.csv"

# Read movie and rating data
movie_data <- read.csv(movies_file, stringsAsFactors = FALSE)
rating_data <- read.csv(ratings_file)

# Data preprocessing (You can add your data preprocessing code here)
# Example: One-hot encoding of movie genres
# Example: Removing movies with too few ratings

# Convert rating matrix into a recommenderlab sparse matrix
ratingMatrix <- dcast(rating_data, userId ~ movieId, value.var = "rating", na.rm = FALSE)
ratingMatrix <- as.matrix(ratingMatrix[, -1]) # Remove userIds
ratingMatrix <- as(ratingMatrix, "realRatingMatrix")

# Overview some important parameters for building recommendation systems for movies
recommendation_model <- recommenderRegistry$get_entries(dataType = "realRatingMatrix")

# Implementing a single model in the R project – Item Based Collaborative Filtering
recommen_model <- Recommender(
  data = ratingMatrix,
  method = "IBCF",
  parameter = list(k = 30)
)

# Exploring the data science recommendation system model
model_info <- getModel(recommen_model)

# Generate recommendations for the top 2 users with 10 recommendations each
num_users_to_recommend <- 2
top_recommendations <- 10
user_recommendations <- list()

for (i in 1:num_users_to_recommend) {
  user_recommendations[[i]] <- predict(object = recommen_model, newdata = ratingMatrix[i, , drop = FALSE], n = top_recommendations)
}

# Print recommendations for the top 2 users with movie titles
for (i in 1:num_users_to_recommend) {
  user_movies <- user_recommendations[[i]]@items[[1]]
  movie_titles <- as.character(subset(movie_data, movie_data$movieId %in% user_movies)$title)
  
  cat("User", i, "Recommendations:", movie_titles, "\n")
}

# Additional code for visualization or analysis can be added here
