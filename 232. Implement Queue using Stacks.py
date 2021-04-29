class MyQueue:

    stack1 = []
    stack2 = []
    count_1 = 0
    count_2 = 0

    def __init__(self):
        """
        Initialize your data structure here.
        """
        MyQueue.stack1 = []
        MyQueue.stack2 = []
        MyQueue.count_1 = 0
        MyQueue.count_2 = 0

    def push(self, x: int) -> None:
        MyQueue.stack1.append(x)
        MyQueue.count_1 += 1
        """
        Push element x to the back of queue.
        """

    def pop(self) -> int:
        result = -1
        if MyQueue.count_1 == 0 and MyQueue.count_2 == 0:
            return None
        if MyQueue.count_2 > 0:
            result = MyQueue.stack2.pop()
            MyQueue.count_2 -= 1
        else:
            while MyQueue.stack1:
                MyQueue.stack2.append(MyQueue.stack1.pop())
                MyQueue.count_1 -= 1
                MyQueue.count_2 += 1
            result = MyQueue.stack2.pop()
            MyQueue.count_2 -= 1
        return result
    def peek(self) -> int:
        result = -1
        if MyQueue.count_1 == 0 and MyQueue.count_2 == 0 :
            return None
        if MyQueue.count_2 > 0 :
            result = MyQueue.stack2[-1]
        else:
            while MyQueue.stack1:
                MyQueue.stack2.append(MyQueue.stack1.pop())

            result = MyQueue.stack2[-1]

        return result


        """
        Get the front element.
        """

    def empty(self) -> bool:
        if MyQueue.count_1 == 0 and MyQueue.count_2 == 0 :
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
param_3 = obj.peek()
print(param_3)
param_2 = obj.pop()
print(param_2)

param_4 = obj.empty()
print(param_4)