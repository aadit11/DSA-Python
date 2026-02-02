class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def intersect(head1, head2):
    if not head1 or not head2:
        return None


    p1 = head1
    p2 = head2

    while p1 != p2:
        p1 = p1.next if p1 else head2
        p2 = p2.next if p2 else head1

    return p1


common = Node(8)
common2 = Node(9)


a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a4 = common
a5 = common2
head = a1
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
a5.next = None

b1 = Node(4)
b2 = Node(5)
b3 = common
b4 = common2
head2 = b1
b1.next = b2
b2.next = b3
b3.next = b4
b4.next = None

result = intersect(head, head2)
print(result.data)