import gensim
import numpy as np #For arrays
import pandas as pd #Gives us DataFrames
import matplotlib.pyplot as plt #For graphics
import seaborn as sns #Makes the graphics look nicer
import sklearn.metrics.pairwise #For cosine similarity
import sklearn.manifold #For T-SNE
import sklearn.decomposition #For PCA


from sklearn import preprocessing
import os #For looking through files
import os.path #For managing file

grooms_wanted = gensim.models.Word2Vec.load("grooms_wanted")

def normalize(vector):
    normalized_vector = vector / np.linalg.norm(vector)
    return normalized_vector

def dimension(model, positives, negatives):
    diff = sum([normalize(model[x]) for x in positives]) - sum([normalize(model[y]) for y in negatives])
    return diff

Gender = dimension(grooms_wanted.wv, ['girl', 'woman', 'female'], ['groom', 'boy', 'man', 'male'])

affluence = ['sikh', 'jat', 'manglik', 'khatri']
appearance = ['fair','beautiful','tall','handsome', 'young','slim', 'short', 'graceful', 'progressive', 'intelligent',
             'traditional', 'pretty', 'attractive', 'strong',  'gentle', 'smart', 'brilliant', 'honest',
             'kind', 'religious']
occupation =['engineer','doctor','businessman','executive','lecturer',  'officer', 'manufacturer', 'dentist', 'nurse', 'industrialist', 'accountant',
            'psychologist', 'lawyer',  'chemist', 'manager','professor', 'inspector', 'secretary', 'instructor']


def makeDF(model, word_list):
    c = []
    g = []
  
    for word in word_list:
        
        #c.append(sklearn.metrics.pairwise.cosine_similarity(brides_wanted_W2V.wv[word].reshape(1,-1), Caste.reshape(1,-1))[0][0])
        #o.append(sklearn.metrics.pairwise.cosine_similarity(brides_wanted_2002W2V.wv[word].reshape(1,-1), occupation.reshape(1,-1))[0][0])
        g.append(sklearn.metrics.pairwise.cosine_similarity(model[word].reshape(1,-1), Gender.reshape(1,-1))[0][0])
    df = pd.DataFrame({'gender': g}, index = word_list)
    return df
    
    
def Coloring(Series):
    x = Series.values
    y = x-x.min()
    z = y/y.max()
    c = list(plt.cm.copper(z))
    return c
style = dict(size=10, color='copper')
def PlotDimension(ax,df, dim):
    ax.set_frame_on(False)
    ax.set_title('Female', fontsize = 26)
    colors = Coloring(df[dim])
    for i, word in enumerate(df.index):
        ax.annotate(word, (0, df[dim][i]), color = colors[i], alpha = 1, fontsize = 20)
 
    
    MaxY = df[dim].max()
   
    MinY = df[dim].min()
    plt.annotate("",
            xy=(1, MinY), xycoords='data',
            xytext=(1, MaxY), textcoords='data',
            arrowprops=dict(arrowstyle="<->",
                            connectionstyle="arc3", color='black', lw=2),
            )
    plt.ylim(MinY,MaxY)
    plt.yticks(())
    plt.xticks(())


def final_plot():
    Occsdf = makeDF(grooms_wanted.wv, occupation)
    # groom seeking adjustments for occupations only to increase interpretability and remove overlapping words. 
    Occsdf.loc['professor'] = -.12
    Occsdf.loc['officer'] = -.03
    Occsdf.loc['instructor']=-.02
    Occsdf.loc['engineer'] = -.10
    Occsdf.loc['secretary'] = -.08
    Occsdf.loc['executive'] = -.068
    
    fig = plt.figure(figsize = (16,10))
    ax1 = fig.add_subplot(131)

    PlotDimension(ax1, Occsdf, 'gender')
    plt.xlabel('Male', fontsize = 26)
    plt.axhline(y = 0, linestyle ='dashed', color = 'black')

    plt.show()
