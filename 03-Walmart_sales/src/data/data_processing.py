import pandas as pd
import datetime
import calendar

# Month list
month_en_ls = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Function to convert a string date format into datetime and extract date features from such datetime
def convert_date_fn(df,datecol):
    """
    Creates time series features from datetime index.
    """
    df = df.copy()
    df['date']=pd.to_datetime(df[datecol], infer_datetime_format=True)
    df['dayofweek'] = df['date'].dt.weekday
    df['quarter'] = df['date'].dt.quarter
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year
    df['dayofyear'] = df['date'].dt.dayofyear
    df['dayofmonth'] = df['date'].dt.day
    df['weekofyear'] = df['date'].dt.isocalendar().week 
    
    # Dictionary with equivalent days and weekday
    days_dic = {'dayofweek': range(0,7), 
    'dayofweek_en':["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]}

    # Dictionary with equivalent of month names
    month_dic = {'month': range(1,13), 
    'month_en':["Jan", "Feb", "Mar", "Apr", "May", "Jun", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]}

    # Dataframes from dictionaries for merging
    days_df = pd.DataFrame(days_dic)
    month_df = pd.DataFrame(month_dic)

    # Merge days_dic for name of dayofweek
    X = df.merge(days_df, how='left', on='dayofweek').merge(month_df, how='left', on='month', copy=False )

    # Order output
    X = X[['Store', 'date', 'dayofweek', 'dayofweek_en', 'quarter', 'month', 'month_en', 'year',
           'dayofyear','dayofmonth','weekofyear', 'Weekly_Sales', 'Holiday_Flag', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']]
    
    return X



# Function to group input data frame and carry out aggregated sum or mean
def group_df_agg_fn(df,group_col, col_eval, aggfn, div_by, div=True):
       df_gp= df.copy()
       df_gp=df_gp.groupby([group_col])[[col_eval]].agg(aggfn).sort_values(by=[col_eval],ascending=False).rename(columns={col_eval: aggfn + '_' + col_eval})
       if True==div:
              df_gp[aggfn + '_' + col_eval] = df_gp[aggfn + '_' + col_eval]/div_by
              print('{} ({})'.format(aggfn + '_' + col_eval, "{:.2e}".format(div_by)))
              return df_gp
       else:
              return df_gp
