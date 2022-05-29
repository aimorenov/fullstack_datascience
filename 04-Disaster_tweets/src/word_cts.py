# Function to count frequency of words in cleaned text (obtained from text_cleaning.py)
import pandas as pd
import nltk


def word_freq(clean_text):

    # Tokenize
    tokens = nltk.word_tokenize(clean_text)
    tokens = [token.lower() for token in tokens if len(token) > 1]

    # Create dictionnary of unigrams: (code obtained from https://stackoverflow.com/questions/12821201/what-are-ngram-counts-and-how-to-implement-using-nltk)
    unigrams = {}
    for token in tokens:
        if token not in unigrams:
            unigrams[token] = 1
        else:
            unigrams[token] += 1

    # Convert to dataframe and sort by frequency
    unigram_df = pd.DataFrame(unigrams.values(),index=unigrams.keys()).reset_index()
    unigram_df.columns = ['word', 'frequency']

    # Sort by frequency of words 
    unigram_df.sort_values(by='frequency', ascending=False, inplace=True)
    return unigram_df