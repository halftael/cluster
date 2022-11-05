import pandas as pd
import numpy as np
import time




class go_term():

    def __init__(self,id,term):
        # 定义了父节点集合 ，子节点集合 ，列表型变量深度，本基因集合，go id&go term
        self.id = id
        self.term = term
        self.gene = []

    def add(self,gene):
        # 用于向term集中添加基因
        self.gene.append(gene)



def P_set(go_term_set)->list[set]:
    # 生成全集的power_set
    # !!!!!! 实际上 由于时间复杂度达到指数阶2^n,本函数弃用
    N = len(go_term_set)
    P_set = []
    for i in range(2 ** N):  # 子集个数，每循环一次一个子集
        print('1')
        # for j in range(N):  # 用来判断二进制下标为j的位置数是否为1
        #     if (i >> j) % 2:
        #         P_set.append(go_term_set[j])
    return P_set

def Generalized_or(subset):
    # 以递归的形式求集合的广义并
    cover = {}
    for j in subset:
        cover = cover|j.gene
    return cover

def Generalized_and(subset,go_term_set):
    # 以递归的形式求集合的广义并
    core = []
    for i in go_term_set:
        core.append(i.gene)
    core = set(core)

    for j in subset:
        core = core&j.gene
    return core

# def optimization(self):
#     # 求最优化的子集

def greedy():
    # 遍历集合，计算出最高复杂度










data1 = pd.read_csv('id&term_bp.CSV')
data1 = np.array(data1)



d = []

ids = data1[:,0]
terms = data1[:,1]
for m,n in zip(ids,terms):
    p = go_term(m,n)
    d.append(p)

data2 = pd.read_csv('gene2id.CSV')
data2 = np.array(data2)


genes = data2[:,0]
gti = data2[:,1]
for i in d:
    for o,p in zip(genes,gti):
        if p == i.id:
            i.add(o)

print(len(set(genes)))


# for i in d:
#     print(i.id,i.gene)
#     print(set(i.gene))


# pst = P_set(d)
