class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None


# a big helper in finding the kth ancestor
# it just maps the parents[i] to the parent of it where [i] is the Node.val
def find_parents(root,n):
    stack = []
    stack.append(root)
    parents = [-1] * (n+1)
    while stack:
        this_node = stack.pop()
        if this_node.left:
            parents[this_node.left.val] = this_node.val
            stack.append(this_node.left)
        if this_node.right: 
            parents[this_node.right.val] = this_node.val
            stack.append(this_node.right)
            
    return parents


def kth_ancestor(root,node,k,n):
    parents = find_parents(root,n)
    checked =1 
    curr = parents[node]
    # just to make sure that we have only gone once up and that k is exactly above 1 
    # so that we arent returning -1 prematurley
    if curr == -1 and k > 1:
        return -1 
    while checked < k:
        curr = parents[curr]
        checked+=1

    return curr

# the real subtree counter function 
# the subtree(root,node,n) is just a traverse to find the node which we want to find the subtree of 
def count_subvalue(root):
    l,r = 0,0
    if root.left:
        l = count_subvalue(root.left)
    if root.right: 
        r = count_subvalue(root.right)
    return l+r+root.val

def subtree(root,node,n):
    if root == None:
        return None
    if root.val != node:
        if root.left:
            left_res = subtree(root.left,node,n)
            if left_res != None : return left_res
        if root.right:
            right_res = subtree(root.right,node,n)
            if right_res != None: return right_res
    else:
        return count_subvalue(root)

   
def depth(root,n):
    depths=[0] * (n+1)
    stack = []
    stack.append((root,0))
    while stack:
        this_node,this_depth = stack.pop()
        depths[this_node.val] = this_depth 
        if this_node.left:
            stack.append((this_node.left,this_depth+1))
        if this_node.right:
            stack.append((this_node.right,this_depth+1))
    return depths

def lowest_common_ancestor(root,a,b):
    if root == None or root.val == a or root.val == b:
        # important point here is that 
        # we return root even though if the root is None meaning it will return None , so no flaw of logic here
        return root
    l = lowest_common_ancestor(root.left,a,b)
    r = lowest_common_ancestor(root.right,a,b)
    if l and r:
        return root
    return l or r


def distance_of_nodes(root,a,b,n):
    # a table of all the depths , depths[i] where i equal to Node.val
    depths = depth(root,n)
    # depth_a and depth_b 
    d_a,d_b = depths[a],depths[b]
    # lowest common ancesotr between a and b 
    lca = lowest_common_ancestor(root,a,b)
    # the depth of lca
    lca_depth = depths[lca.val]
    
    # the formula according to 170 of comp prog handbook 
    # depth_a + depth_b - 2 * depth_lca
    return (d_a+d_b)-(2*lca_depth)




"""
            1
        2       4
    3   5       6
        7

"""

root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right = Node(4)
root.right.right = Node(6)
root.left.right.right = Node(7)
LEN_OF_TREE = 7
#print(kth_ancestor(root,7,2,LEN_OF_TREE))
#print(subtree(root,2,LEN_OF_TREE))
print(distance_of_nodes(root,3,7,LEN_OF_TREE))
