def bubble_sort(arr:list)->list:
    '''Bubble Sort is a simple comparison-based sorting algorithm. It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process is repeated until the list is sorted.

    Time Complexity: O(n^2)
    Space Complexity: O(1)
    Stability: Stable

    Input:
        arr : unsorted list

    Return:
        sorted list in ascending order
    '''

    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
    
    return arr

if __name__=="__main__":
    print(bubble_sort)
    arr = [22, 16, 6, 44, 30, 32, 38, 24, 5, 12, 26, 50, 3, 13, 23, 7, 17, 49, 19, 0]

    print(bubble_sort(arr))
