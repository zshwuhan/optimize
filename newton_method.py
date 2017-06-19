#encoding: utf8

import numpy as np
import pdb

'''
牛顿法、拟牛顿法用在非线性优化上
不过因为牛顿法、拟牛顿法在非线性优化上用得比较广，单独写一个文件
包括:
'''

def f4():
    # f = 4*x1**2 + 2*x1*x2 + 2 * x2**2 + x1 + x2
    # normal: f = c + b.T * x + 1/2 * x.T * A * x
    # dst_x = np.array([-1.0/14, -3.0/14])
    c = 2
    b = np.matrix('1;1')
    A = np.matrix('8,2;2,4') 

    return c,b,A

'''
牛顿法. 要求f有二阶导数
牛顿法非区间搜索法。只要给到起始点，就可以下降(对凸函数是这样子)

算法大致如下：
对原函数二阶tayler展开，然后用二次多项式近似：
f(x) = f(x0) + f'(x)(x - x0) + 1/2(x-x0).T * H * (x - x0) + O((x-x0).T(x-x0))
f_sim(x) = f(x0) + f'(x)(x - x0) + 1/2(x-x0).T * H * (x - x0)
f_sim'(x) = f'(x) + H(x-x0) = 0
x = x0 - H.inv * f'(x)

dk = -H.inv * f', 称为牛顿方向

牛顿法求解，计算量比较大，还要求H正定
H为海森矩阵, 要求是非奇异的

阻尼牛顿法
 由于牛顿法并不能保证收敛.于是改为沿dk方向进行一维搜索求，xk+1 = xk + lambk * dk, 

实际上并不直接求H.inv, 而改为解线性方程：
H*dk = f'

'''
def newton_search_for_quad(f, x0, espilon):
    c,b,A = f()
    x_n_1 = x0
    x = x0
    f_n_1 = c + b.T * x + 1/2.0 * x.T * A * x 

    while True:
        H_f = A
        deriv_f = A * x_n_1 + b

        x_n = x_n_1 - np.dot(np.linalg.inv(H_f), deriv_f)
        x = x_n
        f_n = c + b.T * x + 1/2.0 * x.T * A * x 

        if np.abs(f_n - f_n_1) < espilon:
            return x_n, f_n

        x_n_1 = x_n
        f_n_1 = f_n

    return None

'''
拟牛顿条件
如上式：
~=: sim_eq
f(x)在x_k+1点处理展开
f(x) ~= f(x_k1) + f'(x_k1)(x-xk) + 1/2*(x_k1-x).T * H * (x_k1-x)
两边同时作用一个梯度算子，则：
f'(x) ~= f'(x_k1) + H(x_k1)*(x_k1 - x)
记 x=x_k
   f'(x_k) ~= f'(x_k1) + H(x_k1) * (x_k1 - x_k)
   f'(x_k1) - f'(x_k) ~= H(x_k1) * (x_k1 - x_k)

记 B=H, D=H.inv, y_k = f'(x_k1) - f'(x_k), s_k = (x_k1 - x_k),则
y_k ~= H*s_k 
s_k ~= H.inv * y_k
上述即为拟牛顿条件，
对 H(k+1)或H(k+1).inv做近似  
y_k = B(k+1)*s_k
或：
s_k = D(k+1) * y_k

即用梯度近似计算H或H的逆
'''

def DFP(f, f_deriv, x0, espilon):
    return None

def BFGS(f, f_deriv, x0, espilon):
    return None

def L_BFGS(f, f_deriv, x0, espilon):
    return None

if __name__ == "__main__":
    x0 = np.matrix('0.0;0.0') 
    rst = newton_search_for_quad(f4, x0, 0.01)
    dst_x = np.array([-1.0/14, -3.0/14])
    
    print "expect x:0.63"
    print "nr: dst:", dst_x
    print "nr: rst:", rst 