import pandas as pd
import numpy as np
import copy
from tqdm import tqdm

# Function for measure similarty of two points
def simi(i,j):
    return len(i[1]&j[1])/len(i[1]|j[1])

# Function for measure distance of two clusters
def dist(Ci,Cj):
     return sum(simi(i, j) for i in Ci for j in Cj)/(len(Ci)*len(Cj))

# Function to find minist S in distance matrix
def find_Max(M):
    max = 0
    x = 0; y = 0
    for i in range(len(M)):
        for j in range(len(M[i])):
            if (i != j) and (M[i][j]>=max):
                max = M[i][j];x = i; y = j
    return (x, y, max)

# Function for update
def update(C,M,T,target):
    whole = len(C)
    now = whole
    point = 1
    for cycles in tqdm(range(whole - target),desc = f'Running: {now} clusters now'):
        
        x, y, maxs = find_Max(M)

       # end point 
        if maxs == 0:
            point = 0 
            break
       # update T
        length = maxs
       
       # c1 = 0
       # for i in T[x]:
       #     if i == '('or ')':
       #        c1 += 1
       # if c1 < 2:
       #      t1 = T[X] + ':' + str(length)
       # else:
       #     t1 = T[x] + '1' + ':' + str(length) 
       
       # c2 = 0
       # for i in T[y]:
       #     if i == '(' or ')':
       #         c2 += 1
       # if c2 < 2:
       #     t2 = T[y] + ':' + str(length)
       # else:
       #     t2 = T[y] + '1' + ':' + str(length)
       
        t = '(' + T[x] + ',' + T[y] + ')'

        temp1 = T[x];temp2 = T[y]
        T.remove(temp1);T.remove(temp2)
        T.append(t)

        # update C
        Cm = C[x] + C[y]
        temp1 = C[x];temp2 = C[y]
        C.remove(temp1);C.remove(temp2);C.append(Cm)
        
        # update M
        ## del row
        l =sorted([x,y])[::-1]
        for i in l:
            M.pop(i)
        ## del col
        for i in l:
            for Mi in M:
                Mi.pop(i)
        ## add row
        Mm = []
        for Ci,Mi in zip(C[0:len(C)-1],M):
            d = dist(Ci,Cm)
            Mi.append(d)
            Mm.append(d)
        ## add col
        Mm.append(1.0)
        M.append(Mm)

        # update cluster number
        now -= 1
    return C,M,T,point
        
# load dataset
data = pd.read_csv('./new.csv')
data = np.array(data)

# create node,which is just like [gene,{term set}]
Gene2ID = {}
for i,j in zip(data[:,1],data[:,0]):
    if not Gene2ID.get(j, False):
        Gene2ID[j] = []
    Gene2ID[j].append(i)


nodes = []
for k,v in Gene2ID.items():
    node = []
    node.append(k)
    node.append(set(v))
    nodes.append(node)

# intialize clusters & distance matrix
C = [];M = [];T = []
for i in nodes:
    Ci = []
    Ti = []
    Ci.append(i)
    Ti.append(i[0])
    C.append(Ci)
    T.append(str(Ti))
for i in C:
    Mi = []
    for j in C:
        Mi.append(dist(i, j))
    M.append(Mi)



print('Dateset has been load on.')

# AGNES update for 8/16/32 clusters
print('AGNES START')
r = 1
for target in [16,8,32]:
    print(f'round {r}/3')
    Cr,Mr,Tr,point = update(copy.deepcopy(C),copy.deepcopy(M),copy.deepcopy(T),target)

    
    # store in result.txt
    filename = 'clusters_' + str(target) + '.txt'
    with open(filename,'w') as f:

        for i in Mr:
            f.write(str(i))
            f.write('\r\n')
            f.write('\n')

        for i in Cr:
            f.write(str(i))
            f.write('\r\n')
            f.write(str(len(i)))
            f.write('\n')
       # for i in edges:
        #    f.write(str(i))
         #   f.write('\r\n')
       
        for i in Tr:
            f.write(str(i))
            f.write('\r\n')
            f.write('\n')
    r+= 1
    
    # end point
    if point == 0:
        break
print('Programme end')
