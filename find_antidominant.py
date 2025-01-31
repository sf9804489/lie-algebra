import numpy as np
"""find_antidominant为例外型李代数的基本权坐标下的整权找出对应的反支配整权.
方法参考自Zhanqiang Bai,Fan Gao,Xun xie,And Yutong Wang,Gelfand_kirillov Dimension and Annihilator Varieties of Highest Moudules of Exceptional Lie Algebras
的lemma 3.1"""
"""如果出错，回来检查find_antidominant函数的basic_roots_by_fundamental_weights部份"""
"""find_antidominant函数的basic_roots_by_fundamental_weights部份现在只验证了f4与g2的，2025.1.10;e6,e7,e8,2025.1.19"""

def Judge_antidominant(l_by_fundamental_weights,numsofroots):
    judge=1
    for i in range(numsofroots):
        if l_by_fundamental_weights[i]>0:
            judge=0
            break
    return judge#返回1表示是反支配的，返回0表示不是反支配的
def find_max_and_maxidex(l_by_fundamental_weights,numsofroots):
    max=l_by_fundamental_weights[0]
    max_idex=0
    for i in range(numsofroots):
        if l_by_fundamental_weights[i]>=max:
            max=l_by_fundamental_weights[i]
            max_idex=i
    return max,max_idex
def find_antidominant(l,typeoflie,numsofroots):
    print("等待降权的是：" + str(l))
    if typeoflie == 'F':
        basic_roots_by_fundamental_weights = np.array([[2, -1, 0, 0], [-1, 2, -1, 0], [0, -2, 2, -1], [0, 0, -1, 2]])
    elif typeoflie == 'G':
        basic_roots_by_fundamental_weights = np.array([[2, -1], [-3,2]])
    elif typeoflie == 'E'and numsofroots == 6:
        basic_roots_by_fundamental_weights = np.array([[2,0,-1,0,0,0],[0,2,0,-1,0,0],[-1,0,2,-1,0,0],[0,-1,-1,2,-1,0],[0,0,0,-1,2,-1],[0,0,0,0,-1,2]])
    elif typeoflie == 'E'and numsofroots == 7:
        basic_roots_by_fundamental_weights = np.array([[2,0,-1,0,0,0,0],[0,2,0,-1,0,0,0],[-1,0,2,-1,0,0,0],[0,-1,-1,2,-1,0,0],[0,0,0,-1,2,-1,0],[0,0,0,0,-1,2,-1],[0,0,0,0,0,-1,2]])
    elif typeoflie == 'E' and numsofroots == 8:
        basic_roots_by_fundamental_weights = np.array([[2, 0, -1, 0, 0, 0, 0,0], [0, 2, 0, -1, 0,0, 0, 0], [-1, 0, 2, -1, 0, 0,0, 0], [0, -1, -1, 2, -1, 0,0, 0],
             [0, 0,0, -1, 2, -1, 0,0], [0, 0, 0,0, -1, 2, -1, 0], [0, 0, 0, 0, 0,-1, 2, -1], [0, 0,0, 0, 0, 0, -1, 2]])

    judge = Judge_antidominant(l, numsofroots)
    lenthofw = 0
    w = []
    while judge != 1:
        max, maxidex = find_max_and_maxidex(l, numsofroots)
        l = l - max * basic_roots_by_fundamental_weights[maxidex][:]
        lenthofw = lenthofw + 1
        newW = [0] * (lenthofw)
        newW[:len(w)] = w
        newW[lenthofw - 1] = maxidex
        w = newW  # 给w在右边增加一个长度，加入新的基础反射s_{maxidex+1}
        judge = Judge_antidominant(l, numsofroots)
    print("对应的反支配权：" + str(l))
    print("对应的反射（左作用，作用的先后顺序：从左到右）：" + str(w))
    print("对应的反射（左作用，作用的先后顺序：从右到左）：" + str(w[::-1]))
    print("对应的反射的长度：" + str(lenthofw))
    return w[::-1]

# #示例：
#
# z=-1
# r=np.array([1,1,1,1])
# l=np.array([1,0,1,1])#基本权下的表示
# print("选定的z的值为:"+str(z))
# l=z*l+r
# find_antidominant(l,'F',4)
#
#
#找basic_roots_by_fundamental_weights
# from BasisTransform import *
# g2=np.array([[1,-1,0],[-2,1,1]])
# e6=np.array([[1/2,-1/2,-1/2,-1/2,-1/2,-1/2,-1/2,1/2],
#              [1,1,0,0,0,0,0,0],
#              [-1,1,0,0,0,0,0,0],
#              [0,-1,1,0,0,0,0,0],
#              [0,0,-1,1,0,0,0,0],
#              [0,0,0,-1,1,0,0,0]])
#
# e7=np.array([[1/2,-1/2,-1/2,-1/2,-1/2,-1/2,-1/2,1/2],
#              [1,1,0,0,0,0,0,0],
#              [-1,1,0,0,0,0,0,0],
#              [0,-1,1,0,0,0,0,0],
#              [0,0,-1,1,0,0,0,0],
#              [0,0,0,-1,1,0,0,0],
#              [0,0,0,0,-1,1,0,0]])
# e8=np.array([[1/2,-1/2,-1/2,-1/2,-1/2,-1/2,-1/2,1/2],
#              [1,1,0,0,0,0,0,0],
#              [-1,1,0,0,0,0,0,0],
#              [0,-1,1,0,0,0,0,0],
#              [0,0,-1,1,0,0,0,0],
#              [0,0,0,-1,1,0,0,0],
#              [0,0,0,0,-1,1,0,0],
#              [0,0,0,0,0,-1,1,0]])
# lie=e7
# n=7
# basic_roots_by_fundamental_weights=np.zeros((n,n))
# for i in range(n):
#     l=np.zeros(n)
#     l[i]=1
#     basic_roots_by_fundamental_weights[i][:]=BasisTransform(l,2,3,lie)
# print(basic_roots_by_fundamental_weights)

