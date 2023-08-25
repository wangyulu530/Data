# Book Review Data Linear regression model Analysis
## Introduction

This project aims to analyze a dataset containing book review data and build a linear regression model to predict the average rating of books based on several features.

## Dataset
The dataset for this model is clean by my colleague, including title, authors, average rating, ratings count, text reviews count, and number of pages.

## Data Analysis
1. **Data Cleaning:** The dataset was loaded and any leading spaces in column names were removed.

2. **Data Visualization:** Various visualizations were created to understand the relationships between features and the target variable.

   - `sns.pairplot`: This produces a pairplot that shows scatter plots of the variables against each other, helping us understand the relationships between them.
   - `sns.heatmap`: This creates a correlation heatmap, visualizing the correlation coefficients between the variables. Brighter colors indicate stronger correlations.
   - Scatter Plot: A scatter plot was created to visualize the actual average ratings against the predicted average ratings. This helps see how well the model's predictions align with the actual values.

3. **Linear Regression:**
   - **Features:** The model was trained using the features - average rating, ratings count, text reviews count, and number of pages. Independent variables (`X`) were selected as 'average_rating', 'ratings_count', 'text_reviews_count', and 'num_pages', and the target variable (`y`) was set as 'average_rating'.
   - **Training and Testing:** Data was split into training and testing sets using `train_test_split`.
   - **Model Training:** The Linear Regression model was initialized and fitted on the training data.
   - **Predictions:** Predictions were made on the test data using the trained model.
   - **Evaluation:** Mean Squared Error (MSE) and R-squared score (R2) were calculated to evaluate the model's performance.

4. **Results:**
   - **Mean Squared Error:** 1.4161653979210159e-30
   - **R-squared:** 1.0
   - **Interpretation:**
     - The extremely low MSE and perfect R2 score indicate that the model's predictions are almost identical to the actual values. However, achieving a perfect R2 score is unusual in real-world scenarios and might suggest overfitting or data leakage.
     - Extremely low MSE and perfect R2 score could also indicate data leakage or some issues with the data.

5. **Double Check: Possibility of Multicollinearity:**
   - Correlation matrix among the independent variables (average_rating, ratings_count, text_reviews_count, num_pages) showed weak correlations between the features, indicating no severe multicollinearity.

6. **Multicollinearity Check:**
   - Correlation matrix among the independent variables (average_rating, ratings_count, text_reviews_count, num_pages) and visualizes it using a heatmap.

   |               | average_rating | ratings_count | text_reviews_count | num_pages |
   |---------------|----------------|---------------|--------------------|-----------|
   | average_rating| 1.000000       | 0.038205      | 0.033734           | 0.150809  |
   | ratings_count | 0.038205       | 1.000000      | 0.865979           | 0.034353  |
   | text_reviews_count| 0.033734    | 0.865979      | 1.000000           | 0.036998  |
   | num_pages     | 0.150809       | 0.034353      | 0.036998           | 1.000000  |

   - **Interpretation of Correlations:**
     - average_rating vs. ratings_count: Very weak positive correlation.
     - average_rating vs. text_reviews_count: Very weak positive correlation.
     - average_rating vs. num_pages: Weak positive correlation.
     - ratings_count vs. text_reviews_count: Strong positive correlation.
     - ratings_count vs. num_pages: Very weak positive correlation.
     - text_reviews_count vs. num_pages: Very weak positive correlation.

![Correlation Heatmap](link_to_your_heatmap_image.png)

## Conclusion
Based on our analysis, we can conclude that there appears to be a strong linear relationship between the independent variables and the average rating of books. However, the perfect R-squared value in the linear regression model raises questions about potential overfitting or other factors influencing the results. Therefore, it is advisable to further validate the model's performance and consider additional factors that might affect book ratings.

Moreover, the absence of multicollinearity among the independent variables suggests that they are not strongly correlated, which enhances the reliability of the regression model's coefficients.

