import requests
import pandas
import io
import datetime
import os
import time
# https://www.alphavantage.co/documentation/
def dataframeFromUrl(url):
	dataString = requests.get(url).content
	parsedResult = pandas.read_csv(io.StringIO(dataString.decode('utf-8')), index_col=0)
	return parsedResult

def get_pricing(ticker,fields='',frequency='1min',
                start_date='2019-09-28',end_date='2019-10-02'):
    '''
    :param ticker:
    :param fields:
    :param frequency: 1min/5min/15min/30min/60min DAILY WEEKLY MONTHLY
    :param start_date:
    :param end_date:
    :return:
    '''
    url='https://www.alphavantage.co/query?apikey=NGV2US07ZZQULVGP&function=TIME_SERIES_INTRADAY&symbol={}&' \
        'interval={}&outputsize=full&datatype=csv'.format(ticker,frequency)
    if 'min' not in frequency:
        url='https://www.alphavantage.co/query?\
        function=TIME_SERIES_{}&\
        symbol={}&outputsize=full&\
        apikey=NGV2US07ZZQULVGP&datatype=csv'.format(frequency,ticker)
    print(url)
    intraday = dataframeFromUrl(url)
    # if fields:
    #     intraday=intraday[fields]

    # intraday = intraday[intraday.index>start_date]
    intraday.sort_index(inplace=True)
    return intraday
if __name__=='__main__':
    print(get_pricing('AAPL').head())