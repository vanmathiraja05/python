#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')


df.plot(kind = 'hist', x = 'Duration', y = 'Calories')
print(df.head())
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
print("17############################################################################################\n")
sys.stdout.flush()
print("18")
