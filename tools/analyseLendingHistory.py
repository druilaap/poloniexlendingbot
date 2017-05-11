import pandas as pd
import sys

curs = ['BTC', 'BTS', 'CLAM', 'DASH', 'DOGE', 'ETH', 'FCT', 'LTC', 'MAID', 'STR', 'XMR', 'XRP']
frame_dict = {}

lendingFile = sys.argv[1]

df = pd.read_csv(lendingFile,
                 usecols=['Currency', 'Rate', 'Earned', 'Close', 'Open'],
                 index_col='Open',
                 parse_dates=['Open', 'Close'],
                 infer_datetime_format=True)

for cur in curs:
    frame_dict[cur] = df[df.Currency == cur]
    print("Summary for {0}".format(cur))
    print("Total earned : {0}".format(frame_dict[cur].Earned.sum()))
    print("Best rate    : {0}%".format(frame_dict[cur].Rate.max() * 100))
    print("Average rate : {0:.6f}%".format(frame_dict[cur].Rate.mean() * 100))
