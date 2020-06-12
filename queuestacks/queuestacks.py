class MyQueue(object):
    def __init__(self):
        self.stackOne = []
        self.stackTwo = []

    def push(self, x):
        self.stackOne.append(x)

    def pop(self):
        self.peek()
        return self.stackTwo.pop()

    def peek(self):
        if not self.stackTwo:
            while self.stackOne:
                self.stackTwo.append(self.stackOne.pop())
        return self.stackTwo[-1]

    def empty(self):
        return not self.stackOne and not self.stackTwo

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()