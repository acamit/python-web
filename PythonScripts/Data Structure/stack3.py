class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    # String representation of the stack
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-2]

    def getsize(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def peek(self):
        if self.is_empty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Popping from an empty stack")

        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value


if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)

    print(f'Stack: {stack}')

    for _ in range(1, 6):
        removed = stack.pop()
        print(f'Pop: {removed}')

    print(f'Stack: {stack}')
