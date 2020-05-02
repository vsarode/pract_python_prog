class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        t_head = self.head
        if not t_head:
            t_head = Node(data)
        while t_head.next:
            t_head = t_head.next
        print(t_head.data)
        t_head.next = Node(data)

    def at_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print(self):
        val = self.head
        while val:
            print(val.data)
            val = val.next


if __name__ == '__main__':
    l1 = SLinkedList()
    l1.append(10)
    l1.append(20)
    l1.append(30)
    l1.append(40)
    l1.append(50)
    l1.print()
