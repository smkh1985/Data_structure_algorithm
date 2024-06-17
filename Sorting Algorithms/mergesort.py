def mergesort(arr:list)->list :
    '''Merge Sort is a divide-and-conquer algorithm that divides the list into two halves, recursively sorts each half, and then merges the sorted halves to produce the sorted list.

        Time Complexity: O(n log n)
        Space Complexity: O(n)
        Stability: Stable

        Inputs:
            arr : unsorted array

        Returns:
            sorted array
    '''

    if len(arr)==1: # single element array is sorted inherently
        return arr
    
    else:

        # Divide the array into two half
        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        # sort the right subarray
        right_sorted = mergesort(right_arr)
        
        # sort the left subarray
        left_sorted = mergesort(left_arr)

        # Combine two subarrays
        sorted_arr = []  # this empty array shows that merge sort is not inplace sort.
        right_idx = 0
        left_idx = 0

        min_length = min(len(right_sorted), len(left_sorted))
        while right_idx<min_length and left_idx<min_length:
            if right_sorted[right_idx]<left_sorted[left_idx]:
                sorted_arr.append(right_sorted[right_idx])
                right_idx+=1
            else:
                sorted_arr.append(left_sorted[left_idx])
                left_idx+=1


        sorted_arr.extend(right_sorted[right_idx:])
        sorted_arr.extend(left_sorted[left_idx:])

        return sorted_arr

if __name__=="__main__":
    arr = [22, 16, 6, 44, 30, 32, 38, 24, 5, 12, 26, 50, 3, 13, 23, 7, 17, 49, 19, 0]

    print(mergesort(arr))
