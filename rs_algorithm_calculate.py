import numpy as np
import math as math
from collections import Counter

'''参考：1,Iwahori_Hecke Algebras and Schur Algebras of the Symmetric Group:p52.24.
2.Gelfand—Kirillov Dimensions and Associated Varieties of Highest Weight Moudules:Theorem1.5'''
'''参考：3.Gelfand—Kirillov Dimension and Reducibility of Scalar Generalized Verma Modules for Classical Lie Algebras:Proposition3.9'''
# l：欧式坐标下
# lie代数的类型：typeoflie="A"，a型李代数；typeoflie="B"或“C”，b、c型李代数；typeoflie=“D”，d型李代数
# rs_algorithm与rs_algorithm_and_shape是同样的函数，第一个只输出rs算法的young图shape，第二个不止输出rs算法的young图shape还会输出具体的young图（矩阵形式，里面的0不一定是young图的数字）
def rs_algorithm(l,n):
    shape = np.zeros(n).astype(int)
    RS = np.zeros((n, n))
    for k in range(n):
        judge=1
        t=l[k]
        i=0
        while judge!=0:
            if shape[i]==0:
                RS[i][0]=t
                shape[i] = shape[i] + 1
                judge = 0
            elif t>=RS[i][shape[i]-1]:
                shape[i]=shape[i]+1
                RS[i][shape[i]-1]=t
                judge=0
            else:
                for a in range(shape[i]):
                    if RS[i][a]>t:
                        z=RS[i][a]
                        RS[i][a]=t
                        t=z
                        i=i+1
                        break
    return shape
def rs_algorithm_and_shape(l,n):
    shape = np.zeros(n).astype(int)
    RS = np.zeros((n, n))
    for k in range(n):
        judge=1
        t=l[k]
        i=0
        while judge!=0:
            if shape[i]==0:
                RS[i][0]=t
                shape[i] = shape[i] + 1
                judge = 0
            elif t>=RS[i][shape[i]-1]:
                shape[i]=shape[i]+1
                RS[i][shape[i]-1]=t
                judge=0
            else:
                for a in range(shape[i]):
                    if RS[i][a]>t:
                        z=RS[i][a]
                        RS[i][a]=t
                        t=z
                        i=i+1
                        break
    return shape,RS
def find_peven(p,n):
    j = 0
    peven = np.zeros(n)  # p（lambda）even
    for i in range(n):
        if j==0:
            peven[i]=math.ceil(p[i]/2)
            j=1
        else:
            peven[i]=math.floor(p[i]/2)
            j=0
    return peven
def calculate(p,n):
    result=0
    for i in range(n):
      result=result+i*p[i]
    return result
def afunction(l,typeoflie):#l的分量全是整数时，计算a函数
    lenthofl=int(l.shape[0])
    if typeoflie == "B" or typeoflie == "C" or typeoflie=="D":
        newl = np.zeros(2 * lenthofl)
        for i in range(lenthofl):
            newl[i] = l[i]
            newl[2 * lenthofl - 1 - i] = -l[i]
        l = newl
        lenthofl = 2 * lenthofl # 如果是bcd型李代数，算的RSYoung图需要对权做处理
    p = rs_algorithm(l, lenthofl)  # 算对应的RSYoung图的Shape
    peven = find_peven(p, lenthofl)
    podd = p - peven  # p（lambda）odd
    if typeoflie == "A":
        a=calculate(p, lenthofl)
    elif typeoflie == "B" or typeoflie=="C":
        a=calculate(podd, lenthofl)
    elif typeoflie == "D":
        a=calculate(peven, lenthofl)
    return a
def find_vector(l,lenthofl,lintegral,findwhat,valueoffindwhat):
    vector=np.zeros(valueoffindwhat)
    judge=0
    for i in range(lenthofl):
        if lintegral[i]==findwhat:
            vector[judge]=l[i]
            judge=judge+1
    #print(vector)
    return vector
def find_vector_wildtilde(vector):
    lenthofvector = int(len(vector))
    vector_wildtilde = np.zeros(lenthofvector)
    numsofnoninteger=0
    numsofinteger=1
    for i in range(lenthofvector):
        if i==0:
            vector_wildtilde[i] = vector[i]
        else:
            difference=vector[i]-vector[0]
            if difference-round(difference)==0:
                vector_wildtilde[numsofinteger]=vector[i]
                numsofinteger=numsofinteger+1
            else:
                vector_wildtilde[lenthofvector-1-numsofnoninteger]=-vector[i]
                numsofnoninteger=numsofnoninteger+1
    ##print(str(vector)+"的wildtilde向量为"+str(vector_wildtilde))
    return vector_wildtilde
def afunction_of_non_integral(l, typeoflie):
    lenthofl = int(len(l))
    lintegral = np.zeros(lenthofl)#四舍五入取l每个分量的小数部分
    for i in range(lenthofl):
        lintegral[i] = abs(round(l[i]) - l[i])
    counter = Counter(lintegral)
    count = list(counter.keys())#l每个分量的小数部分的类别汇总
    valueofcount = list(counter.values())#l每个分量小数部分类别的的个数
    lenthofcount = len(count)
    a = 0
    if typeoflie == "A":
        for i in range(lenthofcount):
            vector = find_vector(l, lenthofl, lintegral, count[i], valueofcount[i])
            a = a + afunction(vector, "A")
    elif typeoflie=="B":
        for i in range(lenthofcount):
            if count[i]==0:
                vector = find_vector(l, lenthofl, lintegral, count[i], valueofcount[i])
                a = a + afunction(vector, "B")
            elif count[i]==0.5:
                vector = find_vector(l, lenthofl, lintegral, count[i], valueofcount[i])
                a = a + afunction(vector, "B")
            else:
                vector = find_vector(l, lenthofl, lintegral, count[i], valueofcount[i])
                vector=find_vector_wildtilde(vector)
                a = a + afunction(vector, "A")
    elif typeoflie == "C":
        for i in range(lenthofcount):
            if count[i] == 0:
                vector = find_vector(l, lenthofl, lintegral, count[i], valueofcount[i])
                a = a + afunction(vector, "B")
            elif count[i] == 0.5:
                vector = find_vector(l, lenthofl, lintegral, count[i], valueofcount[i])
                a = a + afunction(vector, "D")
            else:
                vector = find_vector(l, lenthofl, lintegral, count[i], valueofcount[i])
                vector = find_vector_wildtilde(vector)
                a = a + afunction(vector, "A")
    elif typeoflie == "D":
        for i in range(lenthofcount):
            if count[i] == 0:
                vector = find_vector(l, lenthofl, lintegral, count[i], valueofcount[i])
                a = a + afunction(vector, "D")
            elif count[i] == 0.5:
                vector = find_vector(l, lenthofl, lintegral, count[i], valueofcount[i])
                a = a + afunction(vector, "D")
            else:
                vector = find_vector(l, lenthofl, lintegral, count[i], valueofcount[i])
                vector = find_vector_wildtilde(vector)
                a = a + afunction(vector, "A")
    return a

#示例：print(afunction(np.array([-3/2,-3/2,1/2,-1/2]),"B"))