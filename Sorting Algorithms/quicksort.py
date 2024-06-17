def quicksort(arr:list)->list :
    '''Quick Sort is a divide-and-conquer algorithm that selects a 'pivot' element and partitions the array into elements less than the pivot and elements greater than the pivot. The partitions are then recursively sorted.

    Time Complexity: O(n log n) on average, O(n^2) in the worst case
    Space Complexity: O(log n)
    Stability: Not stable

    Inputs:
    arr : unsorted array

    Returns:
        sorted array
    '''

    
    if len(arr)<=1: # single element array is sorted inherently
        return arr
    
    else:
        #assume pivot is last element
        pivot = arr[-1]

        # Find the position of the pivot

        # assume pivot location is first location
        final_pivot_idx = 0

        # compare all elements with pivot value and if they are less than pivot, swap values and push pivot location forward
        for j in range(len(arr)-1):
            if arr[j]<pivot:
                arr[j],arr[final_pivot_idx] = arr[final_pivot_idx],arr[j]
                final_pivot_idx+=1

        arr[final_pivot_idx],arr[-1] = arr[-1],arr[final_pivot_idx]
        
        # print(arr[:final_pivot_idx], pivot , arr[final_pivot_idx+1:])

        # sort the right subarray
        right_sorted = quicksort(arr[:final_pivot_idx])
        
        # sort the left subarray
        left_sorted = quicksort(arr[final_pivot_idx+1:])

        # Combine two subarrays
        sorted_arr = right_sorted + [pivot] + left_sorted  # this empty array shows that merge sort is not inplace sort.
        
        return sorted_arr


if __name__=="__main__":
    arr = [22, 16, 6, 44, 30, 32, 38, 24, 5, 12, 0, 50, 3, 13, 23, 7, 17, 49, 19, 26]

    print(quicksort(arr))
