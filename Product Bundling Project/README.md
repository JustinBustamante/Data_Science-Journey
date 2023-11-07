Product Bundling Recommendation System
Overview
This notebook aims to build a product bundling recommendation system using machine learning and data mining techniques. The system suggests bundles of products that are often bought together.

Data Source
The dataset used is the Sales Transactions Dataset Weekly, which can be found here.

Key Features
Data Preprocessing
Handling missing values
Data type conversions
Scaling
Exploratory Data Analysis (EDA)
Summary statistics
Distributions
Correlations among features
Model Building
Two main techniques are used for product bundling:

K-Means Clustering: Segments customers into different groups based on their buying habits.
Association Rule Mining: Finds associations between different products.
K-Means Clustering
Data is standardized using StandardScaler.
Optimal number of clusters is determined using the Elbow method.
Association Rule Mining
Uses the Apriori algorithm to find frequent itemsets.
Generates association rules based on 'lift'.
How to Use
K-Means Recommendations: After running the K-Means section, you'll get customer segments that can be targeted for specific types of product bundles.
Association Rule Recommendations: The Apriori algorithm will provide you with rules that tell you which products are often bought together.
Libraries Used
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
mlxtend