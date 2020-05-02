class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        t_head = self.head
        if not t_head:
            new_node = Node(data)
            new_node.prev = t_head
            self.head = new_node
            print("if", self.head.data)
        else:
            while t_head.next:
                t_head = t_head.next
            new_node = Node(data)
            t_head.next = new_node
            new_node.next=t_head
            print("else", self.new_node.data)

    def print(self):
        val = self.head
        while val:
            print(val.data)
            val = val.next


if __name__ == '__main__':
    dl = DLinkedList()
    dl.append(10)
    dl.append(20)
    dl.append(30)
    dl.append(40)
    dl.print()
