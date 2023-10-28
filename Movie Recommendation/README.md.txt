Movie Recommendation System
Overview
This script provides a movie recommendation system using three different approaches:

Content-Based Filtering
Collaborative Filtering
Hybrid (Content-Based + Collaborative)
Data
We used two datasets:

movies.csv: Contains movie titles and genres.
ratings.csv: Contains user ratings for movies.
Features
Content-Based Filtering
Algorithm: TF-IDF (Term Frequency-Inverse Document Frequency) for text vectorization and Cosine Similarity for calculating similarity.
Input: Movie title
Output: Top-N similar movies based on genres.
Collaborative Filtering
Algorithm: k-Nearest Neighbors (k-NN) with cosine similarity.
Input: User ID
Output: Top-N recommended movies based on similar users' ratings.
Hybrid
Algorithm: Combines Content-Based and Collaborative Filtering.
Input: Movie title and User ID
Output: Top-N similar movies to the given movie, sorted by predicted ratings for the given user.

How to Use
Content-Based Recommendations

content_based_recommendations('Toy Story (1995)', top_n=10)


Collaborative Filtering Recommendations

collaborative_filtering_recommendations(1, top_n=10)

Hybrid Recommendations

hybrid_recommendations('Toy Story (1995)', 1, top_n=10)
