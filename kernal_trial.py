#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
df = pd.read_csv("/content/Twitter_volume_AAPL.csv", header=None, skiprows=6, parse_dates=[0], names=['period', 'value'])
df.value.astype(int, copy=False);


# In[ ]:


import warnings
warnings.filterwarnings('ignore')


# In[ ]:


import pandas as pd
df = pd.read_csv("/content/Twitter_volume_AAPL.csv", header=None, skiprows=6, parse_dates=[0], names=['period', 'value'])
df.value.astype(int, copy=False);


# In[ ]:


max_date = df.period.max()
min_date = df.period.min()


# In[ ]:


num_of_actual_points = df.index.shape[0]
num_of_expected_points = (max_date.year - min_date.year) * 12 + max_date.month - min_date.month + 1


# In[ ]:


print("Date range: {} - {}".format(min_date.strftime("%d.%m.%Y"), max_date.strftime("%d.%m.%Y")))
print("Number of data points: {} of expected {}".format(num_of_actual_points, num_of_expected_points))


# In[ ]:


plt.savefig('intro-visualization.png')


# In[ ]:


from statsmodels.tsa.seasonal import seasonal_decompose


# In[ ]:


decompfreq = 12  # 12 months seasonality
model = 'additive'


# In[ ]:


decomposition = seasonal_decompose(
    df.set_index("period").value.interpolate("linear"),
    freq=decompfreq,
    model=model)


# In[ ]:


trend = decomposition.trend
seasonal = decomposition.seasonal 
residual = decomposition.resid


# In[ ]:


fig, ax = plt.subplots(figsize=(18,6))
df.plot(x="period", y="value", ax=ax, label="observed", c='lightgrey')
trend.plot(ax=ax, label="trend")
plt.legend(loc='upper left')


# In[ ]:


plt.savefig('intro-trend.png')


# In[ ]:


fig, ax = plt.subplots(figsize=(15,4))
seasonal.plot(ax=ax, label="seasonality")
plt.legend(loc='bottom left')


# In[ ]:


fig, ax = plt.subplots(figsize=(18,4))
residual.plot(ax=ax, legend="seasonality")
plt.legend(loc='upper left')
res

