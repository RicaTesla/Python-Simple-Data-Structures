class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)


stack = Stack()
print("Is the stack empty?", stack.is_empty())
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack size:", stack.size())
print("Peeked item:", stack.peek())
print("Popped item:", stack.pop())

# Checking the size of the stack after popping
print("Stack size:", stack.size())

# Pushing another item onto the stack
stack.push(4)

# Checking the size of the stack after popping
print("Stack size:", stack.size())