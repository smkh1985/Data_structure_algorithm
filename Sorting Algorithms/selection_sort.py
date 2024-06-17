def selection_sort(arr:list)->list:
    '''Selection Sort divides the list into a sorted and an unsorted region. It repeatedly selects the smallest (or largest) element from the unsorted region and moves it to the end of the sorted region.

Time Complexity: O(n^2)

Space Complexity: O(1)

Stability: Not stable

        Inputs:
            arr : unsorted array

        Returns:
            sorted array
    '''
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[i]:
                min_idx = j

        arr[i],arr[min_idx] = arr[min_idx],arr[i]

    return arr


if __name__=="__main__":
    arr = [22, 16, 6, 44, 30, 32, 38, 24, 5, 12, 26, 50, 3, 13, 23, 7, 17, 49, 19, 0]

    print(selection_sort(arr))
