class Stack():
    def __init__(self, l):
        self.len = len(l)
        self.stack = l

    def push(self, x):
        self.stack.append(x)
        self.len += 1

    def pop(self):
        if self.len <= 0:
            raise ValueError('Cannot pop from an empty stack')
        res = self.stack[-1]
        self.stack = self.stack[:-1]
        self.len -= 1
        return res

    def top(self):
        return self.stack[-1]
