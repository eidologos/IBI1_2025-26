import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir('Practical10')
dalys_data=pd.read_csv('dalys-rate-from-all-causes.csv')
dalys_data.iloc[0,3]
dalys_data.iloc[0:10,[2,3]]
dalys_data.loc[dalys_data.Entity == "Zimbabwe", "Year"]
recent_data=dalys_data.loc[dalys_data.Year == 2019, ["Entity", "DALYs"]]
uk = dalys_data.loc[dalys_data.Entity == "United Kingdom"]
plt.plot(uk.Year, uk.DALYs, 'b+')
plt.xticks(uk.Year, rotation=-90)
plt.show()