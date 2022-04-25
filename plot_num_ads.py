import matplotlib.pyplot as plt
import pandas as pd

def data_size(data):
    '''
    Gets the length of the data
    Input: data(csv file)
    Returns length(int) of the data
    '''
    df = pd.read_csv(data)
    df = df.drop_duplicates( keep = 'first')
 
    return len(df)

def plot_fig(savefig = True, path = './num_ads.tiff'):
    '''
    plots the number of ads across years for brides and grooms
    Input: none
    Returns: nothing, just plots the figure and d=saves it optionally
    '''
    x_1 = []
    x = []
    y = [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]
    for data in ['data/brides_data/brides-wanted_2001.csv', 'data/brides_data/brides-wanted_2002.csv', 'data/brides_data/brides-wanted_2003.csv', 'data/brides_data/brides-wanted_2004.csv',
                'data/brides_data/brides-wanted_2005.csv', 'data/brides_data/brides-wanted_2006.csv', 'data/brides_data/brides-wanted_2007.csv', 'data/brides_data/brides-wanted_2008.csv',
                'data/brides_data/brides-wanted_2009.csv']:
        x.append(data_size(data))
    for data in ['data/grooms_data/grooms-wanted_2001.csv', 'data/grooms_data/grooms_wanted_2002.csv', 'data/grooms_data/grooms-wanted_2003.csv', 'data/grooms_data/grooms-wanted_2004.csv',
                'data/grooms_data/grooms-wanted_2005.csv', 'data/grooms_data/grooms-wanted_2006.csv', 'data/grooms_data/grooms-wanted_2007.csv', 'data/grooms_data/grooms-wanted_2008.csv',
                'data/grooms_data/grooms-wanted_2009.csv']:
        x_1.append(data_size(data))

    plt.plot(y , x, label = 'brides wanted')
    plt.plot(y, x_1, label = 'grooms wanted')
    plt.legend(loc = 'upper left')
    if savefig:
        plt.savefig(path,
                    dpi=300,
                    format="tiff",
                    bbox_inches="tight",
                    pil_kwargs={"compression": "tiff_lzw"})
  
    plt.show()

if __name__=="__main__":
    plot_fig(savefig=True, path="./num_ads.tiff")