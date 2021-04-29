class MyStack:
    queue = None
    count = 0

    def __init__(self):
        """
        Initialize your data structure here.
        """
        MyStack.queue = []
        MyStack.count = 0

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        MyStack.queue.append(x)
        MyStack.count += 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        for i in range(MyStack.count -1):
            MyStack.queue.append(MyStack.queue.pop(0))
        result = MyStack.queue.pop(0)
        MyStack.count -= 1
        return result
    def top(self) -> int:
        """
        Get the top element.
        """
        if MyStack.count == 0:
            return -1
        for i in range(MyStack.count -1):
            MyStack.queue.append(MyStack.queue.pop(0))
        result = MyStack.queue[0]
        MyStack.queue.append(MyStack.queue.pop(0))
        MyStack.count -= 1
        return result

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if MyStack.count == 0 :
            return True
        else:
            return False

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(2)
obj.push(3)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()