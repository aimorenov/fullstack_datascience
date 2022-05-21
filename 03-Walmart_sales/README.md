**Bloc no 3: Walmart Sales**  
Predictive analysis of strutctured data using artificial intelligence
==============================  

**Project:**  A dataset a dataset containing information about weekly sales achieved by different Walmart stores, and other variables such as the unemployment rate, fuel price or a measure of inflation (CPI).

This dataset was part of a [Kaggle competition](https://www.kaggle.com/competitions/walmart-sales-forecasting/overview) and was modified by Jedha.

**Goals:**   

Build a machine learning model that can best predict weekly sales for Walmart stores using different kind of features. 

    - Carry out an exploratory data analysis (EDA) to identify feature distributions, missing values, colinearities and relationships between explanatory features
    - Define pre-processing pipeline for scaling and imputation of missing values in data 
    - Create new features from patterns observed in EDA, and define if they improve model performance  
    - Train a first baseline linear regression model to predict weekly sales using selected explanatory variables   
    - Reduce any overfitting observed in baseline via Ridge and or Lasso regularization. Define best hyperparameters to tune for each regularization function   
    - Train another regressor to compare to baseline e.g. Random Forest Regressor 
    - Once best model has been identified, evaluate its robustness through a cross validation

**Deliverables:** 

*Model*  
`pipeline_preprocess_ridgepredictor.joblib`: best identified predictor. 

*EDA visualizations* : target and explanatory variables distribution and correlation, identification of groups of stores based on certain variables. 

*Notebooks with code* for reproduction of preprocessing and model training*





Code
------------  
All code can be found in: 
* Four notebooks:
    - `01-EDA.ipynb`: Exploratory Data Analysis
    - `02-data_processing.ipynb`: Missing value imputation, scaling, feature engineering, pre-processing pipelines  
    - `03-train_model.ipynb`: Split test vs train datasets, train baseline model
    - `04-model_selection.ipynb` : Fight overfitting via regularisation (establish best hyperparameters via gridsearch), compare to other regressors, cross validation 
* Python scripts of functions associated to notebooks (inside src folder). 

**Requirements.txt** can be found in root of all projects aimorenov/fullstack_datascience

<br>
    
Project Organization
------------

```markdown
├── 01-EDA.ipynb
├── 02-data_processing.ipynb
├── 03-train_model.ipynb
├── 04-model_selection.ipynb
├── README.md
├── data
│   ├── interim
│   │   ├── Walmart_Store_sales-expvar-basic.csv
│   │   ├── Walmart_Store_sales-expvar-feateng.csv
│   │   ├── Walmart_Store_sales-targetvar.csv
│   │   └── Walmart_Store_sales.csv
│   ├── processed
│   │   ├── Walmart_Store_sales-expvar-test-basic.npz
│   │   ├── Walmart_Store_sales-expvar-train-basic.npz
│   │   ├── Walmart_Store_sales-target-test-basic.csv
│   │   └── Walmart_Store_sales-target-train-basic.csv
│   └── raw
│       └── Walmart_Store_sales.csv
├── models <- pipeline of best identified pre-processing and model
│   └── pipeline_preprocess_ridgepredictor.joblib
├── references <- documentation of data
│   └── Walmart_store_sales_dictionary.txt
├── results <- visualisations of different notebooks  
│   ├── 01-EDA_explanatory_variables_distribution.png
│   ├── 01-EDA_store_groups_CPI_unemployment.png
│   ├── 01-EDA_target_variable_distribution-permonthyear.png
│   ├── 01-EDA_target_variable_distribution.png
│   ├── 01-EDA_variables_corr.png
│   └── 04-Best_model_Ridge_crossval.png
└── src <- functions and or variables used in the different notebooks
    ├── __init__.py
    ├── data
    │   └── data_processing.py
    ├── features
    │   └── build_features.py
    └── visualization
        └── visualize.py
```

Information for jury member of certification
------------ 
For any questions regarding project please contact me at aimorenov.jedhacertif[at]gmail[dot]com indicating name of project or bloc. I will be happy to answer.  

Link to [video describing project]() 
