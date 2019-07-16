from queue import Queue

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.put(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        temp = None
        count = 0
        while not self.q1.empty():
            temp = self.q1.get()
            self.q2.put(temp)
            count += 1
        count -= 1
        while count:
            self.q1.put(self.q2.get())
            count -= 1
        self.q2.get()
        return temp

    def top(self) -> int:
        """
        Get the top element.
        """
        temp = None
        while not self.q1.empty():
            temp = self.q1.get()
            self.q2.put(temp)
        while not self.q2.empty():
            self.q1.put(self.q2.get())
        return temp

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.q1.empty()

obj = MyStack()
obj.push(1)
obj.push(2)
obj.top()
obj.pop()
obj.top()
obj.pop()
obj.empty()