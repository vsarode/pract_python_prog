"""
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ls1 = []
        ls2 = []
        while l1.next:
            ls1.append(str(l1.val))
            l1 = l1.next
        ls1.append(str(l1.val))

        while l2.next:
            ls2.append(str(l2.val))
            l2 = l2.next
        ls2.append(str(l2.val))

        ls1.reverse()
        ls2.reverse()
        result = int(''.join(ls2)) + int(''.join(ls1))
        head = ListNode(str(result)[-1])
        res = head
        for i in str(result)[:-1][::-1]:
                next_node = ListNode(i)
                res.next = next_node
                res=next_node
        return head


if __name__ == '__main__':
    n1 = ListNode(2)
    n2 = ListNode(4)
    n3 = ListNode(3)

    n11 = ListNode(5)
    n22 = ListNode(6)
    n33 = ListNode(4)

    n1.next=n2
    n2.next=n3

    n11.next=n22
    n22.next=n33
    o = Solution()
    res = o.addTwoNumbers(n1, n11)
    print("out")
    print(res.val)
    print(res.next.val)
    while res.next:
        print(res.val)
        res=res.next
    print(res.val)



    # n1.next = n2
    # n2.next = n3
    #
    # print(n1.val)
    # print(n1.next.val)
    # print(n1.next.next.val)
