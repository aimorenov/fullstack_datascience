**Bloc no 6: Agribalyse personal project**  
Administration of data management projects
==============================  

**Team members:** Malika Berrehail, Patricia Escalera, Aura Moreno Vega and Anatole Reffet 

**Project:**  My environmental footprint: Using public data from the project [Agribalyse](https://doc.agribalyse.fr/documentation/), train a model to calculate the environmental footprint of a given list of ingredients (making up a dish)

**Goals:**   

* Extract, explore, feature engineer, pre-process and reduce the dimensions of agribalyse data   
* Train different supervised regression models to best predict the environmental footprint of a list of user input ingredients   
* Deploy trained model in heroku as a streamlit web application allowing user to input list of ingredients and retrieve score 


**Deliverables:** 

* Heroku url enabling use of application: [https://envfoodprint.herokuapp.com/](https://envfoodprint.herokuapp.com/)  

* Trained model enabling prediction of environmental score: `models/score_predictor_v2.joblib` 

* Requirements.txt enabling reproduction of analysis environment 

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<br>

Information for jury member of certification
------------  
For any questions regarding  project please contact me at aimorenov.jedhacertif[at]gmail[dot]com indicating name of project or bloc. I will be happy to answer.  

Link to [video describing project](). 

Link to [presentation](https://docs.google.com/presentation/d/185ejQaOt2GTbjXWeCmsGH0QB1--7aQehxDAITkcTnH0/edit?usp=sharing)

<br><br>

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
