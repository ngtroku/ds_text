# -*- coding: utf-8 -*-
import pandas as pd

data_path = "./"
encoding = 'utf-8'
input = data_path + "/data.csv"
output = data_path + "/Cnvdata.csv"

def read_csv(filename, col=0, moji='', encoding='utf_8_sig'):
    df = pd.read_csv(filename, header=None)
    newsr = []
    for x in df.iloc[:, col]:
        newsr.append(moji.join(x.splitlines()).replace(',', moji))
    df = pd.DataFrame(newsr)
    return df

df = read_csv(input, col=0, moji='', encoding=encoding)
print(df.head())
df.to_csv(output, header=None, index=None, encoding='utf_8_sig')
