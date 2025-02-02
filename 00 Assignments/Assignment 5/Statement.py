# Task 1: Data Wrangling
# Objective:
# Clean and preprocess a given dataset by handling missing data, dealing with outliers, and transforming the data for further analysis.
# Dataset:
# Use the Seaborn Titanic dataset (seaborn.load_dataset("titanic")).
# Steps to Follow:
# 1. Data Loading:
#    Load the Titanic dataset using seaborn.load_dataset("titanic").
# 2. Missing Data Handling:
#    Identify and report the missing values in the dataset.
#    Fill the missing values:
#    For numerical columns (age, fare), impute using the median.
#    For categorical columns (embarked, deck), impute using the mode.
# 3. Outlier Detection:
#    Identify outliers in the age and fare columns using the IQR method (Interquartile Range).
#    Handle the outliers by either removing them or replacing them with the median of the column.
# 4. Feature Transformation:
#    Create a new feature family_size: Combine the sibsp and parch columns.
#    Create an age_group feature: Categorize passengers into "Child", "Adult", and "Senior" based on their age.
# 5. Categorical Data Encoding:
#    Convert the sex column into a numerical format using Label Encoding (1 for male, 0 for female).
# 6. Normalization:
#    Normalize the age and fare columns using MinMax scaling.


# Task 2: Exploratory Data Analysis (EDA)
# Objective:
# Perform an exploratory analysis on the Titanic dataset to derive insights and visualize patterns.
# Dataset:
# Use the Seaborn Titanic dataset.
# Steps to Follow:
# 1. Univariate Analysis:
#    Plot histograms for numerical features (age, fare, family_size).
#    Visualize the distribution of the survived column using a countplot.
# 2. Bivariate Analysis:
#    Create a boxplot to show the distribution of fare based on the class feature.
#    Create a violin plot to explore how age varies across different class values.
#    Plot the correlation matrix of numerical features using a heatmap.
# 3. Group-wise Analysis:
#    Group the data by the survived column and calculate the mean of age, fare, and family_size for both survivors and non-survivors.
#    Create a bar plot to show the average fare for survivors vs. non-survivors.
# 4. Multivariate Analysis:
#    Create a pairplot to visualize the relationships between age, fare, and family_size with survived as the hue.
#    Use a stacked bar plot to compare the survival rate across different class values and sex.
