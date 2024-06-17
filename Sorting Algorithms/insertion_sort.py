def insertion_sort(arr:list)->list:
    '''Insertion Sort builds the final sorted array one item at a time. It takes each element from the input data and inserts it into the correct position in the sorted list.
        -Time Complexity: O(n^2)
        -Space Complexity: O(1)
        -Stability: Stable

        Inputs:
            arr : unsorted array

        Returns:
            sorted array
    '''

    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j] = arr[j],arr[i]

    return arr


if __name__=="__main__":
    arr = [22, 16, 6, 44, 30, 32, 38, 24, 5, 12, 26, 50, 3, 13, 23, 7, 17, 49, 19, 0]

    print(insertion_sort(arr))
