# -*- coding: utf-8 -*-
import pandas as pd
from manuf import MacParser

VENDOR_DATA = './app/static/wifi_data/vendor_data'
WIFI_DATA = './app/static/wifi_data/t1.csv'
SS_THRES = -100

def get_wifi_data():
    vendor_checker = MacParser(VENDOR_DATA)
    df = pd.read_csv(WIFI_DATA, usecols=[0, 3, 6], header=None)
    df.columns = ['timestamp', 'mac_address', 'signal_strength']
    df = df[df.signal_strength > SS_THRES]
    df['vendor'] = map(vendor_checker.get_manuf, df['mac_address'].values)
    s = df.groupby('vendor').size().sort_values(ascending=False)[:6]  # get series
    return list(s.index),list(s.values)

