# -*- coding: utf-8 -*-
"""View data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eBKc-zMKtoIt3gzxbi8Rhdhas-V9x7oq
"""

import pymongo
from pymongo import MongoClient
import pprint
import datetime
from datetime import datetime
import time

uri = "mongodb://redwan1006066:14243444redwan@ds125602.mlab.com:25602/redwan-uga-spr2019-data"
client = MongoClient(uri)
db = client['redwan-uga-spr2019-data']
col = db['envdata']
print(col.count_documents({}))

datetime_obj = datetime.strptime(col.find_one()['date']+' '+col.find_one()['time'], "%d-%m-%Y %H-%M-%S")
print(datetime_obj)

datetimes = []
temps = []
hums = []
for docs in col.find({}):
  datetime_obj = datetime.strptime(docs['date']+' '+docs['time'], "%d-%m-%Y %H-%M-%S")
  datetimes.append(datetime_obj)
  temps.append(docs['temperature'])
  hums.append(docs['humidity'])

def enable_plotly_in_cell():
  import IPython
  from plotly.offline import init_notebook_mode
  display(IPython.core.display.HTML('''
        <script src="/static/components/requirejs/require.js"></script>
  '''))
  init_notebook_mode(connected=False)

import plotly
import plotly.plotly as py
import plotly.graph_objs as go

enable_plotly_in_cell()

plotly.tools.set_credentials_file(username='RedwanIslam', api_key='WyPvjm7cSJE2knxgE3Oh')

data1 = go.Scatter(x=datetimes, y=hums)
data2 = go.Scatter(x=datetimes, y=temps)
py.iplot([data1, data2])