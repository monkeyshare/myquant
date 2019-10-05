import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#设置随即种子
np.random.seed(123)

normal = np.random.randn(500)

#画直方图
plt.hist([normal[:10],normal[10:100],normal[100:250],normal],
         normed=1,histtype='bar',stacked=True)
plt.ylabel('Frequency')
plt.xlabel('Value')
plt.show()

#画双峰分布图（0值两边都是正态分布）
def bimodal(n):
    X = np.zeros((n))
    for i in range(n):
        if np.random.binomial(1,0.5)==0:
            X[i]=np.random.normal(-5,1)
        else:
            X[i]=np.random.normal(5,1)
    return X

X=bimodal(1000)
plt.hist(X,bins=50)
plt.ylabel('Frequency')
plt.xlabel('Value')
print('mean:',np.mean(X))
print('standard deviation',np.std(X))
plt.show()
from statsmodels.stats.stattools import jarque_bera
print('P of jarque_bera: ',jarque_bera(X))
X=np.random.normal(np.mean(X),np.std(X),1000)
plt.hist(X,bins=50)
plt.show()

#滚动夏普比例
def sharpe_ratio(asset,riskfree):
    return np.mean(asset-riskfree)/np.std(asset-riskfree)
start = '2012-01-01'
end = '2015-01-01'

treasury_ret = get_pricing('BIL',fields='price',start_date=start,
                           end_date=end)
pricing= get_pricing('AMZN',fields='price',start_date=start,
                           end_date=end)
returns = pricing.pct_change()[1:]
#计算滚动夏普比例
running_sharpe = [sharpe_ratio(returns[i-90:i],treasury_ret[i-90:i])
                  for i in range(90,len(returns))]
_,ax1 = plt.subplots()
ax1.plot(range(90,len(returns)-100),running_sharpe[:-100])
ticks = ax1.get_xticks()
ax1.set_xticklabels([pricing.index[i].date() for i in ticks[:-1]])
plt.xlabel('Date')
plt.ylabel('sharpe ratio')

#计算并画出布林带（移动均值－＋标准差）

