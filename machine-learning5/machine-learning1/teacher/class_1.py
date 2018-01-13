# -*- coding:utf-8 -*-  
import math
import sympy
from sympy.abc import x, e
import numpy as np
import scipy.stats as stats
from matplotlib import pyplot as plt

#### 1.  计算sigmod函数的导数 ####
# sigmod 函数表达式
sigmod = 1/( e**-x + 1 )

# 求导
sigmod_diff = sympy.diff( sigmod, x )
sympy.pprint( sigmod_diff )


#### 2. 使用taylor展开式近似计算e^x
func = e**x
# 在原点进行15阶泰勒级数展开, 计算x = 2.5时候的函数值
taylor_series = func.series( x, 0, 16 ).removeO()
value = taylor_series.subs( { e : math.e, x : 2.5 } )
print( value )


#### 3.1 泊松分布, 一分钟内通过某个街道的平均车辆数为3
# 生成lambda=3的泊松分布
parameter = 3
dist = stats.poisson( parameter )

# 一分钟内通过不同车辆数( k <= 20 )的概率质量函数
k_values = np.arange( 20 )
pmf_values = np.array( [ dist.pmf( k )  for k in k_values ] )

plt.bar( k_values, pmf_values )
plt.show()

#### 3.2 高斯分布，生产某种零件所需的平均时间为2分钟，标准差为0.1分钟
# 生成均值为2，标准差为0.1的正态分布
dist = stats.norm( loc = 2, scale = 0.1 )

# 求出概率密度函数
x_values = np.linspace(0, 5, 10000 )
pdf_values = dist.pdf( x_values )
plt.plot( x_values, pdf_values )
plt.show()

















