import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('thailand_cpi_2017.csv', index_col=0)
df = df.sort_index()
filtered = df.index >= 2000

fullChart = df.loc[:, ['Core CPI Delta', 'Headline CPI Delta']]
ax = fullChart.plot(title='Thailand CPI')
ax.set(xlabel='Year',ylabel='Percent')
ax.axvline(x=2000, color='red', linestyle='--')

plt.show()
plt.close()

core_cpi_avg = df[filtered]['Core CPI Delta'].mean()
headline_cpi_avg = df[filtered]['Headline CPI Delta'].mean()

chart = df[filtered].loc[:, ['Core CPI Delta', 'Headline CPI Delta']]
ax1, ax2 = chart.plot(subplots=True)

ax1.set(title="Thailand Core CPI. x̄ = {0:.2f}".format(core_cpi_avg) )
ax1.axhline(y=core_cpi_avg, color='red', linestyle='--')

ax2.set(title="Thailand Headline CPI. x̄ = {0:.2f}".format(headline_cpi_avg) )
ax2.axhline(y=headline_cpi_avg, color='red', linestyle='--')

plt.subplots_adjust(hspace=0.4)
plt.show()