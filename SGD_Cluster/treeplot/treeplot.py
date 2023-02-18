
from ete3 import Tree,TreeStyle
import sys

sys.setrecursionlimit(2000000000)

file = open('tree_data_temp')
read = file.readlines()
file.close()

branch  = []
for i in read:
    i = i.replace('[','')
    i = i.replace(']','')
    branch.append(i)
    # print(type(i))
    # print(i)

c = 0
for i in branch:
    c += 1
    # print(i)
    # print(type(i))
    t = Tree(i)
    ts = TreeStyle()
    ts.show_leaf_name = True
    ts.mode = "c"
    ts.arc_start = -180 # 0 degrees = 3 o'clock
    ts.arc_span = 360
    # print(t)
    #t.write(outfile='test.ns')
    t.render(f'cluster{c}.svg',tree_style = ts)













