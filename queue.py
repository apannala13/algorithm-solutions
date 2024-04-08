"""
Simple Queue implementation using two stacks.

Since queues follow FIFO principles and stacks follow LIFO,
the stack just needs to be inversed in order to display the characteristics of a queue.

"""
class Queue:
    def __init__(self):
        self.instack = []  #append objects to this stack
        self.outstack = []  #this stack will server as inverse of instack

    def __len__(self) -> int:
        return len(self.instack) + len(self.outstack)

    def put(self, obj:int) -> None:
        if obj not in self.instack: ##want unique elements in this case
            self.instack.append(obj)
            

    def get(self) -> int:
        if not self.outstack: #if outstack is empty
            self.outstack = self.instack[::-1] #invert stack
            self.instack = [] #empty to accept new elements without affecting cur queue order
        return self.outstack.pop()

if __name__ == "__main__":
    q = Queue()
    q.put(4)
    q.put(5)
    q.put(1)
    print(q.get())
    print(q.get())
    print(len(q))
    
    
