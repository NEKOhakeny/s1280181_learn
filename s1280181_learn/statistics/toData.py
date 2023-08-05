import pandas as pd
import csv
# csvファイルを読み込んでDataFrameに変換
# タブ区切りであることを指定
df = pd.read_csv('itemFrequency.csv', sep='\t')

# 一つ目の属性から',,'を空文字に置き換え
# 正規表現による置換を指定
df.iloc[:,0] = df.iloc[:,0].replace(',{2,}','', regex=True)
df = df[~df.iloc[:, 0].str.contains(',')]
# DataFrameをcsvファイルに書き出し
# タブ区切りであることを指定
# 行番号や列名が出力されないように指定
df.to_csv('output.csv', sep='\t', index=False, header=False)