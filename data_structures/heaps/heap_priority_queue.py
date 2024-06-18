from typing import Any,Union
from heap import MaxHeap, MinHeap

class MaxPriorityQueue():
    '''MaxPriorityQueue


        Methods:
            - Push a value into Queue O(Log N)
            - Get maximum number (without removing)  O(1)
            - Pop maximum priority from queue  O(Log N)
            - increase priority for specific node O(Log N)

    '''

    def __init__(self):
        self.heap = MaxHeap([])

    def edit(self, idx , new_val):
        self.heap.edit(idx,new_val)


    def push(self,val:Union[int,float]) -> None :
        self.heap.push(-100000000)
        self.edit(self.heap.length-1, val)

    def root(self) -> Union[int,float]:
        return self.heap[0]

    def pop(self)->Union[int,float]:
        return self.heap.pop()

    def __str__(self):
        return f'{self.__class__.__name__} - {self.heap}'

class MinPriorityQueue():
    '''MinPriorityQueue


        Methods:
            - Push a value into Queue O(Log N)
            - Get maximum number (without removing)  O(1)
            - Pop maximum priority from queue  O(Log N)
            - increase priority for specific node O(Log N)

    '''

    def __init__(self):
        self.heap = MinHeap([])

    def edit(self,idx,new_val):
        self.heap.edit(idx,new_val)

    def push(self,val:Union[int,float]) -> None :
        self.heap.push(-100000000)
        self.edit(self.heap.length-1, val)
        

    def root(self) -> Union[int,float]:
        return self.heap[0]

    def pop(self)->Union[int,float]:
        return self.heap.pop()

    def __str__(self):
        return f'{self.__class__.__name__} - {self.heap}'

if __name__ == '__main__':
    priority = MaxPriorityQueue()
    print(priority)
    priority.push(10)
    print(priority)
    priority.push(20)
    print(priority)
    priority.push(5)
    print(priority)
    priority.push(15)
    print(priority)
    priority.push(25)
    print(priority)
    priority.push(17)
    print(priority)
    priority.edit(2,3)
    print(priority)
    priority.edit(3,12)
    print(priority)
    print('MAX:' , priority.root())
    print(priority.pop())
    print(priority.pop())
    print(priority.pop())
    print(priority.pop())
    print(priority.pop())
    print(priority.pop())