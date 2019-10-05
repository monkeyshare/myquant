import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.stats as stats
from statsmodels.stats import stattools
from datafunc import get_pricing
#交易成本
def perf_impact(leverage,turnover,trading_days,txn_cost_bps):
    '''
    :param leverage: 杠杆
    :param turnover: 周转次数／天
    :param trading_days:交易日数／年
    :param txn_cost_bps:一个基点是0.01%，几个基点
    :return:
    '''
    p = leverage*turnover*trading_days*txn_cost_bps/10000
    return p
'''
# 市场影响、时间风险的交互关系
x=np.linspace(0,1,101)
risk=np.cos(x*np.pi)
impact=np.cos(x*np.pi+np.pi)

fig,ax=plt.subplots()
ax.plot(x,risk)
ax.plot(x,impact)
ax.set_ylabel('交易成本/bps', fontsize=15)
ax.set_xlabel('订单间隔时间',fontsize=15)
ax.set_yticklabels([])
ax.set_xticklabels([])
ax.grid(False)
ax.text(0.09,-0.6,'Timing Tisk',fontsize=15,fontname='serif')
ax.text(0.08,0.6,'Market Impact',fontsize=15,fontname='serif')
plt.title('时间风险vs市场影响对交易成本的效用',fontsize=15)
plt.show()
'''
tickers='FB'
data=get_pricing(tickers,fields='volume')
data.index=pd.to_datetime(data.index)
# data=data.tz_convert('US/Eastern')
print(data[data.index.day=='2019-09-26'])
data=data['volume']
plt.subplot(211)

data[data.index.strftime('%Y-%m-%d') == '2019-09-26']['volume'].plot(title='intraday volume profile')

plt.subplot(212)
(data[data.index.strftime('%Y-%m-%d')=='2019-09-26']['volume'].resample('10T',closed='right').sum()/\
    data[data.index.strftime('%Y-%m-%d')=='2019-09-26']['volume'].sum()).plot()

dat = get_pricing('FB')

def relative_order_size(participation_rate,pct_ADV):
    '''
    相对订单量
    :param participation_rate:
    :param pct_ADV:
    :return:
    '''
