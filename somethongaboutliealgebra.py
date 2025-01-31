import numpy as np

# '''如果想让print输出的矩阵全是分数就加上下面两行代码'''
from fractions import *
np.set_printoptions(formatter={'all':lambda x: str(Fraction(x).limit_denominator())})#print输出的数组全是分数

#%% 有限维单李代数的一些信息
"""
单根的选取与顺序以Data for Simple Lie Algebra为准
type_of_lie的值必须为大写，n必须是匹配type_of_lie的正整数
"""

#get_cartan_matrix_of_lie_algebra获取An(n>=1),Bn(n>=2),Cn(n>=3),Dn(n>=4)的Cartan矩阵。
def get_cartan_matrix_of_lie_algebra(type_of_lie,n):
    cartan_matrix = np.zeros((n, n))
    if type_of_lie == "A":
        if n == 1:
            cartan_matrix = np.array([2])
        else:
            for i in range(n):
                cartan_matrix[i,i] = 2
                if i == 0:
                    cartan_matrix[i,i + 1] = -1
                elif i == n - 1:
                    cartan_matrix[i,i - 1] = -1
                else:
                    cartan_matrix[i,i + 1] = -1
                    cartan_matrix[i,i - 1] = -1
    elif type_of_lie == "B" and n >= 2:
        for i in range(n):
            cartan_matrix[i,i] = 2
            if i == 0:
                cartan_matrix[i,i + 1] = -1
            elif i == n - 1:
                cartan_matrix[i,i - 1] = -2
            else:
                cartan_matrix[i,i + 1] = -1
                cartan_matrix[i,i - 1] = -1
    elif type_of_lie == "C" and n >= 3:
        for i in range(n):
            cartan_matrix[i,i] = 2
            if i == 0:
                cartan_matrix[i,i + 1] = -1
            elif i == n - 2:
                cartan_matrix[i,i + 1] = -2
                cartan_matrix[i,i - 1] = -1
            elif i == n - 1:
                cartan_matrix[i,i - 1] = -1
            else:
                cartan_matrix[i,i + 1] = -1
                cartan_matrix[i,i - 1] = -1
    elif type_of_lie == "D" and n >= 4:
        for i in range(n):
            cartan_matrix[i,i] = 2
            if i == 0:
                cartan_matrix[i,i + 1] = -1
            elif i == n - 3:
                cartan_matrix[i,n-2] = -1
                cartan_matrix[i,n-1] = -1
                cartan_matrix[i,n-4] = -1
            elif i == n - 2:
                cartan_matrix[i,n-3] = -1
            elif i == n - 1:
                cartan_matrix[i,n-3] = -1
            else:
                cartan_matrix[i,i+1] = -1
                cartan_matrix[i,i-1] = -1
    else:
        print("李代数的类型或n输入错误！")
    return cartan_matrix

#get_simple_roots_by_es_of_lie_algebra获取An(n>=1),Bn(n>=2),Cn(n>=3),Dn(n>=4),En(n=6,7,8),F4,G2的单根在他们对应的标准正交空间V的标准正交基下的表示。
#得到的矩阵simple_roots_by_es每i行（0开始）代表第i+1个单根在V的标准正交基下的表示。
def get_simple_roots_by_es_of_lie_algebra(type_of_lie,n):
    if type_of_lie == "A":
        simple_roots_by_es = np.zeros((n, n+1))
        for i in range(n):
            simple_roots_by_es[i,i] = 1
            simple_roots_by_es[i,i + 1] = -1
    elif type_of_lie == "B" and n >= 2:
        simple_roots_by_es = np.zeros((n,n))
        for i in range(n):
            if i == n - 1:
                simple_roots_by_es[i,i] = 1
            else:
                simple_roots_by_es[i,i] = 1
                simple_roots_by_es[i,i + 1] = -1
    elif type_of_lie == "C" and n >= 3:
        simple_roots_by_es = np.zeros((n, n))
        for i in range(n):
            if i == n - 1:
                simple_roots_by_es[i,i] = 2
            else:
                simple_roots_by_es[i,i] = 1
                simple_roots_by_es[i,i + 1] = -1
    elif type_of_lie == "D" and n >= 4:
        simple_roots_by_es = np.zeros((n, n))
        for i in range(n):
            if i == n - 1:
                simple_roots_by_es[i,i] = 1
                simple_roots_by_es[i,i - 1] = 1
            else:
                simple_roots_by_es[i,i] = 1
                simple_roots_by_es[i,i + 1] = -1
    elif type_of_lie=="E" and n==6:
        simple_roots_by_es=np.array([[1/2,-1/2,-1/2,-1/2,-1/2,-1/2,-1/2,1/2],
             [1,1,0,0,0,0,0,0],
             [-1,1,0,0,0,0,0,0],
             [0,-1,1,0,0,0,0,0],
             [0,0,-1,1,0,0,0,0],
             [0,0,0,-1,1,0,0,0]])
    elif type_of_lie=="E" and n==7:
        simple_roots_by_es = np.array([[1 / 2, -1 / 2, -1 / 2, -1 / 2, -1 / 2, -1 / 2, -1 / 2, 1 / 2],
                       [1, 1, 0, 0, 0, 0, 0, 0],
                       [-1, 1, 0, 0, 0, 0, 0, 0],
                       [0, -1, 1, 0, 0, 0, 0, 0],
                       [0, 0, -1, 1, 0, 0, 0, 0],
                       [0, 0, 0, -1, 1, 0, 0, 0],
                       [0, 0, 0, 0, -1, 1, 0, 0]])
    elif type_of_lie=="E" and n==8:
        simple_roots_by_es= np.array([[1 / 2, -1 / 2, -1 / 2, -1 / 2, -1 / 2, -1 / 2, -1 / 2, 1 / 2],
                       [1, 1, 0, 0, 0, 0, 0, 0],
                       [-1, 1, 0, 0, 0, 0, 0, 0],
                       [0, -1, 1, 0, 0, 0, 0, 0],
                       [0, 0, -1, 1, 0, 0, 0, 0],
                       [0, 0, 0, -1, 1, 0, 0, 0],
                       [0, 0, 0, 0, -1, 1, 0, 0],
                       [0, 0, 0, 0, 0, -1, 1, 0]])
    elif type_of_lie=="F" and n==4:
        simple_roots_by_es = np.array([[1 / 2, -1 / 2, -1 / 2, -1 / 2], [0, 0, 0, 1], [0, 0, 1, -1], [0, 1, -1, 0]])
    elif type_of_lie=="G" and n==2:
        simple_roots_by_es = np.array([[1, -1, 0], [-2, 1, 1]])
    else:
        print("李代数的类型或n输入错误！")
    return simple_roots_by_es

#get_fundamental_weights_by_es_of_lie_algebra获取An(n>=1),Bn(n>=2),Cn(n>=3),Dn(n>=4)的单根对应的基本权在V的标准正交基下的表示。
#得到的矩阵fundamental_weights_by_es/denominator（为保精度，把分母denominator提出来）的每i行（0开始）代表第i+1个单根对应的基本权在V的标准正交基下的表示。
def get_fundamental_weights_by_es_of_lie_algebra(type_of_lie,n):
    if type_of_lie == "A":
        fundamental_weights_by_es = np.zeros((n, n+1))
        denominator = n + 1
        for i in range(n):
            for j in range(n+1):
                if j <= i:
                    fundamental_weights_by_es[i,j] = n - i
                else:
                    fundamental_weights_by_es[i,j] = -i - 1
    elif type_of_lie == "B" and n >= 2:
        fundamental_weights_by_es = np.zeros((n, n))
        denominator = 2
        for i in range(n):
            if i == n - 1:
                for j in range(n):
                    fundamental_weights_by_es[i,j] = 1
            else:
                for j in range(n):
                    if j <= i:
                        fundamental_weights_by_es[i,j] = 2
    elif type_of_lie == "C" and n >= 3:
        fundamental_weights_by_es = np.zeros((n, n))
        denominator = 1
        for i in range(n):
            for j in range(n):
                if j <= i:
                    fundamental_weights_by_es[i,j] = 1
    elif type_of_lie == "D" and n >= 4:
        fundamental_weights_by_es = np.zeros((n, n))
        denominator = 2
        for i in range(n):
            if i <= n - 3:
                for j in range(n):
                    if j <= i:
                        fundamental_weights_by_es[i,j] = 2
            elif i == n - 2:
                for j in range(n):
                    if j != n - 1:
                        fundamental_weights_by_es[i,j] = 1
                    elif j == n - 1:
                        fundamental_weights_by_es[i,j] = -1
            elif i == n - 1:
                for j in range(n):
                    fundamental_weights_by_es[i,j] = 1
    else:
        print("李代数的类型或n输入错误！")
    return fundamental_weights_by_es, denominator

# """测试get_cartan_matrix_of_lie_algebra、get_simple_roots_by_es_of_lie_algebra、get_fundamental_weights_by_es_of_lie_algebra"""
# type_of_lie="D"
# n=10
# print("典型李代数"+str(type_of_lie)+"_"+str(n)+"的一些信息：")
# print("Cartan矩阵:")
# print(get_cartan_matrix_of_lie_algebra(type_of_lie,n))
# print("单根在他们对应的标准正交空间V的标准正交基下的表示:")
# print(get_simple_roots_by_es_of_lie_algebra(type_of_lie,n))
# fundamental_weights_by_es, denominator=get_fundamental_weights_by_es_of_lie_algebra(type_of_lie,n)
# print("基本权在V的标准正交基坐标下每个分量乘上" + str(denominator) + "的结果（供精度检查）:")
# print(fundamental_weights_by_es)
# print("基本权在V的标准正交基坐标下的表示:")
# print(fundamental_weights_by_es/denominator)



#%%与换基底有关的一些程序

#find_cartan_matrix用于计算任意根系的cartan矩阵。
#输入根在V的标准正交基坐标下的表示root矩阵与根的个数numsofroots，得到对应的cartan矩阵。
def find_cartan_matrix(root,numsofroots):
    if numsofroots==1:
        cartan=np.array([2])
    else:
        cartan = np.zeros((numsofroots, numsofroots))
        for i in range(numsofroots):
            for j in range(numsofroots):
                cartan[i, j] = 2 * np.dot(root[i], root[j]) / np.dot(root[i], root[i])
    return cartan

#find_weights_by_es用于计算所有基本权在单根下的表示。
#输入根在V的标准正交基坐标下的表示root矩阵（最好全部是单根）与根的个数numsofroots，得到对应的所有基本权在单根下的表示Wtt矩阵。
#一旦root矩阵里面出现分数，此函数得到的结果（因为linalg）在后续计算中容易出错，建议手动输入Wtt。
def find_weights_by_es(root,numsofroots):
    cartan = find_cartan_matrix(root, numsofroots)
    Wtt = np.zeros((numsofroots, numsofroots))
    W = np.identity(numsofroots)
    for i in range(numsofroots):
        Wtt[i] = np.linalg.solve(cartan, W[i])
    return Wtt

#下面六个用于坐标转换（单根、基本权、V的标准正交基）l表示待转换坐标的向量
def from_roots_to_es(l,root,numsofroots,numsofes):
    transformedl = np.zeros(numsofes)
    for i in range(numsofroots):
        transformedl = transformedl + l[i] * root[i]
    return transformedl
def from_weights_to_roots(l,Wtt,numsofroots):#基本权坐标转为基本根坐标
    transformedl = np.zeros(numsofroots)
    for i in range(numsofroots):
        transformedl = transformedl + l[i] * Wtt[i]
    return transformedl
def from_weights_to_es(l,root,Wtt,numsofroots,numsofes):#基本权坐标转为欧式坐标
    transformedl =from_weights_to_roots(l, Wtt, numsofroots)
    transformedl =from_roots_to_es(transformedl,root,numsofroots,numsofes)
    return transformedl
def from_es_to_weights(l,root,numsofroots):
    l = np.dot(root, l.T)
    for i in range(numsofroots):
        l[i] = 2 * l[i] / np.dot(root[i], root[i].T)  # l从欧拉坐标转为基本权坐标
    return l
def from_es_to_roots(l,root,Wtt,numsofroots):
    transformedl=from_es_to_weights(l,root,numsofroots)
    transformedl=from_weights_to_roots(transformedl,Wtt,numsofroots)
    return transformedl
def from_roots_to_weights(l,root,numsofroots,numsofes):
    transformedl=from_roots_to_es(l,root,numsofroots,numsofes)
    transformedl=from_es_to_weights(transformedl,root,numsofroots)
    return transformedl

#basistransform是上面六个的集合
#类型用数字表示：1表示欧氏坐标，2表示基本根坐标，3表示基本权坐标
#vector是待转换坐标的向量，typeofvector是待转换向量的坐标类型，typeoftransforminto是待转换向量需要转入的坐标类型，root是待转换坐标向量所在李代数的单根在V的标准基下的表示矩阵
def basistransform(vector,typeofvector,typeoftransforminto,root):
    numsofroots = int(root.shape[0])  ##基本根的个数
    numsofes = int(root.shape[1])  ##欧式空间的维数，ei的个数
    Wtt = find_weights_by_es(root, numsofroots)
    if typeofvector==1 and typeoftransforminto==2:
        result=from_es_to_roots(vector,root,Wtt,numsofroots)
    elif typeofvector==1 and typeoftransforminto==3:
        result=from_es_to_weights(vector, root, numsofroots)
    elif typeofvector == 2 and typeoftransforminto == 1:
        result =from_roots_to_es(vector,root,numsofroots,numsofes)
    elif typeofvector == 2 and typeoftransforminto == 3:
        result =from_roots_to_weights(vector,root,numsofroots,numsofes)
    elif typeofvector == 3 and typeoftransforminto == 1:
        result =from_weights_to_es(vector,root,Wtt,numsofroots,numsofes)
    elif typeofvector == 3 and typeoftransforminto == 2:
        result =from_weights_to_roots(vector,Wtt,numsofroots)
    else:
        print("向量类型或向量输出类型输入错误！")
        result=vector
    return result

# # """测试"""
# root=get_simple_roots_by_es_of_lie_algebra("E",6)
# numsofroots=int(root.shape[0])##基本根的个数
# numsofes=int(root.shape[1])##欧式空间的维数，ei的个数
# l=np.array([1,1,1,1,1,1])#基本权表示下，分量全为1，此为rho
# Wtt=find_weights_by_es(root,numsofroots)
# print(Wtt)
# print(from_weights_to_es(l,root,Wtt,numsofroots,numsofes))
# print(basistransform(l,3,1,root))


#%%单根分类以及获得典型单李代数之间的同态

#clasify_simple_roots用于分类一堆单根获取单根分类表
#find_isomorphism_of_simple_lie_algebra用于找已经分类为单李代数的cartan图的类别以及同态（单根映为单根）

#exchange_simple_roots用于交换第i+1与j+1个单根的编号，输出交换编号后的cartan矩阵
def exchange_simple_roots(i,j,cartan):
    cartan[:, [i, j]] = cartan[:, [j, i]]
    cartan[[i, j], :] = cartan[[j, i], :]
    return cartan

#count_nonzero用于数给定一维向量中非零元的个数nums_of_sametype，以及非零元的位置id_of_sametype(从1开始的序号!）
def count_nonzero(l):
    lenthofl = int(l.shape[0])
    nums_of_sametype = 0
    for i in range(lenthofl):
        if l[i] != 0:
            if nums_of_sametype == 0:
                id_of_sametype = np.array([i + 1])
                nums_of_sametype = 1
            else:
                id_of_sametype = np.insert(id_of_sametype, [nums_of_sametype], i + 1)
                nums_of_sametype = nums_of_sametype + 1
    return id_of_sametype,nums_of_sametype

#clasify_simple_roots用于分类一堆单根，输入cartan矩阵输出types,nums_of_types
def clasify_simple_roots(cartan):
    nums_of_simple_roots = int(cartan.shape[0])
    types = np.zeros((2, nums_of_simple_roots))  # types第一行是单根的序号，第二行是对应单根所在类
    for i in range(nums_of_simple_roots):  # 将type第一行顺次编号（从1开始），作为cartan阵对应的单根的序号
        types[0][i] = i + 1
    nums_of_types = 1#记录单根归为多少类别
    types[1][0] = 1#默认填写的cartan阵至少为1维
    for choose in range(nums_of_simple_roots):
        id_of_sametype, nums_of_sametype = count_nonzero(cartan[choose][:])#得到第choose+1个单根所在行有多少个非零元，以及这些非零元的单根序号
        thetypeoftheseid = 0#记录第choose+1个单根所在类
        for i in range(nums_of_sametype):#此for循环用于寻找与第choose+1个单根链接的单根（包括自己）的类是否已被记录在types里
            if types[1][id_of_sametype[i] - 1] != 0:#如果与第choose+1个单根有链接的单根的类已经被记录在types里，就记录进去
                thetypeoftheseid = types[1][id_of_sametype[i] - 1]
        if thetypeoftheseid == 0:#如果与第choose+1个单根有链接的单根的类都没有被记录
            nums_of_types = nums_of_types + 1#说明这可能是新的一类
            for j in range(nums_of_sametype):
                types[1][id_of_sametype[j] - 1] = nums_of_types
        else:
            for j in range(nums_of_sametype):
                types[1][id_of_sametype[j] - 1] = thetypeoftheseid
    #print("first"+str(types))
    #最后把同一类，但是标号不一样的统一为同一类
    for choose in range(nums_of_simple_roots):
        id_of_sametype, nums_of_sametype = count_nonzero(cartan[choose][:])
        # print(str(choose)+":"+str(id_of_sametype))
        thistypeofit=types[1][choose]
        whichtypeofit=types[1][choose]
        for i in range(nums_of_sametype):#此for循环用于寻找与第choose+1个单根链接的单根（包括自己）的类是否不一致
            if types[1][id_of_sametype[i]-1]<whichtypeofit:
                whichtypeofit=types[1][id_of_sametype[i]-1]
        if thistypeofit!=whichtypeofit:
            nums_of_types=nums_of_types-1
            max1=max(thistypeofit,whichtypeofit)
            min1=min(thistypeofit,whichtypeofit)
            for j in range(nums_of_simple_roots):
                if types[1][j]==max1:
                    types[1][j]=min1
            for j in range(nums_of_simple_roots):
                if types[1][j]>max1:
                    types[1][j] =types[1][j]-1
        #print(types)
    return types,nums_of_types

# C=np.array([[2,0 ,0 ,0 ,0 ,0 ,0 ,-1],
#  [0, 2, 0 ,-1, -1 ,0 ,0 ,0],
#  [0, 0 ,2 ,0, 0, 0 ,-1 ,0],
#  [0, -1, 0 ,2 ,0 ,0 ,0, 0],
#  [0 ,-1 ,0 ,0 ,2, -1, 0, -1],
#  [0 ,0, 0 ,0 ,-1 ,2 ,0, 0],
#  [0 ,0 ,-1, 0 ,0 ,0 ,2, 0],
#  [-1, 0 ,0, 0, -1, 0 ,0 ,2]])
# print(clasify_simple_roots(C))

#找矩阵中的某一个特定元素，输出这个元素的位置（从（0，0）开始）
def find_element(matrix, target):##参考自https://blog.51cto.com/u_16213357/9774583
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == target:
                return (i, j)
    return None

#判断单李代数的类型
def judge_simple_lie_algebra(cartan):
    nums_of_simple_roots = int(cartan.shape[0])
    tuple2 = find_element(cartan, -2)
    tuple3=find_element(cartan,-3)
    if tuple3 is None:
        if tuple2 is None:
            isd = 0
            for i in range(nums_of_simple_roots):
                l1, l2 = count_nonzero(cartan[i][:])
                if l2 == 4:
                    adjointnums=0
                    for k in range(l2):
                        lll1,lll2=count_nonzero(cartan[l1[k]-1][:])
                        if lll2==3:
                            adjointnums=adjointnums+1
                    if adjointnums>1:
                        typeofit = "E"
                        isd = 1
                        break
                    else:
                        typeofit = "D"
                        isd = 1
                        break
            if isd == 0:
                typeofit = "A"
        else:
            row = tuple2[0]
            print(row)
            l1, l2 = count_nonzero(cartan[row][:])
            if nums_of_simple_roots == 2:
                typeofit = "B"
            elif nums_of_simple_roots == 1:
                print("输入的cartan矩阵有误!")
            else:
                if l2 == 2:
                    typeofit = "B"
                elif l2 == 3:
                    l11, l22 = count_nonzero(cartan[:][row])
                    if l22 == 2:
                        typeofit = "C"
                    elif l22 == 3:
                        typeofit = "F"
                else:
                    print("输入的cartan矩阵有误!")
    else:
        typeofit = "G"
    return typeofit

def find_isomorphism_of_simple_A_lie_algebra(cartan):
    nums_of_simple_roots = int(cartan.shape[0])
    founded = -1
    isomorphism = -np.ones(nums_of_simple_roots)
    if nums_of_simple_roots==1:
        isomorphism=np.array([0])
    else:
        for i in range(nums_of_simple_roots):
            l1, l2 = count_nonzero(cartan[i][:])
            if l2 == 2:  # 第i+1个单根是A的头或尾
                isomorphism[i] = 0  # 第i+1个单根映到到An的第0+1个单根
                founded = 0
                break
        if founded == -1:
            print("输入的A型单李代数有误！")
        else:
            while founded < nums_of_simple_roots - 1:
                for i in range(l2):
                    if isomorphism[l1[i] - 1] == -1:
                        founded = founded + 1
                        isomorphism[l1[i] - 1] = founded
                        l1, l2 = count_nonzero(cartan[l1[i] - 1][:])
                        break
    return isomorphism

def find_isomorphism_of_simple_D_lie_algebra(cartan):
    nums_of_simple_roots = int(cartan.shape[0])
    founded = -1
    isomorphism = -np.ones(nums_of_simple_roots)
    for i in range(nums_of_simple_roots):
        l1, l2 = count_nonzero(cartan[i][:])
        if l2 == 4:  # 第i+1个单根是D的倒数第3个单根
            isomorphism[i] = nums_of_simple_roots-3  # 第i+1个单根映到到Dn的第n-3+1个单根
            founded = 0
            break
    if founded == -1:
        print("输入的D型单李代数有误！")
    else:
        if nums_of_simple_roots==4:
            for i in range(l2):
                if isomorphism[l1[i] - 1] == -1:
                    founded = founded + 1
                    isomorphism[l1[i] - 1] =  founded
        elif nums_of_simple_roots>4:
            for i in range(l2):
                if isomorphism[l1[i] - 1] == -1:
                    ll1, ll2 = count_nonzero(cartan[l1[i] - 1][:])
                    if ll2 == 2:
                        founded = founded + 1
                        isomorphism[l1[i] - 1] = nums_of_simple_roots - 3 + founded
            founded = -1
            for i in range(nums_of_simple_roots):
                if isomorphism[i] == -1:
                    l1, l2 = count_nonzero(cartan[i][:])
                    if l2 == 2:  # 第i+1个单根是D的头
                        isomorphism[i] = 0  # 第i+1个单根映到到Dn的第0+1个单根
                        founded = 0
                        break
            if founded == -1:
                print("输入的D型单李代数有误！")
            else:
                while founded < nums_of_simple_roots - 4:
                    for i in range(l2):
                        if isomorphism[l1[i] - 1] == -1:
                            founded = founded + 1
                            isomorphism[l1[i] - 1] = founded
                            l1, l2 = count_nonzero(cartan[l1[i] - 1][:])
                            break
    return isomorphism

def find_isomorphism_of_simple_B_lie_algebra(cartan):
    nums_of_simple_roots = int(cartan.shape[0])
    tuple = find_element(cartan, -2)
    row = tuple[0]
    isomorphism = -np.ones(nums_of_simple_roots)
    isomorphism[row] = nums_of_simple_roots-1#第row+1个单根是B的倒数第1个根
    founded=0
    l1,l2=count_nonzero(cartan[row][:])
    while founded < nums_of_simple_roots - 1:
        for i in range(l2):
            if isomorphism[l1[i] - 1] == -1:
                founded = founded + 1
                isomorphism[l1[i] - 1] =nums_of_simple_roots-1-founded
                l1, l2 = count_nonzero(cartan[l1[i] - 1][:])
                break
    return isomorphism

def find_isomorphism_of_simple_C_lie_algebra(cartan):
    nums_of_simple_roots = int(cartan.shape[0])
    tuple = find_element(cartan, -2)
    colunm = tuple[1]
    isomorphism = -np.ones(nums_of_simple_roots)
    isomorphism[colunm] = nums_of_simple_roots-1#第colunm+1个单根是C的倒数第1个根#后面和B的一样，因为C和B的cartan阵互为转置
    l1,l2=count_nonzero(cartan[colunm][:])
    founded=0
    while founded < nums_of_simple_roots - 1:
        for i in range(l2):
            if isomorphism[l1[i] - 1] == -1:
                founded = founded + 1
                isomorphism[l1[i] - 1] =nums_of_simple_roots-1-founded
                l1, l2 = count_nonzero(cartan[l1[i] - 1][:])
                break
    return isomorphism

#找单李代数之间的同态（仅典型型）
def find_isomorphism_of_simple_lie_algebra(cartan):
    typeofit=judge_simple_lie_algebra(cartan)
    if typeofit=="A":
        isomorphism=find_isomorphism_of_simple_A_lie_algebra(cartan)
    elif typeofit=="B":
        isomorphism = find_isomorphism_of_simple_B_lie_algebra(cartan)
    elif typeofit == "C":
        isomorphism = find_isomorphism_of_simple_C_lie_algebra(cartan)
    elif typeofit == "D":
        isomorphism = find_isomorphism_of_simple_D_lie_algebra(cartan)
    else:
        isomorphism=np.zeros([1])
        print("出错！不是典型李代数！")
    return isomorphism,typeofit



##测试
#'''
print("输入的cartan矩阵为：")
cartan=np.array([[2 ,-1, 0, 0, 0],
 [-1, 2 ,0 ,-1, 0 ],
 [0, 0, 2, 0 ,-1 ],
 [0 ,-1 ,0 ,2 ,0 ],
  [0, 0 ,-1 ,0 ,2 ]])
print(cartan)
types, nums_of_types = clasify_simple_roots(cartan)
print("单根分类情况（第一行为根的序号，第二行为类）：")
print(types)
nums_of_simple_roots = int(cartan.shape[0])
for i in range(nums_of_types):
    thetype = []
    for j in range(nums_of_simple_roots):
        if types[1][j] == i + 1:
            thetype = thetype + [j]
    a = cartan[thetype][:, thetype]
    print("第" + str(i + 1) + "个类别的Cartan矩阵为：")
    print(a)
    print("此单李代数的类型为："+str(judge_simple_lie_algebra(a)))
    isomorphism,typeofit=find_isomorphism_of_simple_lie_algebra(a)
    print("到标准顺序下的对应单李代数的同态为(此单李代数的第i个根映到对应李代数的第j个根（i，j从0开始）：")
    print(isomorphism)
print("================================================================================")
print("输入的cartan矩阵为：")
cartan=get_cartan_matrix_of_lie_algebra("D",5)
exchange_simple_roots(0,3,cartan)
exchange_simple_roots(2,3,cartan)
print(cartan)
types, nums_of_types = clasify_simple_roots(cartan)
print("单根分类情况（第一行为根的序号，第二行为类）：")
print(types)
nums_of_simple_roots = int(cartan.shape[0])
for i in range(nums_of_types):
    thetype = []
    for j in range(nums_of_simple_roots):
        if types[1][j] == i + 1:
            thetype = thetype + [j]
    a = cartan[thetype][:, thetype]
    print("第" + str(i + 1) + "个类别的Cartan矩阵为：")
    print(a)
    print("此单李代数的类型为："+str(judge_simple_lie_algebra(a)))
    isomorphism,typeofit=find_isomorphism_of_simple_lie_algebra(a)
    print("到标准顺序下的对应单李代数的同态为(此单李代数的第i个根映到对应李代数的第j个根（i，j从0开始）)：")
    print(isomorphism)
print("================================================================================")



#'''