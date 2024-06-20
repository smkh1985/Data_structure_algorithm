from linked_list import SinglyLinkedList


class Queue_LinkedList():
    def __init__(self):

        self.queue = SinglyLinkedList()



    def enqueue(self,val):
        self.queue.add_last(val)

    def dequeue(self):

        val = self.queue.remove_first()
        if val:
            return val
        else:

            raise ValueError("Queue is empty")

    def __str__(self):

        return f'{self.queue}'


    def is_empty(self):

        return self.queue.length==0

    def first(self):

        top = self.queue.head
        if top:
            return top.val
        else:

            raise ValueError("Stack is empty") 


if __name__=='__main__':
    q = Queue_LinkedList()
    q.enqueue(5)
    print(q)
    q.enqueue(10)
    print(q)
    v = q.dequeue()
    print(v)
    print(q)

    q.enqueue(5)
    print(q)
    q.enqueue(25)
    print(q)
    v = q.dequeue()
    print(v)
    print(q)
    v = q.dequeue()
    print(v)
    print(q)
    v = q.dequeue()
    print(v)
    print(q)
    v = q.dequeue()
    print(v)
    print(q)