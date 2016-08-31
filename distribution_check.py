import pandas as pd

from manuf import MacParser

VENDOR_DATA = './data/vendor_data'
WIFI_DATA = './data/t1.csv'
SS_THRES = -100

vendor_checker = MacParser(VENDOR_DATA)

df = pd.read_csv(WIFI_DATA, usecols=[0, 3, 6], header=None)
df.columns = ['timestamp', 'mac_address', 'signal_strength']

print df.head(5)

df = df[df.signal_strength > SS_THRES]

print df.head(5)

df['vendor'] = map(vendor_checker.get_manuf, df['mac_address'].values)
print len(df['mac_address'].unique())

print df.head(5)

import matplotlib.pyplot as plt

s = df.groupby('vendor').size().sort_values(ascending=False)[:6]  # get series
s.name = 'mac distribution'
print s
s.plot.pie(autopct='%.2f', fontsize=10, figsize=(12, 12), legend=True)
plt.show()
