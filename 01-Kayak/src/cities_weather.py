import requests
import pandas as pd
import json

# Create dataframe of city names with and without french accents
filename = 'data/raw/top_35_cities_france.txt'
with open(filename) as file:
    top_cities_ls = [line.rstrip() for line in file]

filename = 'data/interim/top_35_cities_france_normalized_names.txt'
with open(filename) as file:
    top_cities_clean_ls = [line.rstrip() for line in file]

cities_meta_df =  pd.DataFrame({'city': top_cities_ls, 'city_clean' : top_cities_clean_ls})

# Retrieve latitude and longitude from nominatim API
def req_gps_fn(x):
    return(requests.get("https://nominatim.openstreetmap.org/search?q={}&country=France&format=jsonv2".format(x)).json())


# Retrieve weather information from openweathermap API
def req_weather_fn(x,y,key):
    return(requests.get("https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=hourly,minutely&units=metric&appid={}".format(x,y,key)).json())



# Transform request list of dictionary responses into single dataframe
def req_to_df_fn(api_res):
    try:
        api_keys=api_res[0][0].keys()
    except:
        api_keys=api_res[0].keys()
    print('Number of API keys retrieved in request response: ', len(api_keys))

    # Convert every response dictionary to dataframe: output in list of lists
    api_df_ls = []
    try:
        for r in api_res:
            api_df_ls.append(pd.DataFrame(r, columns = api_keys))
    # In case there are nested dictionaries:
    except:
          for r in api_res:
            api_df_ls.append(pd.DataFrame.from_dict(r, orient='index').transpose())    
    
    print('List of dataframes per API result. Length: ', len(api_df_ls))

    # Merge list of dataframes into single dataframe
    api_df = pd.concat(api_df_ls)
    print('Merged API requests dataframe shape: ', api_df.shape)
    return(api_df)


# Explode nested dictionaries in daily column
def explode_df_fn(df, column):
    #Explode nested dictionary of chosen column using json_normalize
    df_explode = df.join(pd.json_normalize(df[column]))
    df_explode.drop(columns=[column], inplace=True)

    #Create new names of columns in order to be able to choose columns if needed
    column_names=df_explode.columns[0:4].tolist()
    column_names.append('Today')
    names_7days=['Day_'+str(df_explode.columns[x]) for x in range(5,12)]
    column_names=column_names+ names_7days
    column_names

    #Update new column names
    df_explode.columns=column_names
    return(df_explode)

# Explode dictionary found within a chosen day to have all info on weather for each day
def explode2_df_fn(col_name,df_exploded):
    #Subset first columns
    df_explode2=df_exploded.iloc[:,0:4]
    #Explode df
    df_explode3=df_explode2.join(pd.json_normalize(df_exploded[col_name]))
    df_explode3['Day']=col_name
    return(df_explode3)



# List of all exploded dataframes for chosen days
def explodeall_df_fn(days_ls, df_exploded):
    #List of exploded dataframes for each day
    df_all_ls=[explode2_df_fn(x, df_exploded) for x in days_ls]
    print("Explosion done for all: {} days".format(len(df_all_ls)))

    #Concatenate all into a single dataframe
    weather_7Dexp_df=pd.concat(df_all_ls)
    print("Shape of df:{}".format(weather_7Dexp_df.shape))
    print("Verify unique days:",pd.unique(weather_7Dexp_df.Day))

    #Update name of columns: replace '.' by '_'
    weather_7Dexp_df.columns=[str.replace(".","_") for str in weather_7Dexp_df.columns.tolist()]
    return(weather_7Dexp_df)
