import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#成交额计算
num_share=np.array([3000,6000,10000])
prices=np.array([30,31,35])

print(np.dot(num_share,prices))

#分钟级别的愿数据为最后时刻的价格、一分钟内的成交额；
# 一天的加权平均价格可通过分钟级别的数据估算
data = get_pricing('SPY',start_date='2015-6-1',end_date='2015-6-20',frequency='minute')

plt.plot(data['volume'])
plt.ylabel('Volume(USD)')
#volume in every minute of one day
plt.plot(data['volume']['2015-6-4'])
#volume in every minute over the whole period
avg_minute_volume = data.groupby([data.index.hour,data.index.minute]).mean()['volume']
avg_minute_volume.plot()
#volume in every hour of one day

#slippage 滑点

#liquidity 流动性
#大单快无滑点速成交/资产快速变现
#交易规模、市场价格、成交时间、成交价
#单边市场#one-side market
#非持续价格  大宗交易
#交易成本:中间商费用、滑点
#不同的股票流动性差异很大
start_date = '2016-4-1'
end_date = '2016-6-14'
appl_volume_data = get_pricing(start_date=start_date,end_date=end_date,
                               fields='volume')
spy_volume_data = get_pricing('ESM16',end_date=end_date,
                               fields='volume')
appl_volume_data.plot()
spy_volume_data.plot()
plt.legend()
#股票流动性受市值影响；期货流动性更高，不同类型或类别的期货流动性差异很大

#执行算法（高频交易）execution algorithms 拆成小份成交，以减少交易成本

#自动化交易分为交易决策、交易执行。交易决策叫程序交易；交易执行叫算法交易



