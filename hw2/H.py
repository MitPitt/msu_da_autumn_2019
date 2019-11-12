class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def children(self):
        return [i for i in [self.left, self.right] if i]

class BinarySearchTree:

    def __init__(self, value=None):
        if value is None:
            self.root = None
        else:
            self.root = Node(value)

    def __find(self,current,value):
        if current == None:
            return False
        elif current.value == value:
            return True
        elif(value < current.value):
            return self.__find(current.left, value)
        else:
            return self.__find(current.right, value)
    def __contains__(self, value):
        return self.__find(self.root,value)

    def __iter__(self):
        if self.root == None:
            raise StopIteration()
        thislevel = [self.root]
        while thislevel:
            nextlevel = []
            for i in thislevel:
                yield i.value
                for j in i.children():
                    nextlevel.append(j)
            thislevel = nextlevel

    def __append(self, current, value):
        if(value <= current.value):
            if(current.left):
                self.__append(current.left, value)
            else:
                current.left = Node(value)
        elif(value > current.value):
            if(current.right):
                self.__append(current.right, value)
            else:
                current.right = Node(value)
    def append(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.__append(self.root, value)


if __name__ == '__main__':

    tree = BinarySearchTree()
    for v in [8, 3, 10, 1, 6, 4, 14, 13, 7]:
        tree.append(v)
    for v in [8, 12, 13]:
        print(v in tree)
    print(*tree)

    tree = BinarySearchTree()
    for v in [5, 0, 6, 2, 1, 3]:
        tree.append(v)
    for v in [6, 12]:
        print(v in tree)
    print(*tree)

    tree = BinarySearchTree()
    for v in []:
        tree.append(v)
    for v in [6, 12]:
        print(v in tree)
    print(*tree)

