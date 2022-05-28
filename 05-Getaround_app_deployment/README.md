**Bloc no 5: Getaround dashboard and prediction endpoint**  
Industrialization of a machine learning algorithm and automation of decision-making processes
==============================  

**Project:**  Getaround is a company that enables people to rent a car for a couple of hours up to a few days. Users are supposed to bring the car back on time, however there can be late checkouts which results in friction with the next driver if the next checkin is impacted. 

Two datasets for the company are analysed in this projetc:  
1. `get_around_pricing_project` containing information regarding a car (e.g. model, mileage, fuel etc) and the rental price per day  
2. `get_around_delay_analysis` containing information for unique rentals and their checkout times, delay at checkout time, time delta with a successive rental etc


**Goals:**  
There are two different goals for this project:  
1. Build a machine learning model that predicts the rental price per day for a car based on different properties of the car. Deploy such model to an API endpoint that users can access using json requests.  
2. Construct a dashboard that enables the analysis of successive rentals and impact of late checkouts on next rental. Create an interactive board enabling the evaluation of setting a minimum threshold of time delta between chained rentals to see if problematic cases are solved or not.  

**Deliverables:**  

- API endpoint available on Heroku domain: `https://getaroundprice-app-amv.herokuapp.com/predict`, together with its [documentation page](https://getaroundprice-app-amv.herokuapp.com)  

    - Model developed to predict rental price per day for a given car:  `api_endpoint/models/reg_model.joblib`

<br> 

- Dashboard available on Heroku domain: [https://getaround-dashboard-amv.herokuapp.com/](https://getaround-dashboard-amv.herokuapp.com/)  

- All the code used to create previous two applications  

*Note: loading of Heroku domains may take a few seconds as account on Heroku is free user*  

<br>

Code
------------  
Code has been separated in two different files for dasboard and api endpoint: 
* API endpoint:
    - `app.py`: Code in Flask for API endpoint app  
    *Notebooks:*  
    - `data_eda.ipynb`: Quick exploratory analysis to identify explanatory variables in dataset, check for missing values and/or outliers 
    - `model_training.ipynb`: Split test vs train datasets, train baseline regression model and compare to other models to choose the one with best performance and stability (cross validation)  - best model stored as `reg_model.joblib`
    - `test_endpoint.ipynb` : Test API endpoint is working     
<br> 

* Dashboard:  
    - `app.py`: Code in streamlit for dashboard app  
    - `get_around_delay_analysis.ipynb`: Notebook for exploring data and evaluating the best graphical representations to be used in dashboard
<br> 

A `requirements.txt` and a `Procfile` are present for both apps for correct deployment (`setup.sh` is also included for streamlit app)  

<br>
    
Project Organization
------------  

```markdown  
.
├── api_endpoint
│   ├── Procfile
│   ├── app.py
│   ├── data
│   │   ├── get_around_pricing_project_clean.csv
│   │   └── get_around_pricing_project_raw.csv
│   ├── models
│   │   └── reg_model.joblib
│   ├── notebooks
│   │   ├── data_eda.ipynb
│   │   ├── model_training.ipynb
│   │   └── test_endpoint.ipynb
│   ├── requirements.txt
│   ├── templates
│   │   └── index.html
│   └── train.py
└── dashboard
    ├── Procfile
    ├── app.py
    ├── data
    │   ├── processed
    │   │   └── get_around_delay_analysis.csv
    │   └── raw
    │       └── get_around_delay_analysis.xlsx
    ├── get_around_delay_analysis.ipynb
    ├── getaround_logo.png
    ├── requirements.txt
    └── setup.sh  
````
<br>

Information for jury member of certification
------------ 
For any questions regarding project please contact me at aimorenov.jedhacertif[at]gmail[dot]com indicating name of project or bloc. I will be happy to answer.  

Link to [video describing project](https://share.vidyard.com/watch/266yKAbFW2TazvcoCjqMvu?)     


