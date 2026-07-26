class node:
    def __init__ (self,data):
        self.data=data
        self.left=None
        self.right=None
def level_order(root):
    if root is None:
        return
    queue=[root]
    while(len(queue)):
        current=queue.pop(0)
        print(current.data)
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
print("\n level order traversa:")
level_order(root)
