def recursive_binary_search(arr:list,key,low:int,high:int):
    ''' Recursive implementation of binary search algorithm
    Input:
        arr : a list of numbers
        key : a number that you are looking for in the arr
        low : low index for search range
        high : high index for search range

    Return:
        Index of the key if key is in the list, otherwise -1

    '''

    if low>high:
        return -1
    mid = (low+high)//2
    
    if arr[mid]==key:
        return mid
    elif arr[mid]>key:
        return recursive_binary_search(arr,key,low,mid-1)
    elif arr[mid]<key:
        return recursive_binary_search(arr,key,mid+1,high)

if __name__=="__main__":
    arr = [1,3,6,17,19,32,45,67,68,73,75,79,82]
    key = 82
    print(binary_search_recursive(arr,key,0,len(arr)-1))