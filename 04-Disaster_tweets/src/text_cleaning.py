### Functions to clean text text
# Functions used are based on what was seen during course at Jedha and by looking up specifically cleaning of texts (since texts have hastags and other elemnts specific to texts such as userid, retext indication etc)
# Some of the text cleaning sources from which I inspired myself are: Catris Code (Lia Ristiana)  and Bicachu (John Bica)

import pandas as pd
import re
import gensim # IMPORTANT: use gensim for importing stopwords as kernel crashed when importing spacy on M1 chips 
import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

## ------------  If wanting to use spacy for importing stop words:  NOT USABLE ON M1 CHIPS (usable on google colab)
# pip install -U pip setuptools wheel
# pip install -U spacy
# python -m spacy download en_core_web_sm

# import en_core_web_sm
# nlp = en_core_web_sm.load()
# # Import Stop words 
# from spacy.lang.en.stop_words import STOP_WORDS

## ----------------


# Define string of punctuations
punctuation = '!"$%&\'()*+,-./:;<=>?[\\]^_`{|}~•@'

# Stopwords
stopwords = gensim.parsing.preprocessing.STOPWORDS


## Subfunctions to be implemented in a final cleaning function

# Remove users
def remove_users(text):
    """Takes a string and removes retext and @user information"""
    text = re.sub('(RT\s@[A-Za-z]+[A-Za-z0-9-_]+)', '', text)  # remove re-tweet
    text = re.sub('(@[A-Za-z]+[A-Za-z0-9-_]+)', '', text)  # remove tweeted at
    return text

# Remove urls and other links
def remove_links(text):
    """Takes a string and removes web links from it"""
    text = re.sub(r'http[s]?://\S+', '', text)   # remove http or https links
    text = re.sub(r"www.\S+", "", text) # remove www. links
    text = re.sub(r'bit.ly/\S+', '', text)  # remove bitly links
    text = text.strip('[link]')   # remove any other links [links]
    text = re.sub(r'pic.twitter\S+','', text) # remove media url (pictures)
    return text


# Remove hastags
def remove_hashtags(text):
    """Takes a string and removes any hash tags"""
    text = re.sub('(#[A-Za-z]+[A-Za-z0-9-_]+)', '', text)  # remove hash tags
    return text


# Remove audio/video tags or labels
def remove_av(text):
    """Takes a string and removes AUDIO/VIDEO tags or labels"""
    text = re.sub('VIDEO:', '', text)  # remove 'VIDEO:' from start of text
    text = re.sub('AUDIO:', '', text)  # remove 'AUDIO:' from start of text
    return text


# Tokenization and removal of stop words
def tokenize(text):
    """Returns tokenized representation of words in lemma form excluding stopwords"""
    result = []
    for token in gensim.utils.simple_preprocess(text): # convert into list of tokens (lowercase, tokenize and de-accent)
        if token not in stopwords \
                and len(token) > 2:  # drops words with less than 3 characters
            result.append(lemmatize(token))
    return result


# Lemmatization
def lemmatize(token):
    """Returns lemmatization of a token"""
    return WordNetLemmatizer().lemmatize(token, pos='v')


## Final cleaning function
def preprocess_text(text):
    """Main master function to clean texts, stripping noisy characters, and tokenizing use lemmatization"""
    text = remove_users(text)
    text = remove_links(text)
    text = remove_hashtags(text)
    text = remove_av(text)
    text = text.lower()  # lower case
    text = re.sub('[' + punctuation + ']+', ' ', text)  # strip punctuation defined previously
    text = re.sub('\s+', ' ', text)  # remove double spacing
    text = re.sub('([0-9]+)', '', text)  # remove numbers
    text_token_list = tokenize(text)  # apply lemmatization and tokenization
    text = ' '.join(text_token_list)
    return text

