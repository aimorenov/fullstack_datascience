**Bloc no 2: Speed dating project**  
Exploratory Data Analysis (EDA)
==============================  

**Project:**  A dataset from the Columbia Business School was collected from participants in experimental speed dating events from 2002-2004. Participants of the event had a speed date with every other participant of the opposite sex and had to decide at the end it they wanted to see their partner or not. They also filled in a questionnaire where they scored different attributes of  a partner based on the importance they gave to them: Attractiveness, Sincerity, Intelligence, Fun, Ambition, and Shared Interests.  

This dataset was part of a [Kaggle competition](https://www.kaggle.com/datasets/annavictoria/speed-dating-experiment)

**Goals:**   

* Carry out an exploratory analysis of the data to identify different patterns such as:
    - Most important attributes per sex or race
    - Distribution of different characteristics of participants (age, gender, race, field of study)
    - etc

**Deliverables:** 

* Two notebooks enabling the EDA, containing inside all created graphs:
    - Notebook `01_data_cleaning_description`: 
    - Notebook  `02_variable_correlations_exploration`


Code
------------  
All code can be found in: 
* **01_data_cleaning_description.ipynb** Notebook for cleaning and first description of variables  
* **02_variable_correlations_exploration.ipynb** Notebook  where I evaluate certain variables to identify patterns 





Project Organization
------------

```markdown
├── 01_data_cleaning_description.ipynb
├── 02_variable_correlations_exploration.ipynb
├── config
├── data
│   ├── interim
│   ├── processed
│   │   └── Speed_Dating_Data.csv <- cleaned data without duplicates
│   └── raw
│       └── Speed Dating Data.csv
├── references
│   └── Speed Dating Data Key.pdf <- variables documentation
└── src
    ├── __init__.py
    └── data_cleaning.py <- functions used in both notebooks
```