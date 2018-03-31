import random
import numpy as np
import time
import datetime
from kdtree import *
# kdtree = KDTree(4)
# for i in range(100):
#     kdtree.insert([i,i,i,i])
# kdtree.delete([0,0,0,0])
# kdtree.delete([1,1,1,1])
# print(kdtree.findnearest([0,10,0,10]))


DIM = 1000
NUM = 1000

kdtree = KDTree(DIM)
point = []

for i in range(NUM):
    # temp = np.array([random.randint(1,100) for j in range(DIM)])
    temp = np.array([random.random() for j in range(DIM)])
    point.append(temp)
    kdtree.insert(temp)

temp = np.array([random.random() for j in range(DIM)])
# dist1 = MAXDIST
# print('11111111111111 ' + str(datetime.datetime.now()))
# # start = datetime.datetime.now()
# for i in range(NUM):
#     dist1 = min(dist1, sum((point[i] - temp) ** 2))
# # end = datetime.datetime.now()
# print('11111111111111 ' + str(datetime.datetime.now()))
# print(dist1)
# # print(end-start)
#
# # start = datetime.datetime.now()
# print('11111111111111 ' + str(datetime.datetime.now()))
# dist2 = kdtree.findnearest(temp)[0]
# # end = datetime.datetime.now()
#
# # print(end-start)
# print('11111111111111 ' + str(datetime.datetime.now()))
# print(dist2)


# temp = point.pop(0)
# dist1 = MAXDIST
# start = datetime.datetime.now()
# for i in range(len(point)):
#     dist1 = min(dist1,sum((point[i] - temp)**2 )**0.5)
# end = datetime.datetime.now()
# print(dist1)
# print(end-start)
#
# kdtree.delete(temp)
# start = datetime.datetime.now()
# dist2 = kdtree.findnearest(temp)[0]
# end = datetime.datetime.now()
# print(dist2)
# print(end-start)
# temp = point.pop(0)
for epoh in range(10):
    # if epoh % 10 == 0:
    print(epoh)
    temp = np.array([random.random() for j in range(DIM)])
    dist1 = MAXDIST
    # start = datetime.datetime.now()
    start = time.time()
    for i in range(len(point)):
        dist1 = min(dist1,sum((point[i] - temp)**2 )**0.5)
    end = time.time()
    # print(dist1)
    print(end-start)

    # kdtree.delete(temp)
    start = time.time()
    dist2 = kdtree.findnearest(temp)[0]
    end = time.time()
    # print(dist2)
    print(end-start)
    if dist2 != dist1:
        print(dist1)
        print(dist2)