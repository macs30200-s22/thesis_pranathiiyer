import nltk
import pandas as pd#gives us DataFrames
import matplotlib.pyplot as plt #For graphics
import wordcloud #Makes word clouds
import numpy as np #For divergences/distances
import scipy #For divergences/distances
import seaborn as sns #makes our plots look nicer
import sklearn.manifold
import lucem_illud
import analysis

def kl_divergence(X, Y):
    P = X.copy()
    Q = Y.copy()
    P.columns = ['P']
    Q.columns = ['Q']
    df = Q.join(P).fillna(0)
    p = df.iloc[:,1]
    q = df.iloc[:,0]
    D_kl = scipy.stats.entropy(p, q)
    return D_kl

def chi2_divergence(X,Y):
    P = X.copy()
    Q = Y.copy()
    P.columns = ['P']
    Q.columns = ['Q']
    df = Q.join(P).fillna(0)
    p = df.iloc[:,1]
    q = df.iloc[:,0]
    return scipy.stats.chisquare(p, q).statistic

def Divergence(corpus1, corpus2, difference="KL"):
    """Difference parameter can equal KL, Chi2, or Wass"""
    freqP = nltk.FreqDist(corpus1)
    P = pandas.DataFrame(list(freqP.values()), columns = ['frequency'], index = list(freqP.keys()))
    freqQ = nltk.FreqDist(corpus2)
    Q = pandas.DataFrame(list(freqQ.values()), columns = ['frequency'], index = list(freqQ.keys()))
    if difference == "KL":
        return kl_divergence(P, Q)
    elif difference == "Chi2":
        return chi2_divergence(P, Q)
    elif difference == "KS":
        try:
            return scipy.stats.ks_2samp(P['frequency'], Q['frequency']).statistic
        except:
            return scipy.stats.ks_2samp(P['frequency'], Q['frequency'])
    elif difference == "Wasserstein":
        try:
            return scipy.stats.wasserstein_distance(P['frequency'], Q['frequency'], u_weights=None, v_weights=None).statistic
        except:
            return scipy.stats.wasserstein_distance(P['frequency'], Q['frequency'], u_weights=None, v_weights=None)
        
def heat_map():
    df1 = analysis.tokenize('data/grooms_data/grooms-wanted_2001.csv')
    df2 = analysis.tokenize('data/grooms_data/grooms-wanted_2002.csv')
    df3 = analysis.tokenize('data/grooms_data/grooms-wanted_2003.csv')
    df4 = analysis.tokenize('data/grooms_data/grooms-wanted_2005.csv')
    df5 = analysis.tokenize('data/grooms_data/grooms-wanted_2006.csv')
    df6 = analysis.tokenize('data/grooms_data/grooms-wanted_2007.csv')
    df7 = analysis.tokenize('data/grooms_data/grooms-wanted_2008.csv')
    df8 = analysis.tokenize('data/grooms_data/grooms-wanted_2009.csv')
    df9 = analysis.tokenize('data/grooms_data/grooms-wanted_2010.csv')
    df10 = analysis.tokenize('data/grooms_data/grooms-wanted_2011.csv')
    df11 = analysis.tokenize('data/grooms_data/grooms-wanted_2012.csv')
    df12 = analysis.tokenize('data/grooms_data/grooms-wanted_2013.csv')
    df13 = analysis.tokenize('data/grooms_data/grooms-wanted_2014.csv')
    
    corpora = []
    for df in [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13]:
        t = df['tokenized_ads'].tolist()
        flat_list = [item for sublist in t for item in sublist]
        corpora.append(flat_list)
        
    fileids = [2001, 2002, 2003, 2005, 2006,2007, 2008,2009, 2010, 2011, 2012, 2013, 2014 ]
    L = []
    for p in corpora:
        l = []
        for q in corpora:
            l.append(Divergence(p,q, difference = 'KL'))
        L.append(l)
    M = np.array(L)
    fig = plt.figure()
    div = pd.DataFrame(M, columns = fileids, index = fileids)
    ax = sns.heatmap(div)
    plt.title('KL Divergence between bride seeking ads across years')
    plt.show()

if __name__ == '__main__':
    heat_map()