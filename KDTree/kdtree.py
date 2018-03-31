import numpy as np


MAXDIST = 1e60
MINDIST = -1e60


class KDNode(object):
    def __init__(self, data, index):
        self.data = np.array(data)
        self.index = index
        self.right = None
        self.left = None


class KDTree(object):
    def __init__(self, dim):
        self.root = None
        self.dim = dim
        self.RectMax = np.array([MINDIST for i in range(dim)])
        self.RectMin = np.array([MAXDIST for i in range(dim)])

    def insert(self, data):
        self.root = self.insert_(self.root, data, 0, self.dim)

    def insert_(self, node, data, index, dim):
        if node == None:
            for i in range(self.dim):
                self.RectMax[i] = max(self.RectMax[i], data[i])
                self.RectMin[i] = min(self.RectMin[i], data[i])
            return KDNode(data, index)
        if data[node.index] < node.data[node.index]:
            node.left = self.insert_(node.left, data, (index + 1) % dim, dim)
        else:
            node.right = self.insert_(node.right, data, (index + 1) % dim, dim)
        return node

    def delete(self, data):
        self.root = self.delete_(self.root, np.array(data), 0, self.dim)
        for i in range(self.dim):
            self.RectMax[i] = self.findmax(self.root, 0, i, self.dim)[i]
            self.RectMin[i] = self.findmin(self.root, 0, i, self.dim)[i]

    def findmin(self, node, index, ind, dim):
        if index == ind:
            if node.left is None:
                return node.data
            else:
                return self.findmin(node.left, (index + 1) % dim, ind, dim)
        else:
            ans = node.data
            if node.left != None:
                d = self.findmin(node.left, (index + 1) % dim, ind, dim)
                if d[ind] < ans[ind]:
                    ans = d
            if node.right != None:
                d = self.findmin(node.right, (index + 1) % dim, ind, dim)
                if d[ind] < ans[ind]:
                    ans = d
            return ans

    def findmax(self, node, index, ind, dim):
        if index == ind:
            if node.right is None:
                return node.data
            else:
                return self.findmax(node.right, (index + 1) % dim, ind, dim)
        else:
            ans = node.data
            if node.left != None:
                d = self.findmax(node.left, (index + 1) % dim, ind, dim)
                if d[ind] > ans[ind]:
                    ans = d
            if node.right != None:
                d = self.findmax(node.right, (index + 1) % dim, ind, dim)
                if d[ind] > ans[ind]:
                    ans = d
            return ans

    def delete_(self, node, data, index, dim):
        if node is None:
            print('not found!')
            return None
        if (node.data == data).all():
            if node.right != None:
                node.data = self.findmin(node.right, (index + 1) % dim, index, dim)
                node.right = self.delete_(node.right, node.data, (index + 1) % dim, dim)
            elif node.left != None:
                node.data = self.findmin(node.left, (index + 1) % dim, index, dim)
                node.right = self.delete_(node.left, node.data, (index + 1) % dim, dim)
                node.left = None
            else:
                node = None
        elif data[index] < node.data[index]:
            node.left = self.delete_(node.left, data, (index + 1) % dim, dim)
        else:
            node.right = self.delete_(node.right, data, (index + 1) % dim, dim)
        return node

    def findnearest(self, data):
        self.bestdist = sum((self.root.data - data) ** 2)**0.5
        self.bestdata = self.root.data
        # RectMax = [ MAXDIST for i in range(self.dim)]
        # RectMin = [ MINDIST for i in range(self.dim)]
        self.findnearest_(self.root, data, 0, self.RectMin, self.RectMax, self.dim)
        # self.findnearest_(self.root, data, 0, RectMin, RectMax, self.dim)
        return self.bestdist, self.bestdata

    def getdist(self, data, RectMin, RectMax):
        sum = 0.0
        for i in range(len(RectMax)):
            if data[i] < RectMin[i]:
                sum += (data[i] - RectMin[i]) ** 2
            if data[i] > RectMax[i]:
                sum += (data[i] - RectMax[i]) ** 2

        return sum**0.5

    def findnearest_(self, node, data, index, RectMin, RectMax, dim):
        if (node == None) | (self.getdist(data, RectMin, RectMax) > self.bestdist):
            return
        dist = sum((data - node.data) ** 2)**0.5
        if dist < self.bestdist:
            self.bestdist = dist
            self.bestdata = node.data
        if data[index] < node.data[index]:
            temp = RectMax[index]
            RectMax[index] = node.data[index]
            self.findnearest_(node.left, data, (index + 1) % dim, RectMin, RectMax, dim)
            RectMax[index] = temp

            temp = RectMin[index]
            RectMin[index] = node.data[index]
            self.findnearest_(node.right, data, (index + 1) % dim, RectMin, RectMax, dim)
            RectMin[index] = temp
        else:
            temp = RectMin[index]
            RectMin[index] = node.data[index]
            self.findnearest_(node.right, data, (index + 1) % dim, RectMin, RectMax, dim)
            RectMin[index] = temp

            temp = RectMax[index]
            RectMax[index] = node.data[index]
            self.findnearest_(node.left, data, (index + 1) % dim, RectMin, RectMax, dim)
            RectMax[index] = temp


