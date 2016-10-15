# -*- coding: utf-8 -*-

# kargerMinCut

'''
The file contains the adjacency list representation of a simple undirected graph. There are 200
 vertices labeled 1 to 200. The first column in the file represents the vertex label, and the 
 particular row (other entries except the first column) tells all the vertices that the vertex 
 is adjacent to. So for example, the 6th row looks like : "6	155	56	52	120	......". This 
 just means that the vertex with label 6 is adjacent to (i.e., shares an edge with) the vertices 
 with labels 155,56,52,120,......,etc

Your task is to code up and run the randomized contraction algorithm for the min cut problem and
 use it on the above graph to compute the min cut. (HINT: Note that you'll have to figure out an
 implementation of edge contractions. Initially, you might want to do this naively, creating a 
 new graph from the old every time there's an edge contraction. But you should also think about 
 more efficient implementations.) (WARNING: As per the video lectures, please make sure to run 
 the algorithm many times with different random seeds, and remember the smallest cut that you 
 ever find.) Write your numeric answer in the space provided. So e.g., if your answer is 5, just
 type 5 in the space provided.
'''

import random
import math
import copy



def cut(graph):
    while len(graph) > 2:
        rand_node = random.choice(graph.keys())
        rand_edge = random.choice(graph[rand_node])
        #将两个node合并，并将连接这两个node的edge删除
        graph[rand_node] = [i for i in (graph.pop(rand_edge) + graph[rand_node]) if (i != rand_node and i != rand_edge)]
        #将其他node中与这两个node连接的edge合并（其实就是将原来的两个node的名称统一为新的合并的node）
        for key in graph:
            for idx in range(len(graph[key])):
                if graph[key][idx] == rand_edge:
                    graph[key][idx]= rand_node
    for key in graph:
        return len(graph[key])

def min_cut(graph):
    node_num = len(graph)
    repeat_times = 1000 #课程推荐次数为 int(node_num ** 2 * math.log(node_num))
    min_cut_num = None
    for i in range(repeat_times):
        cut_num = cut(copy.deepcopy(graph))
        if min_cut_num is None:
            min_cut_num = cut_num
        elif min_cut_num > cut_num:
            min_cut_num = cut_num
    return min_cut_num
'''
#test case:
graph = {1:[2,3,4,5],2:[1,3,5],3:[1,2,4],4:[1,3,5],5:[1,2,4]}
print min_cut(graph)
'''

# 读取数据为graph dict,并输出结果
file_hand = open('MinCut_data.txt','r')
graph = dict()
for line in file_hand:
    line_list = [int(num) for num in line.split()]
    graph[line_list[0]] = line_list[1:]
print min_cut(graph)
