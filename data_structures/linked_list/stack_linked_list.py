from linked_list import SinglyLinkedList

class Stack_LinkedList():
    def __init__(self):
        self.stack = SinglyLinkedList()


    def push(self,val):
        self.stack.add_first(val)

    def pop(self):
        val = self.stack.remove_first()
        if val:
            return val
        else:
            raise ValueError("Stack is empty")

    def __str__(self):
        return f'{self.stack}'

    def is_empty(self):
        return self.stack.length==0

    def top(self):
        top = self.stack.head
        if top:
            return top.val
        else:
            raise ValueError("Stack is empty") 

if __name__=='__main__':
    l = Stack_LinkedList()
    l.push(5)
    print(l)
    l.push(10)
    print(l)
    v = l.pop()
    print(v)
    print(l)

    l.push(5)
    print(l)
    l.push(25)
    print(l)
    v = l.pop()
    print(v)
    print(l)
    v = l.pop()
    print(v)
    print(l)
    v = l.pop()
    print(v)
    print(l)
    v = l.pop()
    print(v)
    print(l)