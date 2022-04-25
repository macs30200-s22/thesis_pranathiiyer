
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np 
import spacy
import subprocess
import nltk
nlp = spacy.load("en_core_web_sm")


stop_words_freq = ['for','well', 'no', 'and','with','only','match','invited','bar','d','bam', 'alliance','invited', 'a','by',
                   'looking','family','our', 'in','from','note','send','please','do','not','any','your','reply','they','can',
                   'be', 'images','photographs','forwarded','due','to','technical','reasons','suitable', 'uly72/5"','born'
                  'ma','bed','cantt','8910abol','23/5\x923\x94','girl','email', 'dd','m', 'boy']

def tokenize(data):
    '''
    Tokenizes all ads for the data of a given year
    Input: data (a csv file)
    Returns: pandas dataframe with a column of tokenized_ads
    '''
    df = pd.read_csv(data)
    df = df.drop_duplicates(keep = 'first')
    df.dropna(how = 'any', inplace = True)
    df.columns = ['ads']
    df['tokenized_ads'] = df.apply(lambda row: nltk.word_tokenize(row['ads']), axis=1)
    return df

def word_to_count(data):
    '''
    Returns a word count for every word in the tokenized ads
    Input: data (a csv file)
    Returns: a dictionary of words and their counts
    '''
    wordCounts = {}
    data = tokenize(data)
    for row in data['tokenized_ads']:
        for word in row:
            if word not in stop_words_freq:
                wLower = word.lower()
                if wLower in wordCounts:
                    wordCounts[wLower] += 1
                else:
                    wordCounts[wLower] = 1
            else:
                continue
    return wordCounts
        
        
def counts_data(wordCounts):
    '''
    creates a dataframe for words and their counts
    Input: dictionary of words and their counts
    Returns a pandas dataframe of words and counts
    '''
    countsForFrame = {'word' : [], 'count' : []}
    for w, c in wordCounts.items():
        countsForFrame['word'].append(w)
        countsForFrame['count'].append(c)
    return pd.DataFrame(countsForFrame)
    

def normalizeTokens(word_list, extra_stop= stop_words_freq):
    '''
    Normalizes words of all ads/texts in the data
    Input: a list of words to be normalized
           a list of stop words 
    Returns a list of normalized words 
    '''
    normalized = []
    if type(word_list) == list and len(word_list) == 1:
        word_list = word_list[0]

    if type(word_list) == list:
        word_list = ' '.join([str(elem) for elem in word_list]) 

    doc = nlp(word_list.lower())
    if len(extra_stop) > 0:
        for stopword in extra_stop:
            lexeme = nlp.vocab[stopword]
            lexeme.is_stop = True

    for w in doc:
        if w.text != '\n' and not w.is_stop and not w.is_punct and not w.like_num and len(w.text.strip()) > 0:
            normalized.append(str(w.lemma_))

    return normalized


def spacy_pos(word_list):
    '''
    Tags parts of speech for all ads/texts
    Input: list of tokenized ads
    Returns: a list of tuples of words and their tags
    '''
    tags = []
    if type(word_list) == list:
        word_list = ' '.join([str(elem) for elem in word_list])
    doc = nlp(word_list.lower())
    for w in doc:
        tags.append((w.text, w.tag_))
    return tags

def final_func(data, savefigs = True, path_1 = './word_counts.tiff', path_2 = './proper_nouns.tiff'):
    '''
    The final function that brings together all functions to create the final plot
    Input: data(csv file)
    Returns: nothing, just creates a plot, and saves it optionally
    '''
    df = tokenize(data)
    normalized_tokens = df['tokenized_ads'].apply(lambda x: normalizeTokens(x, stop_words_freq))
    normalized_tokens_POS= df['tokenized_ads'].apply(lambda x: spacy_pos(x))
    bridesfdist_POStoWord = nltk.ConditionalFreqDist((p, w) for w, p in normalized_tokens_POS.sum())
    bridesfdist = nltk.ConditionalFreqDist(((len(w), w) for w in normalized_tokens.sum()))
    if savefigs:
        fig_1 = plt.figure(figsize = (10,4))
        plt.gcf().subplots_adjust(bottom=0.15)
       
        bridesfdist[3].plot(15, title = "Counts of top 15 three letter words")
        plt.show()
        fig_1.savefig(path_1,
                    dpi=300,
                    format="tiff",
                    bbox_inches="tight",
                    pil_kwargs={"compression": "tiff_lzw"})
        fig_2 = plt.figure(figsize = (10,4))
        plt.gcf().subplots_adjust(bottom=0.15)
        bridesfdist_POStoWord['NNP'].plot(20, title="Top 20 proper nouns")
        plt.show()
        fig_2.savefig(path_2,
                    dpi=300,
                    format="tiff",
                    bbox_inches="tight",
                    pil_kwargs={"compression": "tiff_lzw"})
    else:
        
        bridesfdist[3].plot(15, title = "Counts of top 15 three letter words")
        bridesfdist_POStoWord['NNP'].plot(20, title="Top 20 proper nouns")

if __name__=='__main__':
    final_func(data)
 