from typing import Any,Union

class MaxHeap():
    '''MaxHeap is a complete binary tree that satisfies the max-heap property. For every node i, the value of the node is greater than or equal to the values of its children
        Inputs:
            - arr : an array of numbers which may not have the heap property
    '''
    def __init__(self,arr :list):
        '''Heap Constructor
        '''
        self.arr = arr
        self.length = len(self.arr)
        self.build()

    def build(self):
        for i in range(self.length//2-1, -1, -1):
            self.heapify(i)

    def heapify(self,idx):

        '''This is a recursive function. Assume that subtrees on node i are maxHeap and try to keep the MaxHeap property at node i
        Inputs:
            i : the index of node that its subtrees are MaxHeap and we want to merge two subtrees with the parent
        '''

        parent_idx,  parent_val = idx , self.arr[idx]
        left_child_idx, left_child_val = self.left_child(parent_idx)
        right_child_idx, right_child_val = self.right_child(parent_idx)

        if right_child_val and right_child_val>parent_val:
            max_idx = right_child_idx
            max_val = right_child_val

        else:
            max_idx = parent_idx
            max_val = parent_val

        if left_child_val and left_child_val>max_val:
            max_idx = left_child_idx
            max_val = left_child_val

        if max_idx == parent_idx:
            return

        elif max_idx == left_child_idx:
            self.arr[parent_idx],self.arr[left_child_idx]=self.arr[left_child_idx],self.arr[parent_idx]
            self.heapify(left_child_idx)
       
        elif max_idx == right_child_idx:
            self.arr[parent_idx],self.arr[right_child_idx]=self.arr[right_child_idx],self.arr[parent_idx]
            self.heapify(right_child_idx)
    
    def heaify_parents(self,idx):      
        # now we need to check if the parent still keep the heam property
        parent_idx , parent_val = self.parent(idx)

        while parent_idx is not None  and self[idx] > parent_val:
            self[idx] , self[parent_idx] =  self[parent_idx] ,self[idx] 
            self.heapify(parent_idx)
            idx = parent_idx


            parent_idx , parent_val = self.parent(idx)

    def edit(self, idx , new_val):
        if idx>self.length:
            raise ValueError('index is out of range')
        
        if new_val < self[idx]:
            self[idx] = new_val
            self.heapify(idx)
        
        if new_val > self[idx]:
            self[idx] = new_val
            self.heaify_parents(idx)

        if new_val == self[idx]: # No change
            return

    def sort(self):
        # we know the first element in MaxHeap is the maximum element.
        # So using a for loop with reverse counter (i from n to 0) we repeatedly get the maximum `arr[0]` and exchange it with `arr[i]`
        for i in range(len(self.arr)-1,0 ,-1):
            self.arr[i],self.arr[0] = self.arr[0],self.arr[i]

            # after replacing we remove the last element from the heap by reducing the heap length.
            self.length -=1

            # finally we heapify the heap to make sure self.arr keep the MaxHeap property
            self.heapify(0)
            
        return self.arr

    def left_child(self,i):
        '''This method return the index and value of the left child for node i. if there is no left child return None'''
        return (2*i+1,self.arr[2*i+1]) if 2*i+1<self.length else (None,None)

    def right_child(self,i):
        '''This method return the index and value of the right child for node i. if there is no right child return None'''
        return (2*i+2,self.arr[2*i+2]) if 2*i+2<self.length else (None,None)
        
    def parent(self,i):
        '''This method return the index and value of the parent for node i. if there is no parent return None'''
        return ((i-1)//2, self.arr[(i-1)//2]) if i>0 else (None,None)


    def __getitem__(self,idx):
        return self.arr[idx]

    def __setitem__(self,idx,val):
        self.arr[idx] = val

    def push(self,val):
        self.arr.append(val)
        self.length+=1

    def pop(self):
        assert self.length>0, 'No value to pop'
        root = self.arr[0]
        if self.length==1: # single element heap
            self.arr=[]
            self.length-=1
        else:
            self.arr[0]= self.arr.pop(self.length-1)
            self.length-=1
            self.heapify(0)
        return root

    def __str__(self):
        return f'{self.__class__.__name__}({self.arr})'
    
def heapsort(arr:list)->list :
    heap = MaxHeap(arr)
    return heap.sort()




class MinHeap():
    '''MinHeap is a complete binary tree that satisfies the min-heap property. For every node i, the value of the node is less than or equal to the values of its children
        Inputs:
            - arr : an array of numbers which may not have the heap property
    '''
    def __init__(self,arr :list):
        '''Heap Constructor
        '''
        self.arr = arr
        self.length = len(self.arr)
        self.build()

    def build(self):
        for i in range(self.length//2-1, -1, -1):
            self.heapify(i)

    def heapify(self,idx):

        '''This is a recursive function. Assume that subtrees on node i are maxHeap and try to keep the MaxHeap property at node i
        Inputs:
            i : the index of node that its subtrees are MaxHeap and we want to merge two subtrees with the parent
        '''

        parent_idx,  parent_val = idx , self.arr[idx]
        left_child_idx, left_child_val = self.left_child(parent_idx)
        right_child_idx, right_child_val = self.right_child(parent_idx)

        if right_child_val and right_child_val<parent_val:
            min_idx = right_child_idx
            min_val = right_child_val

        else:
            min_idx = parent_idx
            min_val = parent_val

        if left_child_val and left_child_val<min_val:
            min_idx = left_child_idx
            min_val = left_child_val

        if min_idx == parent_idx:
            return

        elif min_idx == left_child_idx:
            self.arr[parent_idx],self.arr[left_child_idx]=self.arr[left_child_idx],self.arr[parent_idx]
            self.heapify(left_child_idx)
       
        elif min_idx == right_child_idx:
            self.arr[parent_idx],self.arr[right_child_idx]=self.arr[right_child_idx],self.arr[parent_idx]
            self.heapify(right_child_idx)
    


    def edit(self, idx , new_val):
        if idx>self.length:
            raise ValueError('index is out of range')
        
        if new_val < self[idx]:
            self[idx] = new_val
            self.heaify_parents(idx)
            
        
        if new_val > self[idx]:
            self[idx] = new_val
            self.heapify(idx)

        if new_val == self[idx]: # No change
            return


    def heaify_parents(self,idx):      
        # now we need to check if the parent still keep the heam property
        parent_idx , parent_val = self.parent(idx)

        while parent_idx is not None  and self[idx] < parent_val:
            self[idx] , self[parent_idx] =  self[parent_idx] ,self[idx] 
            self.heap.heapify(parent_idx)
            idx = parent_idx
            parent_idx , parent_val = self.parent(idx)


    def sort(self):
        # we know the first element in MaxHeap is the maximum element.
        # So using a for loop with reverse counter (i from n to 0) we repeatedly get the maximum `arr[0]` and exchange it with `arr[i]`
        for i in range(len(self.arr)-1,0 ,-1):
            self.arr[i],self.arr[0] = self.arr[0],self.arr[i]

            # after replacing we remove the last element from the heap by reducing the heap length.
            self.length -=1

            # finally we heapify the heap to make sure self.arr keep the MaxHeap property
            self.heapify(0)
            
        return self.arr

    def left_child(self,i):
        '''This method return the index and value of the left child for node i. if there is no left child return None'''
        return (2*i+1,self.arr[2*i+1]) if 2*i+1<self.length else (None,None)

    def right_child(self,i):
        '''This method return the index and value of the right child for node i. if there is no right child return None'''
        return (2*i+2,self.arr[2*i+2]) if 2*i+2<self.length else (None,None)
        
    def parent(self,i):
        '''This method return the index and value of the parent for node i. if there is no parent return None'''
        return ((i-1)//2, self.arr[(i-1)//2]) if i>0 else (None,None)


    def __getitem__(self,idx):
        return self.arr[idx]

    def __setitem__(self,idx,val):
        self.arr[idx] = val

    def push(self,val):
        self.arr.append(val)
        self.length+=1

    def pop(self):
        assert self.length>0, 'No value to pop'
        root = self.arr[0]
        if self.length==1: # single element heap
            self.arr=[]
            self.length-=1
        else:
            self.arr[0]= self.arr.pop(self.length-1)
            self.length-=1
            self.heapify(0)
        return root

    def __str__(self):
        return f'{self.__class__.__name__}({self.arr})'
    
def heap_sort(arr:list,order)->list :
    if order =='asc':
        heap = MinHeap(arr)
    elif order == 'desc':
        heap = MaxHeap(arr)

    return heap.sort()


if __name__ == '__main__':
    print(heap_sort([4,1,3,2,16,9,10,14,8,7],'asc'))
    print(heap_sort([4,1,3,2,16,9,10,14,8,7],'desc'))