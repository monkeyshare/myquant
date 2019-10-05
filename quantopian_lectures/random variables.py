import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.stats as stats
from statsmodels.stats import stattools
# from __future__ import division

class DiscreteRandomVariable:
    def __init__(self,a=0,b=1):
        self.VariableType = ""
        self.low = a
        self.high = b
    def draw(self,numberofsamples):
        samples = np.random.random_integers(self.low,self.high,numberofsamples)
        return samples

# 均匀分布
DieRolls = DiscreteRandomVariable(1,6)
plt.hist(DieRolls.draw(1000),bins=[1,2,3,4,5,6,7],align='mid')
plt.xlabel('Value')
plt.ylabel('Occurences')
plt.legend('Diew Rolls')
plt.show()
# 二项式分布
class BinominalRandomVariable:
    def __init__(self,numberoftrials=10,probabilityofsuccess=0.5):
        self.VariablesType = 'Binominal'
        self.numberoftrials = numberoftrials
        self.probabilityofsuccess = probabilityofsuccess
        return
    def draw(self,numberofsamples):
        samples = np.random.binomial(self.numberoftrials,self.probabilityofsuccess,numberofsamples)
        return samples
binomials = BinominalRandomVariable(10,0.25)
plt.hist(binomials.draw(2000),bins=range(1,7),align='mid')
plt.xlabel('Value')
plt.ylabel('binominal')
plt.show()

# 连续随机变量的概率密度函数PDF
# 均匀分布
class ContinuousRandomVariable:
    def __init__(self,a=0,b=1):
        self.variablesType=""
        self.low = a
        self.b = b
    def draw(self,numberofsamples):
        samples = np.random.uniform(self.low,self.high,numberofsamples)
        return samples
continuous = ContinuousRandomVariable(0,1)
a=0
b=8
x=np.linspace(a,b,100)
print(x)
y=[(i-a)/(b-a) for i in x] #累积概率密度函数
plt.plot(x,y)
plt.xlabel('Value')
plt.ylabel('Probability')
plt.show()
# 正态分布
class NormalRandomVariable(ContinuousRandomVariable):
    def __init__(self,mean=0,variance=1):
        ContinuousRandomVariable.__init__(self)
        self.variablesType = "Normal"
        self.mean=mean
        self.standardDeviation = np.sqrt(variance)
        return
    def draw(self,numberofsamples):
        samples=np.random.normal(self.mean,self.standardDeviation,size=numberofsamples)
        return samples
mu = 0
sigma = 1
x=np.linspace(-8,8,200)
y=(1/(sigma*np.sqrt(2*3.1415926)))*np.exp(-(x-mu)*(x-mu)/2*sigma*sigma)
plt.plot(x,y)
plt.show()

# 泊努力分布的均值为np，标准差为np（1-p），可标准化
n=50
p=0.25
X=BinominalRandomVariable(n,p)
X_samples=X.draw(10000)
Z_samples=(X_samples-n*p)/np.sqrt(n*p*(1-p))
plt.hist(X_samples,bins=20)
plt.show()
# 模拟资产趋势
initial=1000
X=NormalRandomVariable(0,1)
samples=X.draw(200)
Y=pd.Series(np.cumsum(samples)+initial,name='Y')
Y.plot()
plt.show()
#模拟资产组合的曲线
start='2015-01-01'
end='2016-01-01'
prices=get_pricing('TSLA',fields=['price'],start_date=start,end_date=end)

returns = prices.pct_change()[1:]

cutoff=0.01

_,p_value,skewness,kurtosis = stattools.jarque_bera(returns)
print(p_value,skewness,kurtosis)
plt.hist(returns.price,bins=20)
plt.ylabel('Occurrences')
plt.show()

sample_mean=np.mean(returns.price)
sample_std=np.std(returns.price)

x=np.linspace(-(sample_mean+4*sample_std),sample_mean+4*sample_std,200)
sample_distribution=((1/np.sqrt(sample_std * sample_std * 2 * np.pi)) *
                       np.exp(-(x - sample_mean)*(x - sample_mean) / (2 * sample_std * sample_std)))
plt.hist(returns.price,bins=20,normed=True)
plt.plot(x,sample_distribution)
plt.xlabel('Vlue')
plt.ylabel('Occurrences')
plt.show()



