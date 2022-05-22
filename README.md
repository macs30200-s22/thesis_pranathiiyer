The code and data in this repository are a preliminary step towards the final objective of understanding the structure, trends, relevance,and success of matrimonial advertisements in the Indian context, throught this project. While this repository currently contains advertisements for prospective brides and grooms from the year 2001 to 2009, and 2014, the final project will also have data for 2010, 2011, 2012, and 2013.These years are slightly difficult to scrape owing to changes in the website. The data for grooms can be found under ```grooms_data``` in the folder ```data```, and the data for brides can be found under ```brides_data``` in the folder ```data```.

The code is written in Python 3.9.10 and all of its dependencies can be installed by running the following in the terminal (with the requirements.txt file included in this repository):

                         pip install -r requirements.txt
                         
Then, you can import the analysis and plot_num_ads module located in this repository to reproduce the analysis in the project that this code supplements (in a Jupyter Notebook, like README.ipynb in this repository, or in any other Python script):

### Findings
It is extremely challenging to reproduce the tables generated in first section of the results section. This is because the analysis involves running a code for individual years and then synthesizing relevant words and presenting them in a tabular format. However, you can generate year-wise proper nounns and top three character words for either category of ads for any year as shown below.


```python
analysis.final_func('data/brides_data/brides-wanted_2008.csv')
```


    
![png](README_files/README_2_0.png)
    



    
![png](README_files/README_2_1.png)
    


The above commands can easily be run for any of the files from the data folder to reproduce other analyses.


You can use the file ```sikh_jat_ads.py``` to successfully generate the first figure of the paper. You can also run the command below to generate the plot.


```python
import sikh_jat_ads
```


```python
sikh_jat_ads.plot()
```


    
![png](README_files/README_6_0.png)
    


You can run use the file ```KL_divergence_grooms.py``` and ```KL_divergence_brides.py``` to generate the heat maps in figure 2. You can also run the following command to generate the results.


```python
import KL_divergence_brides
```


```python
KL_divergence_brides.heat_map()
```


    
![png](README_files/README_9_0.png)
    


You can run the same command using ```KL_divergence_grooms``` to generate the second heatmap.

You can generate the projections in Figure 3 and Figure 4 using the files ```groom_projection_adjectives.py```, ```groom_projection_occupations.py```, ```brides_projection_adjectives.py```, and ```bride_projection_occupations.py```. You can run the commands below to generate the results.


```python
import groom_projection_adjectives
```


```python
groom_projection_adjectives.final_plot()
```


    
![png](README_files/README_13_0.png)
    


You can run the same command on ```groom_projection_occupations.py``` to generate the projection of occupational words.


```python
import brides_projection_adjectives
```


```python
brides_projection_adjectives.final_plot()
```


    
![png](README_files/README_16_0.png)
    


You can run the same command on ```bride_projection_occupations.py``` to generate the projection of occupational words.


```python
import sklearn
print(sklearn.__version__)
```

    1.0.2



```python
!pip install jupyter
```

    Requirement already satisfied: jupyter in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (1.0.0)
    Requirement already satisfied: qtconsole in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from jupyter) (5.3.0)
    Requirement already satisfied: ipywidgets in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from jupyter) (7.6.5)
    Requirement already satisfied: notebook in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from jupyter) (6.4.8)
    Requirement already satisfied: jupyter-console in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from jupyter) (6.4.0)
    Requirement already satisfied: ipykernel in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from jupyter) (6.9.1)
    Requirement already satisfied: nbconvert in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from jupyter) (6.4.4)
    Requirement already satisfied: matplotlib-inline<0.2.0,>=0.1.0 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from ipykernel->jupyter) (0.1.2)
    Requirement already satisfied: nest-asyncio in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from ipykernel->jupyter) (1.5.5)
    Requirement already satisfied: ipython>=7.23.1 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from ipykernel->jupyter) (8.2.0)
    Requirement already satisfied: jupyter-client<8.0 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from ipykernel->jupyter) (6.1.12)
    Requirement already satisfied: appnope in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from ipykernel->jupyter) (0.1.2)
    Requirement already satisfied: debugpy<2.0,>=1.0.0 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from ipykernel->jupyter) (1.5.1)
    Requirement already satisfied: traitlets<6.0,>=5.1.0 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from ipykernel->jupyter) (5.1.1)
    Requirement already satisfied: tornado<7.0,>=4.2 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from ipykernel->jupyter) (6.1)
    Requirement already satisfied: pickleshare in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyter) (0.7.5)
    Requirement already satisfied: pygments>=2.4.0 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyter) (2.11.2)
    Requirement already satisfied: backcall in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyter) (0.2.0)
    Requirement already satisfied: jedi>=0.16 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyter) (0.18.1)
    Requirement already satisfied: pexpect>4.3 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyter) (4.8.0)
    Requirement already satisfied: setuptools>=18.5 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyter) (61.2.0)
    Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyter) (3.0.20)
    Requirement already satisfied: decorator in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyter) (5.1.1)
    Requirement already satisfied: stack-data in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyter) (0.2.0)
    Requirement already satisfied: parso<0.9.0,>=0.8.0 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from jedi>=0.16->ipython>=7.23.1->ipykernel->jupyter) (0.8.3)
    Requirement already satisfied: python-dateutil>=2.1 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from jupyter-client<8.0->ipykernel->jupyter) (2.8.2)
    Requirement already satisfied: pyzmq>=13 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from jupyter-client<8.0->ipykernel->jupyter) (22.3.0)
    Requirement already satisfied: jupyter-core>=4.6.0 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from jupyter-client<8.0->ipykernel->jupyter) (4.9.2)
    Requirement already satisfied: ptyprocess>=0.5 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from pexpect>4.3->ipython>=7.23.1->ipykernel->jupyter) (0.7.0)
    Requirement already satisfied: wcwidth in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython>=7.23.1->ipykernel->jupyter) (0.2.5)
    Requirement already satisfied: six>=1.5 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from python-dateutil>=2.1->jupyter-client<8.0->ipykernel->jupyter) (1.16.0)
    Requirement already satisfied: ipython-genutils~=0.2.0 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from ipywidgets->jupyter) (0.2.0)
    Requirement already satisfied: widgetsnbextension~=3.5.0 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from ipywidgets->jupyter) (3.5.2)
    Requirement already satisfied: jupyterlab-widgets>=1.0.0 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from ipywidgets->jupyter) (1.0.0)
    Requirement already satisfied: nbformat>=4.2.0 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from ipywidgets->jupyter) (5.3.0)
    Requirement already satisfied: fastjsonschema in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from nbformat>=4.2.0->ipywidgets->jupyter) (2.15.1)
    Requirement already satisfied: jsonschema>=2.6 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from nbformat>=4.2.0->ipywidgets->jupyter) (4.4.0)
    Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from jsonschema>=2.6->nbformat>=4.2.0->ipywidgets->jupyter) (0.18.0)
    Requirement already satisfied: attrs>=17.4.0 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from jsonschema>=2.6->nbformat>=4.2.0->ipywidgets->jupyter) (21.4.0)
    Requirement already satisfied: terminado>=0.8.3 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from notebook->jupyter) (0.13.1)
    Requirement already satisfied: argon2-cffi in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from notebook->jupyter) (21.3.0)
    Requirement already satisfied: jinja2 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from notebook->jupyter) (2.11.3)
    Requirement already satisfied: Send2Trash>=1.8.0 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from notebook->jupyter) (1.8.0)
    Requirement already satisfied: prometheus-client in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from notebook->jupyter) (0.13.1)
    Requirement already satisfied: argon2-cffi-bindings in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from argon2-cffi->notebook->jupyter) (21.2.0)
    Requirement already satisfied: cffi>=1.0.1 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from argon2-cffi-bindings->argon2-cffi->notebook->jupyter) (1.15.0)
    Requirement already satisfied: pycparser in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from cffi>=1.0.1->argon2-cffi-bindings->argon2-cffi->notebook->jupyter) (2.21)
    Requirement already satisfied: MarkupSafe>=0.23 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from jinja2->notebook->jupyter) (2.0.1)
    Requirement already satisfied: nbclient<0.6.0,>=0.5.0 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from nbconvert->jupyter) (0.5.13)
    Requirement already satisfied: jupyterlab-pygments in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from nbconvert->jupyter) (0.1.2)
    Requirement already satisfied: beautifulsoup4 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from nbconvert->jupyter) (4.11.1)
    Requirement already satisfied: entrypoints>=0.2.2 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from nbconvert->jupyter) (0.4)
    Requirement already satisfied: mistune<2,>=0.8.1 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from nbconvert->jupyter) (0.8.4)
    Requirement already satisfied: pandocfilters>=1.4.1 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from nbconvert->jupyter) (1.5.0)
    Requirement already satisfied: defusedxml in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from nbconvert->jupyter) (0.7.1)
    Requirement already satisfied: testpath in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from nbconvert->jupyter) (0.5.0)
    Requirement already satisfied: bleach in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from nbconvert->jupyter) (4.1.0)
    Requirement already satisfied: soupsieve>1.2 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from beautifulsoup4->nbconvert->jupyter) (2.3.1)
    Requirement already satisfied: packaging in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from bleach->nbconvert->jupyter) (21.3)
    Requirement already satisfied: webencodings in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from bleach->nbconvert->jupyter) (0.5.1)
    Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from packaging->bleach->nbconvert->jupyter) (3.0.4)
    Requirement already satisfied: qtpy>=2.0.1 in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from qtconsole->jupyter) (2.0.1)
    Requirement already satisfied: executing in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from stack-data->ipython>=7.23.1->ipykernel->jupyter) (0.8.3)
    Requirement already satisfied: pure-eval in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from stack-data->ipython>=7.23.1->ipykernel->jupyter) (0.2.2)
    Requirement already satisfied: asttokens in /Users/pranathiiyer/opt/anaconda3/lib/python3.9/site-packages (from stack-data->ipython>=7.23.1->ipykernel->jupyter) (2.0.5)



```python

```
