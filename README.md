The code and data in this repository are a preliminary step towards the final objective of understanding the structure, trends, relevance,and success of matrimonial advertisements in the Indian context, throught this project. While this repository currently contains advertisements for prospective brides and grooms from the year 2001 to 2009, and 2014, the final project will also have data for 2010, 2011, 2012, and 2013.These years are slightly difficult to scrape owing to changes in the website. The data for grooms can be found under ```grooms_data``` in the folder ```data```, and the data for brides can be found under ```brides_data``` in the folder ```data```.

The code is written in Python 3.9.10 and all of its dependencies can be installed by running the following in the terminal (with the requirements.txt file included in this repository):

                         pip install -r requirements.txt
                         
Then, you can import the analysis and plot_num_ads module located in this repository to reproduce the analysis in the project that this code supplements (in a Jupyter Notebook, like README.ipynb in this repository, or in any other Python script):


```python
import plot_num_ads
```

This module primarily plots the number of advertisements for brides and grooms across all years. This can help us understand how these ads and their volumnes have changed with respect to brides and grooms in the context of newspapers. Once you import the above module, you can use its plot function to reproduce the figure comparing number of advertisements across years.


```python
plot_num_ads.plot_fig()
```


    
![png](README_files/README_3_0.png)
    


### Findings:
This shows that the number of advertisements for grooms and brides move in the same direction (this could also be a function of problems in scraping). Moreover, it shows that the number of advertisements for grooms peaked heavily after 2006. While the time would have to be examined (as to why this is observed only after 2006 and not before), there is anecdotal evidence that there has traditionally been more societal pressure for women to get married, and this finding supports this at a very rudimentary level. Of course, a more thorough qualitative analysis is required to make any claim.

You can then import the analysis module to delve deeper into some of the actual analysis of the project. This module produces analysis for a single data file. Hence, you could input any data file from the ```data``` folder using the commands below. The below functions are performed on the advertisements seeking brides in the year 2008. A similar analysis can be repreduced for all years.


```python
import analysis
```


```python
data = analysis.word_to_count('brides-wanted_2008.csv')
analysis.counts_data(data)

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>word</th>
      <th>count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>nurse/doctor</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>mba</td>
      <td>2546</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ma</td>
      <td>255</td>
    </tr>
    <tr>
      <th>3</th>
      <td>kashyap</td>
      <td>300</td>
    </tr>
    <tr>
      <th>4</th>
      <td>rajput</td>
      <td>1161</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>9140</th>
      <td>processing</td>
      <td>1</td>
    </tr>
    <tr>
      <th>9141</th>
      <td>0030</td>
      <td>1</td>
    </tr>
    <tr>
      <th>9142</th>
      <td>accoutancy</td>
      <td>1</td>
    </tr>
    <tr>
      <th>9143</th>
      <td>11:50</td>
      <td>1</td>
    </tr>
    <tr>
      <th>9144</th>
      <td>jagdeepkumar</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>9145 rows × 2 columns</p>
</div>



### Findings
While a lot of junk words appear, upon sorting this table we observe that words such as mba, ma, kashyap (a community), rajput (a community) appear several times. This finding is an indication of how these advertisements can be explained along dimensions of occupation, caste, and gender.

You can also run the below commands to reproduce the other plots in the project.



```python
analysis.final_func('brides-wanted_2008.csv')
```


    
![png](README_files/README_10_0.png)
    



    
![png](README_files/README_10_1.png)
    


The above commands can easily be run for any of the files from the data folder to reproduce other analyses.


### Findings
These plots are very informative. They tell us that Sikh, which is a religious community in northern india, is the most frequently used proper noun, and mba ia the most used three letter word. This gives another strong signal towards the heavy use of caste and occupation in these ads. Moreover, it would be interesting to explore why 'usa' is accuring almost as frequently as india.


```python
! pip install nbconvert
```

    Requirement already satisfied: nbconvert in /Users/pranathiiyer/opt/anaconda3/lib/python3.8/site-packages (6.0.7)
    Requirement already satisfied: traitlets>=4.2 in /Users/pranathiiyer/opt/anaconda3/lib/python3.8/site-packages (from nbconvert) (5.0.5)
    Requirement already satisfied: bleach in /Users/pranathiiyer/opt/anaconda3/lib/python3.8/site-packages (from nbconvert) (3.3.0)
    Requirement already satisfied: nbformat>=4.4 in /Users/pranathiiyer/opt/anaconda3/lib/python3.8/site-packages (from nbconvert) (5.1.3)
    Requirement already satisfied: defusedxml in /Users/pranathiiyer/opt/anaconda3/lib/python3.8/site-packages (from nbconvert) (0.7.1)
    Requirement already satisfied: nbclient<0.6.0,>=0.5.0 in /Users/pranathiiyer/opt/anaconda3/lib/python3.8/site-packages (from nbconvert) (0.5.3)
    Requirement already satisfied: pandocfilters>=1.4.1 in /Users/pranathiiyer/opt/anaconda3/lib/python3.8/site-packages (from nbconvert) (1.4.3)
    Requirement already satisfied: entrypoints>=0.2.2 in /Users/pranathiiyer/opt/anaconda3/lib/python3.8/site-packages (from nbconvert) (0.3)
    Requirement already satisfied: mistune<2,>=0.8.1 in /Users/pranathiiyer/opt/anaconda3/lib/python3.8/site-packages (from nbconvert) (0.8.4)
    Requirement already satisfied: pygments>=2.4.1 in /Users/pranathiiyer/opt/anaconda3/lib/python3.8/site-packages (from nbconvert) (2.8.1)
    Requirement already satisfied: jinja2>=2.4 in /Users/pranathiiyer/opt/anaconda3/lib/python3.8/site-packages (from nbconvert) (2.11.3)
    Requirement already satisfied: jupyterlab-pygments in /Users/pranathiiyer/opt/anaconda3/lib/python3.8/site-packages (from nbconvert) (0.1.2)
    Requirement already satisfied: jupyter-core in /Users/pranathiiyer/opt/anaconda3/lib/python3.8/site-packages (from nbconvert) (4.7.1)
    Requirement already satisfied: testpath in /Users/pranathiiyer/opt/anaconda3/lib/python3.8/site-packages (from nbconvert) (0.4.4)
    Requirement already satisfied: MarkupSafe>=0.23 in /Users/pranathiiyer/opt/anaconda3/lib/python3.8/site-packages (from jinja2>=2.4->nbconvert) (1.1.1)
    Requirement already satisfied: async-generator in /Users/pranathiiyer/opt/anaconda3/lib/python3.8/site-packages (from nbclient<0.6.0,>=0.5.0->nbconvert) (1.10)
    Requirement already satisfied: nest-asyncio in /Users/pranathiiyer/opt/anaconda3/lib/python3.8/site-packages (from nbclient<0.6.0,>=0.5.0->nbconvert) (1.5.1)
    Requirement already satisfied: jupyter-client>=6.1.5 in /Users/pranathiiyer/opt/anaconda3/lib/python3.8/site-packages (from nbclient<0.6.0,>=0.5.0->nbconvert) (6.1.12)
    Requirement already satisfied: ipython-genutils in /Users/pranathiiyer/opt/anaconda3/lib/python3.8/site-packages (from nbformat>=4.4->nbconvert) (0.2.0)
    Requirement already satisfied: jsonschema!=2.5.0,>=2.4 in /Users/pranathiiyer/opt/anaconda3/lib/python3.8/site-packages (from nbformat>=4.4->nbconvert) (3.2.0)
    Requirement already satisfied: six>=1.9.0 in /Users/pranathiiyer/opt/anaconda3/lib/python3.8/site-packages (from bleach->nbconvert) (1.12.0)
    Requirement already satisfied: packaging in /Users/pranathiiyer/opt/anaconda3/lib/python3.8/site-packages (from bleach->nbconvert) (20.9)
    Requirement already satisfied: webencodings in /Users/pranathiiyer/opt/anaconda3/lib/python3.8/site-packages (from bleach->nbconvert) (0.5.1)
    Requirement already satisfied: attrs>=17.4.0 in /Users/pranathiiyer/opt/anaconda3/lib/python3.8/site-packages (from jsonschema!=2.5.0,>=2.4->nbformat>=4.4->nbconvert) (20.3.0)
    Requirement already satisfied: pyrsistent>=0.14.0 in /Users/pranathiiyer/opt/anaconda3/lib/python3.8/site-packages (from jsonschema!=2.5.0,>=2.4->nbformat>=4.4->nbconvert) (0.17.3)
    Requirement already satisfied: setuptools in /Users/pranathiiyer/opt/anaconda3/lib/python3.8/site-packages (from jsonschema!=2.5.0,>=2.4->nbformat>=4.4->nbconvert) (52.0.0.post20210125)
    Requirement already satisfied: tornado>=4.1 in /Users/pranathiiyer/opt/anaconda3/lib/python3.8/site-packages (from jupyter-client>=6.1.5->nbclient<0.6.0,>=0.5.0->nbconvert) (6.1)
    Requirement already satisfied: python-dateutil>=2.1 in /Users/pranathiiyer/opt/anaconda3/lib/python3.8/site-packages (from jupyter-client>=6.1.5->nbclient<0.6.0,>=0.5.0->nbconvert) (2.8.1)
    Requirement already satisfied: pyzmq>=13 in /Users/pranathiiyer/opt/anaconda3/lib/python3.8/site-packages (from jupyter-client>=6.1.5->nbclient<0.6.0,>=0.5.0->nbconvert) (20.0.0)
    Requirement already satisfied: pyparsing>=2.0.2 in /Users/pranathiiyer/opt/anaconda3/lib/python3.8/site-packages (from packaging->bleach->nbconvert) (2.4.7)
    [33mWARNING: You are using pip version 22.0.3; however, version 22.0.4 is available.
    You should consider upgrading via the '/Users/pranathiiyer/opt/anaconda3/bin/python -m pip install --upgrade pip' command.[0m[33m
    [0m


```python
!jupyter nbconvert --to md README.ipynb
```

    Traceback (most recent call last):
      File "/Users/pranathiiyer/opt/anaconda3/bin/jupyter-nbconvert", line 11, in <module>
        sys.exit(main())
      File "/Users/pranathiiyer/opt/anaconda3/lib/python3.8/site-packages/jupyter_core/application.py", line 254, in launch_instance
        return super(JupyterApp, cls).launch_instance(argv=argv, **kwargs)
      File "/Users/pranathiiyer/opt/anaconda3/lib/python3.8/site-packages/traitlets/config/application.py", line 845, in launch_instance
        app.start()
      File "/Users/pranathiiyer/opt/anaconda3/lib/python3.8/site-packages/nbconvert/nbconvertapp.py", line 350, in start
        self.convert_notebooks()
      File "/Users/pranathiiyer/opt/anaconda3/lib/python3.8/site-packages/nbconvert/nbconvertapp.py", line 518, in convert_notebooks
        cls = get_exporter(self.export_format)
      File "/Users/pranathiiyer/opt/anaconda3/lib/python3.8/site-packages/nbconvert/exporters/base.py", line 127, in get_exporter
        raise ExporterNameError('Unknown exporter "%s", did you mean one of: %s?'
    nbconvert.exporters.base.ExporterNameError: Unknown exporter "md", did you mean one of: asciidoc, custom, html, latex, markdown, notebook, pdf, python, rst, script, slides, webpdf?



```python

```
