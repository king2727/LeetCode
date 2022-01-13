import collections

class MyQueue(object):

    def __init__(self):
        self.stack = collections.deque([])

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        return self.stack.popleft()

    def peek(self):
        """
        :rtype: int
        """
        return self.stack[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

class MyQueue_stack(object):

    def __init__(self):
        self.stack = []
        self.stack2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        while len(self.stack) != 1:
            self.stack2.append(self.stack.pop())
        r = self.stack.pop()
        while self.stack2:
            self.stack.append(self.stack2.pop())
        return r


    def peek(self):
        """
        :rtype: int
        """
        return self.stack[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack) == 0