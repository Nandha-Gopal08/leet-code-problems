class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next


def printList(head):
    temp = head

    while temp is not None:
        print(temp.val, end=" ")
        temp = temp.next

    print()



head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(1)
head.next.next.next = ListNode(9)

node = head.next

print("Before deleting:")
printList(head)

deleteNode(node)

print("After deleting:")
printList(head)
