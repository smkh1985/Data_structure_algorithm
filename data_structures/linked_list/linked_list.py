class Node():
    def __init__(self,val,next= None):
        self.val = val
        self.next = next


class SinglyLinkedList():
    '''
    '''

    def __init__(self):
        self.head = None 
        self.tail = None
        self.length = 0

    def add_first(self,val):
        node = Node(val,self.head)
        if (self.length)==0:
            self.head = node
            self.tail = node
        else:
            self.head = node
        self.length+=1

    def add_last(self, val):
        node = Node(val,None)
        if (self.length)==0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        
        self.length+=1

    def remove_first(self):
        assert self.length>0, "There is no element in the empty linked list"
        node = self.head
        self.head = self.head.next
        self.length-=1
        return node.val
            
    def remove_last(self):
        '''
        Removing last element in the list. O(N)

        '''
        if self.length==0:
            return None
            
        if self.length==1:
            node = self.head
            self.head = None
            self.tail = None
            return node.val
        
        current = self.head
        while current.next.next:
            current=current.next
        
        node = current.next
        current.next = None
        self.tail = current
        self.length-=1
        return node.val




    def traverse(self):
        l = []
        if self.length==0:
            print('List is Empty!')
        current = self.head
        while current:
            l.append(current.val)
            current = current.next
        return ','.join([str(i) for i in l])

    def __str__(self):
        return self.traverse()
        
if __name__=='__main__':
    l = SinglyLinkedList()
    l.add_first(5)
    print(l)
    l.add_first(10)
    print(l)
    l.add_last(5)
    print(l)
    l.add_last(5)
    print(l)
    l.add_first(25)
    print(l)
    l.add_first(40)
    print(l)
    l.add_last(0)
    print(l)
    l.add_first(50)
    print(l)
    l.add_last(65)
    print(l)
    print(l.remove_first())
    print(l)
    print(l.remove_last())
    print(l)