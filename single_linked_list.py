



class Node:
    def __init__(self, value):
        self.value = value
        self.next:Node = None
    def add(self, value):
        self.next = Node(value)



node1=Node(1)

node1.add(2)

node1.next.add(3)

node1.next.next.add(4)

node1.next.next.next.add(5)

node1.next.next.next.next.add(6)
node1.next.next.next.next.next.add(0)

node2=node1


def middle(node):
    count=0
    final = node
    while node.next:
        print(f"current = {node.value}\ncount={count}")
        if not count % 2 ==0:
            print(f"replace final with {node.value}")
            final = node
        count+=1
        node=node.next
        if not node.next:
            return final

def reverse_one_pass(node:Node):
    prev = None
    curr = list.head
    nex = curr.getNextNode()

    #looping
    while curr:
        #reversing the link
        curr.setNextNode(prev)

        #moving to next node
        prev = curr
        curr = nex
        if nex:
            nex = nex.getNextNode()

    #initializing head
    list.head = prev

def reverse_linked_list_three(node):
    current =node
    new =current.next
    current.next = None
    while current.next:
        prev =current
        current = new
        new = current.next
        current.next = prev
    return current


reverse =reverse_linked_list_three(node2)
while reverse.next:
     print(reverse.value)
     reverse=reverse.next
# print(middle(node2).value)
