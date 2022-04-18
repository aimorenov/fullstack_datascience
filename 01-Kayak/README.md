**Bloc no 1: Kayak project**  
Construction and supply of a data management infrastructure
==============================  

**Project:**  The marketing team would like to create a an application that will recommend people where to plan their next holidays. The application should use real data from:  
* Weather in the next seven given days. 
* Hotels in the area

**Goals:**   

* Scrape data from destinations
* Get weather data from each destination
* Get hotels' info found in each destination
* Store all the information above in a data lake (s3)
* Extract, transform and load cleaned data from your datalake to a data warehouse

**Deliverables:** 

* A .csv file in an S3 bucket containing enriched information about weather and hotels for the top 35 best french cities to visit

* An SQL Database where we should be able to get the same cleaned data from S3

* Two maps where you should have a Top-5 destinations and a Top-20 hotels in the area




Project Organization
------------
01-Kayak
├── **01_cities_weather.ipynb** <- notebook for scraping of weather and gps info for top 35 French cities  
├── **02_booking_scrap1.ipynb** <- notebook for scraping of hotel info for top 35 French cities
├── **02_booking_scrap2.ipynb** <- notebook for scraping of hotel locations for top 35 French cities 
├── **03_s3_db.ipynb** <- notebook for storing of scraping results into S3 bucket
├── **04_etl.ipynb** <- notebook for creating database instance, storing and querying scraped data downloaded from S3 bucket . Maps generated here
├── config <-
│   ├── AWS_bucket_policy.txt <- policy bucket to be modified in S3 bucket creation
├── **data**
│   ├── interim
│   │   ├── scrap1_hotels_topcities_booking.csv
│   │   └── top_35_cities_france_normalized_names.txt
│   ├── processed
│   │   ├── scrap1_hotels_topcities_booking-clean.csv
│   │   ├── scrap2_hotels_topcities_booking.csv
│   │   ├── top_35_cities_france_gpscoord.csv
│   │   └── top_35_cities_france_weather_7days.csv
│   └── raw
│       └── top_35_cities_france.txt
├── **reports**
│   └── figures
│       ├── 01-Kayak_aws_bucket_creation.png <- screenshot validating S3 bucket creation
│       └── 01-Kayak_awsrds_dbpushed-pgadmin-check.png <- screenshot validating AWS RDS db instance creation and loading of SQL tables
├── requirements_kayak.txt <-requirements for reproducing the analysis environment
├── **results <- deliverables**
│   ├── **01-Kayak_map_cities_bestweather-top10hotels.png** <- map of top 10 hotels found for top 5 cities to visit based on best weather over 7 days
│   ├── **01-Kayak_map_cities_bestweather.png** <- map of top 5 cities to visit based on best weather over 7 days
│   ├── **scrap_booking_s3.csv** <- scraping result containing scraped hotel information and location for best 35  French cities
│   └── **top_35_cities_france_weather_gps.csv** <- scraping result containing gps and weather information (over 7 days) for best 35  French cities
├── setup.py <-make project pip installable (pip install -e .) so src can be imported
└── **src**
    ├── __init__.py <- make src a Python module
    ├── **booking_scrap1.py** <- spiders to scrap hotel information
    ├── **booking_scrap2.py** <- spiders to scrap hotel location
    ├── **cities_weather.py** <- functions to scrap weather and gps data from nominatim and openweather APIs
    └── credentials.py <- get credentials for AWS

--------

