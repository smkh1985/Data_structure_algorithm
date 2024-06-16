def binary_search(arr : list ,key) -> int:
    ''' Binary search algorithm
    Input:
        arr : a list of numbers
        key: a number that you are looking for in the arr

    Return:
        Index of the key if key is in the list, otherwise -1

    '''

    low = 0
    high = len(arr)-1
    ind = -1
    
    
    while low<=high:
        mid = (low+high)//2
        if arr[mid]== key :
            ind = mid
            break
        elif arr[mid]>key:
            high = mid-1
        elif arr[mid]<key:
            low = mid+1
    
    return ind

if __name__=="__main__":
    print(binary_search([1,3,6,17,19,32,45,67,68,73,75,79,82] ,67))

        