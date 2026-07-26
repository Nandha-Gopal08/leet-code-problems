class node:
    def __init__ (self,data):
        self.data=data
        self.left=None
        self.right=None
def preorder(root):
    if root is None :
        return 
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)
def postorder(root):
    if root is None :
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")
def level_order(root):
    if root is None:
        return
    queue=[root]
    while(len(queue)):
        current=queue.pop(0)
        print(current.data,end=" ")
        if(current.left):
            queue.append(current.left)
        if(current.right):
            queue.append(current.right)
root = node(1)

root.left = node(2)
root.right = node(3)

root.left.left = node(4)
root.left.right = node(5)

root.right.left = node(6)
root.right.right = node(7)
print("\n preorder Traversal:")
preorder(root)
print("\n inorder traversal:")
inorder(root)
print("\n postorder Traversal:")
postorder(root)
print("\n level order traversa:")
level_order(root)
