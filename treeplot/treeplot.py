import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd


def kvp_generation(data):
    # 要求传入data为array数据类型，返回一个一个字典，key=节点id，value=节点的子节点id

    id2id = {}
    for i in range(99):
        for j in range(1, 5):
            if str(data[i, j])[0] == '1':
                if not id2id.get(f'{data[i, j][1:]}'.strip(), False):
                    id2id[f'{data[i, j][1:]}'.strip()] = []
                id2id[f'{data[i, j][1:]}'.strip()].append(data[i, 0])
            elif str(data[i, j])[0] == '2':
                if not id2id.get(f'{data[i, 0]}'.strip(), False):
                    id2id[f'{data[i, 0]}'.strip()] = []
                id2id[f'{data[i, 0]}'.strip()].append(data[i, j][1:])
            else:
                continue
    return id2id


def edgeTP_list(kvp:dict):
    # 根据键值对生成边列表
    edgeTP_list = []
    for k, v in kvp.items():
        for i in v:
            a = (k, i)
            print(a)
            edgeTP_list.append(a)
    return edgeTP_list


def main():
    # 数据转化为矩阵
    data = pd.read_csv('id2id.CSV')
    data = np.array(data)

    # 生成键值对和元组列表
    kvp = kvp_generation(data)
    assert kvp
    edgelist = edgeTP_list(kvp)
    assert edgelist

    # 创建有向图G数据结构
    G = nx.Graph()
    G.add_edges_from(edgelist)
    nx.draw(G,  # with_labels=True,
            edge_color='k',
            node_size=10,
            node_shape='o',
            linewidths=2,
            width=1.0,
            alpha=0.55,
            style='solid',
            font_size=9,
            font_color='k')
    # matlibplot & networkx 有良好的接口
    plt.show()


if __name__ == '__main__':
    main()
