#使用机器学习库sklearn求解线性回归

import numpy as np #导入计算包
import matplotlib.pyplot as plt #导入绘图包
#1.加载数据源,并画出散点图
points = np.genfromtxt('data.csv', delimiter=',')

#提取points的两列数据，分别作为x,y
x = points[:,0] #第一列数据
y = points[:,1] #第2列数据

#用plt画出散点图
plt.scatter(x,y)
plt.show()

#2.定义损失函数,损失函数是系数的函数
def cost_function(w, b, points):
    total_const = 0 #初始化损失函数
    m = len(points) #数据个数
    #逐点计算平方误差，然后求平均数
    for i in range(m):
        x = points[i,0] #第i行，第1列
        y = points[i,1] #第i行，第2列
        total_const += (y - w * x - b) ** 2
    return total_const / m

from sklearn.linear_model import LinearRegression
lr = LinearRegression()

x_new = x.reshape(-1,1) #改造成n行1列的二维数组
y_new = y.reshape(-1,1)
lr.fit(x_new,y_new) #拟合

#从训练好的模型中提取系截距
w = lr.coef_[0][0]
b = lr.intercept_[0]

cost = cost_function(w,b,points)

print("参数w = ", w)
print("参数b = ", b)
print("损失函数 = ", cost)

plt.scatter(x,y)
pred_y = w * x + b
plt.plot(x, pred_y, c = 'r')
plt.show()



