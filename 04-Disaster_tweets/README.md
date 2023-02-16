**Bloc no 4: Disaster Tweets**  
Predictive analysis of unstructured data using artificial intelligence
==============================  

**Project:**  Using Natural Language Processing, builg a deep learning model that predicts which tweets are about real disasters and which ones are not. A train set of manually annotated tweets will be given, as well as a test set for which the prediction should be done.

This dataset was part of a [Kaggle competition](https://www.kaggle.com/competitions/nlp-getting-started).  

**Goals:**   

Build a machine learning model that can best predict if a posted tweet is or is not about a real disaster. 

    - Carry out all the necessary cleaning, encoding, tokenization and padding of text to feed to the chosen model  
    - Train a baseline deep learning model for a simple binary classification problem and evaluate its performance over n epochs
    - Compare other deep learning models to baseline and define if f1 score of prediction can be improved  

**Deliverables:** 

*Model*    

`results/submissions.csv`: predictions on test set of tweet category  using best identified model (0 == not disaster; 1 == disaster) *formatted as per Kaggle competition requirements*   

`models/baseline_sequential_binaryclass.h5`: best identified model 

`NLP_disaster_tweet_project.ipynb` : model containing all code to clean text and train models 

*source code* containing functions used to clean text etc in notebook





Code
------------  
All code can be found in: 
* One notebook (ran in Google colab):
    - `NLP_disaster_tweet_project.ipynb`

<br>
    
Project Organization
------------

```markdown
.
├── NLP_disaster_tweet_project.ipynb
├── README.md
├── data <- as downloaded  from Kaggle competition
│   ├── test.csv
│   └── train.csv
├── models
│   └── baseline_sequential_binaryclass.h5
├── results
│   └── submission.csv
└── src <- functions used throughout notebook
    ├── text_cleaning.py
    └── word_cts.py
````
