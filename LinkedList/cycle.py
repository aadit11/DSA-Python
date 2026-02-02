class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


node1 = Node(20)
node2 = Node(30)
node3 = Node(40)
node4 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1


def hasCycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

print(hasCycle(head))