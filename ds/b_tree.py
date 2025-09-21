class Node:
    def __init__(self,degree,is_leaf) -> None:
        self.degree = degree
        self.is_leaf = is_leaf
        self.keys = []
        self.children = []


    def is_full(self): return len(self.keys) >= 2 * self.degree - 1 


    # 1 2 3 4 9
    def split_child(self,index,child):
        new_child = Node(self.degree,child.is_leaf)
        new_child.keys = child.keys[self.degree:]
        if not child.is_leaf:
            new_child.children = child.children[self.degree:]


        child.keys = child.keys[:self.degree]
        child.children[:self.degree]

        self.keys.insert(index,child.keys.pop(-1))
        self.children.insert(index+1,new_child)
    def search(self,data):
            i = 0
            while i < len(self.keys) and data > self.keys[i]:
                i+=1


            if i < len(self.keys) and self.keys[i] == data:
                return self
            
            if self.is_leaf:
                return None

            return self.children[i].search(data)
    

    def insert_non_full(self,data):
        len_keys = len(self.keys)
        if self.is_leaf:
            curr_index = len_keys - 1
            # 1 2 3 5
            self.keys.append(None)
            while curr_index >= 0 and data < self.keys[curr_index]:
                self.keys[curr_index+1] = self.keys[curr_index] 
                curr_index-=1

            self.keys[curr_index+1] = data
        else:
            curr_index = len_keys - 1
            while curr_index >= 0 and data < self.keys[curr_index]:
                curr_index-=1
            curr_index += 1

            if self.children[curr_index].is_full():
                pass
            self.children[curr_index].insert_non_full(data)


class B_Tree:
    def __init__(self,degree) -> None:
        self.root = None
        self.degree = degree


    def insert(self,data):
        if self.root == None:
            self.root = Node(self.degree,True)
            self.root.keys.append(data)
        else:
            if self.root.is_full():
                new_root = Node(self.degree,False)
                new_root.children.append(self.root)
                new_root.split_child(0,self.root)

                i=0
                if new_root.keys[0] < data:
                    i+=1
                new_root.children[i].insert_non_full(data)
                self.root = new_root

            else:
                self.root.insert_non_full(data)


    def search(self,data):
        return None if self.root is None else self.root.search(data)
        



if __name__ == "__main__":
    btree = B_Tree(3)
    #     2
    # 3 1 4 9 10
   
    #     x
    # 1 2 3 4 9

    btree.insert(2)
    btree.insert(3)
    btree.insert(1)
    btree.insert(4)
    btree.insert(9)
    print(btree.root.keys)
    print(btree.root.keys[3:])
    print(btree.root.keys[:2])
    btree.insert(10)
    print(btree.root.children[0].keys)
    print(btree.root.keys)
    print(btree.search(10).keys)
