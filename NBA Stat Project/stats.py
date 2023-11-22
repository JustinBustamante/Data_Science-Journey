import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

def main():
    # Load the dataset
    file_path = 'path_to_your_nba_stats.csv'  # Replace with your file path
    nba_data = pd.read_csv(file_path)

    # Preprocessing
    nba_data['min'] = pd.to_timedelta(nba_data['min']).dt.total_seconds() / 60
    nba_data.fillna(nba_data.mean(), inplace=True)

    # Feature Engineering
    nba_data['PER'] = (nba_data['pts'] + nba_data['reb'] + nba_data['ast'] + nba_data['stl'] + nba_data['blk']) \
                      - ((nba_data['fga'] - nba_data['fgm']) + (nba_data['fta'] - nba_data['ftm']) + nba_data['turnover'])

    # EDA and Visualization
    corr_matrix = nba_data.corr()
    plt.figure(figsize=(10, 6))
    sns.heatmap(corr_matrix, annot=True)
    plt.title('Correlation Matrix of NBA Stats')
    plt.show()

    # Player Clustering
    features_for_clustering = ['pts', 'reb', 'ast', 'stl', 'blk', 'PER']
    X_cluster = nba_data[features_for_clustering]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_cluster)
    kmeans = KMeans(n_clusters=5, random_state=42)
    nba_data['Cluster'] = kmeans.fit_predict(X_scaled)

    # Clusters visualization
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=nba_data['Cluster'], palette='viridis')
    plt.title('Player Clusters based on Performance')
    plt.xlabel('PCA Component 1')
    plt.ylabel('PCA Component 2')
    plt.show()

    # Predictive Modeling - Predicting Player Points
    X = nba_data[['min', 'fgm', 'fga', 'reb', 'ast', 'stl', 'blk', 'turnover']]
    y = nba_data['pts']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)

    # Regression model performance
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred)
    plt.xlabel('Actual Points')
    plt.ylabel('Predicted Points')
    plt.title('Actual vs Predicted Player Points')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=4)
    plt.show()

    # Print MSE
    print(f"Mean Squared Error of the regression model: {mse}")

if __name__ == "__main__":
    main()
