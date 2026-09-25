# Smart-Aquaculture-Water-Quality-Index-Prediction-using-Machine-Learning
## Project Overview

Water quality is one of the most critical factors affecting aquaculture productivity and fish health. Poor water quality can lead to disease outbreaks, reduced growth, and significant economic losses.

This project develops an end-to-end Machine Learning solution to predict the **Water Quality Index (WQI)** of aquaculture systems using physicochemical water parameters. Multiple regression algorithms are compared, the best-performing model is optimized using hyperparameter tuning.

A Streamlit web application is also developed for real-time prediction and batch prediction.

 # Objectives

- Predict Water Quality Index (WQI) using Machine Learning.
- Compare multiple regression models.
- Perform comprehensive Exploratory Data Analysis (EDA).
- Apply feature engineering and preprocessing.
- Improve model performance using hyperparameter tuning.
- Deploy the final model using Streamlit.

#  Dataset
- The dataset contains physicochemical parameters collected from aquaculture ponds.

  ### Example Features

- Temperature
- Dissolved Oxygen
- pH
- Salinity
- Turbidity
- Conductivity
- Ammonia
- Nitrate
- Nitrite
- Phosphate

### Target Variable

- Water Quality Index (WQI)

 ## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Joblib

  # 📊 Exploratory Data Analysis

The following analyses were performed:

- Dataset Overview
- Missing Value Analysis
- Duplicate Value Detection
- Descriptive Statistics
- Correlation Analysis
- Distribution Analysis
- Boxplots
- Histograms
- Pairplots
- Feature Relationship Analysis

---

## Data Preprocessing

The preprocessing pipeline includes:

- Missing value handling
- Duplicate removal
- Feature selection
- Train-Test Split
- Feature Scaling
- Data validation

## Machine Learning Models
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor
  
 ##  Model Evaluation Metrics

The models were evaluated using:

- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² Score
- MAPE (Mean Absolute Percentage Error)

## Hyperparameter Tuning

Model performance was improved using:

- GridSearchCV
- RandomizedSearchCV
- 5-Fold Cross Validation

## Project Structure

```
│
├── data/
│     aquaculture.csv
│
├── notebooks/
│     01_EDA.ipynb
│     02_Preprocessing.ipynb
│     03_Model_Training.ipynb
│     04_Hyperparameter_Tuning.ipynb
│
├── models/
│     best_model.pk

├── requirements.txt
├── README.md
```
## Results

- Successfully compared multiple Machine Learning algorithms.
- Identified the best-performing regression model.
- Improved prediction accuracy using hyperparameter tuning.

## Author

**Shiva Gupta**
M.Tech in Aquacultural Engineering

Interested in:

- Machine Learning
- Data Science
- Explainable AI
- Aquaculture Analytics






























