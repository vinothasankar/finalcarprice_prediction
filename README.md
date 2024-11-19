newc.ipynb,omcars.ipynb - Source code for data preprocessing and model development.
price.py - Deployed Streamlit application for price prediction.
car_price.png - screenshot of streamlit app

Approach:
 Data Processing
Imported all city’s dataset which is in unstructured format.
Converted it into a  structured format.
Added a new column named ‘City’ and assign values for all rows with the name of the respective city.
Concatenate all datasets and make it as a single dataset.
Handled Missing Values: Identified  and filled missing values in the dataset, using techniques like mean, median, or mode imputation.depending upon its skew value

Standardising Data Formats:
Checked for all data types and did the necessary steps to keep the data in the correct format.


Encoding Categorical Variables: Converted categorical features into numerical values using encoding techniques.
Use one-hot encoding for nominal categorical variables.

Normalizing Numerical Features: 
Applied Min-Max Scaling to scale numerical features to a standard range

Removed Outliers: Identifed and removed  outliers for kms_Driven price in the dataset to avoid skewing the model.
Used IQR (Interquartile Range) method and Z-score analysis.



 Exploratory Data Analysis (EDA)
Descriptive Statistics: Calculate summary statistics to understand the distribution of data.
Mean, median, mode, standard deviation, etc.

Data Visualization: Created visualizations to identify patterns and correlations.
Used scatter plots, histograms, box plots, and correlation heatmaps.

Feature Selection: Identified important features that significantly impact the car prices.
Used techniques like correlation analysis, feature importance from models.

 Model Development
 
Train-Test Split: Splited the dataset into training and testing sets to evaluate model performance.


Model Selection: 
Values showed that randomforest model performed well among Linear Regression,Support Vector Rregression,Decision Tree Regressor,Random Forest Regressor,
Ridge
So choose it as appropriate machine learning algorithms for price prediction.




Model Training: Trained the selected models on the training dataset.

Used cross-validation techniques to ensure robust performance.
Did Hyperparameter Tuning to Optimize model parameters to improve performance.
Used techniques like Grid Search or Random Search.

 Model Evaluation
Performance Metrics: Evaluated model performance using relevant metrics.
Mean Absolute Error (MAE), Mean Squared Error (MSE), R-squared.

obtained accuracy - 87%
 Deployment
Streamlit Application: Deployed the final model using Streamlit to create an interactive web application.
that allows users to input car features and get real-time price predictions.

User Interface Design: Ensured that the application is user-friendly and intuitive.

obtained(R-Squared Score: 0.8691390591709017) 87% accuracy
