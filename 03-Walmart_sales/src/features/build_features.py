from cmath import nan
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import SimpleImputer, IterativeImputer
from sklearn.preprocessing import  StandardScaler, OneHotEncoder
from feature_engine.imputation import RandomSampleImputer
from sklearn.compose import ColumnTransformer


# Function to create store categories based on weekly sales, CPI and unemployment
def store_cat_fn(data, thresh_sales, thresh_CPI, thresh_unemp, outlier_samp):
    
    df = data.copy()

    # Define variables meeting thresholds
    highsales_highCPI = (df['Weekly_Sales'] >= thresh_sales) & (df['CPI'] >= thresh_CPI)
    highsales_lowCPI = (df['Weekly_Sales'] >= thresh_sales) & (df['CPI'] < thresh_CPI)
    lowsales_lowCPI = (df['Weekly_Sales'] < thresh_sales) & (df['CPI'] < thresh_CPI)
    lowsales_highCPI = (df['Weekly_Sales'] < thresh_sales) & (df['CPI'] >= thresh_CPI)

    highsales_highunemp = (df['Weekly_Sales'] >= thresh_sales) & (df['Unemployment'] >= thresh_unemp)
    highsales_lowunemp = (df['Weekly_Sales'] >= thresh_sales) & (df['Unemployment'] < thresh_unemp)
    lowsales_lowunemp = (df['Weekly_Sales'] < thresh_sales) & (df['Unemployment'] < thresh_unemp)
    lowsales_highunemp = (df['Weekly_Sales'] < thresh_sales) & (df['Unemployment'] >= thresh_unemp)

    outlier= (df['Store_str']==outlier_samp)

    # Create columns containing NA values for storing of new categories
    NaN = np.nan
    df['Store_group_CPI'] = NaN
    df['Store_group_unemp'] = NaN

    df.loc[highsales_highCPI,'Store_group_CPI'] = 'highsales_highCPI'
    df.loc[highsales_lowCPI, 'Store_group_CPI'] = 'highsales_lowCPI'
    df.loc[lowsales_lowCPI, 'Store_group_CPI'] = 'lowsales_lowCPI'
    df.loc[lowsales_highCPI, 'Store_group_CPI'] = 'lowsales_highCPI'
    df.loc[outlier, 'Store_group_CPI'] = 'outlier'

    df.loc[highsales_highunemp, 'Store_group_unemp'] = 'highsales_highunemp'
    df.loc[highsales_lowunemp, 'Store_group_unemp'] = 'highsales_lowunemp'
    df.loc[lowsales_lowunemp, 'Store_group_unemp']= 'lowsales_lowunemp'
    df.loc[lowsales_highunemp, 'Store_group_unemp'] = 'lowsales_highunemp'
    df.loc[outlier, 'Store_group_unemp'] = 'outlier'

    return df

# Dictionary: quarter to string equivalent
quarter_dic = {1.0:'q1', 2.0:'q2', 3.0:'q3', 4.0:'q4'}

# Dictionary: year to string equivalent
year_dic = {2010.0:'y1', 2011.0:'y2', 2012.0:'y3'}



# Function to categorize temperature by ranges (bins)
def temp_bin_fn(data, temp_col, temp_low, temp_high):
    
    df = data.copy()

    # Define category thresholds using bins
    bins = [-np.inf, temp_low, temp_high, np.inf]
    names = ['low_temp','mean_temp','high_temp']

    # Bin values into discrete intervals
    return pd.cut(data[temp_col].to_numpy(), bins,labels=names).tolist()




# Function to categorize fuel price 
def fuel_cat_fn(data, median_fuel):
    
    df = data.copy()

    # Define variables meeting thresholds
    below_median_price = (df['Fuel_Price'] <= median_fuel)
    above_median_price = (df['Fuel_Price'] > median_fuel)

    # Create columns containing NA values for storing of new categories
    NaN = np.nan
    df['Fuel_Price_group'] = NaN

    df.loc[below_median_price, 'Fuel_Price_group'] = 'below_median_price'
    df.loc[above_median_price, 'Fuel_Price_group'] = 'above_median_price'

    return df

# Build dataframe with most important holidays and (religious) events in the USA for the years 2010/2011/2012
usa_hols_ls = ['2010-01-01', '2010-01-18', '2010-02-05','2010-02-14', '2010-03-31', '2010-05-09','2010-07-05', '2010-09-06', '2010-09-06','2010-11-11', '2010-11-25', '2010-12-24', '2010-12-31',
'2011-01-01','2011-01-17','2011-03-30', '2011-07-04','2011-09-05', '2011-11-11', '2011-11-24', '2011-12-26',
'2012-01-01', '2012-01-16','2012-02-05','2012-02-14', '2012-05-28', '2012-07-04', '2012-09-03', '2012-11-12', '2012-11-22', '2012-12-25']

usa_hols_df = pd.DataFrame({'date_str':usa_hols_ls})
usa_hols_df['date']= pd.to_datetime(usa_hols_df['date_str'], infer_datetime_format=True)
usa_hols_df['year'] = usa_hols_df['date'].dt.year
usa_hols_df['weekofyear'] = usa_hols_df['date'].dt.isocalendar().week
usa_hols_df['weekofyear_holiday'] = 1 

# Final dataframe: keep only weekof year and flag for presence holiday in such week
usa_hols_df.drop(['date','date_str'], axis=1, inplace=True)

# Convert year to string
usa_hols_df['year'] = usa_hols_df['year'].map(year_dic)


#### Pipelines for missing value imputations / scaling and one hot encoding

# Basic numerical variables: Fuel_Price, Temperature, Unemployment
# Based on distibution of data, use median for imputation
basic_num_feats = [2, 3, 5, 7] 
eng_num_feats = [1] 
basic_num_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

# Categories: Store_str, quarter, holiday flag
cat_feat = [0, 1, 4]
cat_transformer = Pipeline(
    steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')), 
    ('encoder', OneHotEncoder(drop='first')) # first column will be dropped to avoid creating correlations between features
    ])


# CPI (binomial distribution)
cpi_feat = [6]
cpi_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('scaler', StandardScaler())
])


# Basic variables with more complex distribution: quarter, CPI (binomial distribution)
# Multivariate imputation with Bayesian ridge: include already imputed temperature to aide imputation of other variables
basic_multivar_feats = [1, 3, 5, 6]
basic_multivar_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])






# Engineered categorical variables: Temperature_group, Store_group_CPI, Store_group_unemp
# Impute most frequent and one hot encode 
eng_cat_feats = [2, 3, 4]
eng_cat_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(drop='first'))
])


# Random sample imputer on categorical quarter and weekofyear_holiday (since difficult to impute precisely) 
eng_rand_feats = [0, 5] 
eng_rand_transformer = Pipeline(steps=[
    ('imputer', RandomSampleImputer(random_state=0)),
    ('encoder', OneHotEncoder(drop='first'))
])
