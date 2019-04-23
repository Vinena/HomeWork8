'''
郑映慧 1619100019   2019/04/23
function:
    以正弦函数为拟合函数，完成对巨磁实验的实验数据拟合
'''

import numpy as np
import pylab as pl
from scipy.optimize import leastsq

def fx(x,p):
    A,k,theta,b = p
    return b+A*np.sin(2*k*np.pi*(x+theta))

def residuals(p,y,x):
    return y-fx(x,p)


x = np.linspace(0,48*np.pi/180,17)
x1 = np.linspace(0,48*np.pi/180,1000)
y = [48.5,52.6,27.0,-13.8,-38.0,-29.5,-4.9,25.2,48.6,53.2,26.7,-16.1,-39.4,-29.9,-3.5,25.2,48.5]

p0 = [48,2,90,10]
plsq = leastsq(residuals,p0,args=(y,x))
A,k,theta,b = plsq[0]

pl.rcParams['font.family'] = ['simHei']
pl.rcParams['font.sans-serif'] = ['simHei'] # 步骤一（替换sans-serif字体）)
pl.rcParams['axes.unicode_minus'] = False   # 步骤二（解决坐标轴负数的负号显示问题）

pl.plot(x,y,'ro',label = '实验数据')
pl.plot(x1,fx(x1,plsq[0]),'b-',label = '拟合线')
pl.text(0,-20,'y='+'%.2f'%A+'sin(2*pi*'+'%.2f'%k+'*(x+''%.2f'%theta+'))+''%.2f'%b,size=11)
pl.legend()
pl.show()

print('拟合参数：',plsq[0])