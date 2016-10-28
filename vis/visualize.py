
# coding: utf-8

# In[41]:

import pandas as pd
import os

get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')


# ### Raw Visualization of all Data

# In[42]:

for dirpath, dirnames, filenames in os.walk('./../raw/'):
    for filename in filenames:
        
        # Vorerst nur Dresden
        if filename.endswith('.csv') and filename.startswith('Dresden'):

            # Make directory in 'vis' directory, if not exist
            try:
                os.makedirs(dirpath.replace('raw', 'vis'))
            except:
                pass

            # Get Measurement station name and measured emission value
            station, value = filename.split(',')
            value = value[:-4]
            
            # Read raw data
            data = pd.read_csv(dirpath + '/' + filename, skiprows=2,
                   index_col=0, parse_dates=True, dayfirst=True, names=[value])
        
            if data.isnull().all()[0]:
                # Wenn eh keine Daten drin stehen
                continue
            else:
                plotname = dirpath.replace('raw', 'vis') + '/' + filename.replace('.csv', '.png')
                print('Schreibe %s' % plotname)

                # Create Plot
                ax = data.plot(title=station.decode('utf-8'))

                if value=='CO':
                    ax.set_ylabel(u'mg/m³')
                else:
                    ax.set_ylabel(u'µg/m³')

                plt.savefig(plotname, dpi=150)

                # Clean up
                plt.close()
                
            del data

