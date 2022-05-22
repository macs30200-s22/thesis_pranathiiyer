import matplotlib.pyplot as plt

import pandas as pd
import numpy as np

labels = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]
num_sikhs = [  201.30081301,   853.36813681,  2367.26530612,    97.5       ,
        3918.55907173, 33860.54702495,  4290.83870968, 12912.06217617,
        2224.10820896, 19324.67151163, 16425.96774194, 55666.18077803,
       12801.9047619 , 12013.0515873 ]
num_jats = [   92.72469636,   386.00701208,  1234.        ,     0.        ,
        4566.21472393,  3527.49884527,  9595.11936805, 26986.42009132,
        4030.90980881,  2227.19640565,  1145.66918919,  3419.02354949,
         828.09330454,  3089.32767233]
brides = [619, 2252, 2468,300, 5011, 35213, 9983, 27342,4869, 21783, 16823, 56879, 14590, 16789 ]

def plot():
    df = pd.DataFrame({'sikhs':np.array(num_sikhs).round(3).tolist()[4:], 'jats': np.array(num_jats).round(3).tolist()[4:], 'total ads': brides[4:]}, index = labels)
    ax = df.plot.bar(rot=0,figsize = (12,8), title = 'Proportion of sikh/jat ads in bride seeking ads', colormap = 'Paired')

                  