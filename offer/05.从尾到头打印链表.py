class Node:
    def __init__(self, data, next=None):
        self.value = data
        self.next = next


class Chain:
    def __init__(self, head=None):
        self.head = head

    def append(self, node):
        if not self.head:
            self.head = node
        else:
            temp_node = self.head
            while temp_node.next:
                temp_node = temp_node.next
            temp_node.next = node


def PrintListReversingly_Iteratively(head):
    stack = []
    while head:
        stack.append(head.value)
        head = head.next
    print(stack[::-1])


# 既然想到了用栈来实现这个函数，而递归在本质上就是一个栈结构，于是很自然地又想到了用递归来实现
def PrintListReversingly_Recursively(head):
    if head:
        PrintListReversingly_Recursively(head.next)
        print(head.value, end=' ')


if __name__ == '__main__':
    array = Chain()
    array.append(Node(4))
    array.append(Node(5))
    array.append(Node(3))
    print(array.head.value)
    PrintListReversingly_Iteratively(array.head)
    PrintListReversingly_Recursively(array.head)
