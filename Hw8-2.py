'''
郑映慧 1619100019   2019/04/23
function:
    1、利用curve_fit()函数实现非线性函数的最小二乘法拟合；
    2、完成对阿拉斯加年温度函数的拟合（包括温度最大值与最小值）
notice:
    阿拉斯加年温度变化函数，以年为周期变化，可考虑三角函数拟合
思考题：
    这个拟合有合理之处也有不合理之处：
    合理之处：
        年温度变化曲线具有明显的周期性，
        且从物理上分析，年温度变化主要由于地球的公转造成的，公转为圆周运动，所以利用三角函数拟合具有一定的合理性；
    不合理之处：
        年温度变化受诸多因素影响，不能单一地由时间变化的正弦函数形式表示，需要根据实际的分析、建模，加入更多的影响因子。
'''

import numpy as np
import pylab as pl
from scipy.optimize import curve_fit

month = [i+1 for i in range(12)]
T_max = [17, 19, 21, 28, 33, 38, 37, 37, 31, 23, 19, 18]
T_min = [ -62, -59, -56, -46, -32, -18, -9, -13, -25, -46, -52, -58]

def T_month(month,A,k,theta,b):
    return b+A*np.sin(2*k*np.pi*(month+theta))

p_Tmax = curve_fit(T_month,month,T_max)
p_Tmin = curve_fit(T_month,month,T_min)
A_max,k_max,theta_max,b_max = p_Tmax[0]
A_min,k_min,theta_min,b_min = p_Tmin[0]
# print(A_max,k_max,theta_max,b_max)
print('最高温的时间偏移：',theta_max)
# print(A_min,k_min,theta_min,b_min)
print('最低温的时间偏移：',theta_min)

Max_curve = T_month(month,A_max,k_max,theta_max,b_max)
Min_curve = T_month(month,A_min,k_min,theta_min,b_min)

pl.xlabel('month')
pl.ylabel('T')
pl.xticks(month,month)

pl.plot(month,T_max,'ro')
pl.plot(month,Max_curve,'r-',label='T_max Curve')
pl.plot(month,T_min,'bo')
pl.plot(month,Min_curve,'b-',label='T_min Curve')
pl.legend(loc=1)
pl.title('Annual Temperature curve in Alaska')
pl.show()