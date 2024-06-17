def counting_sort(arr,max_number):
    '''Counting Sort is a non-comparison-based sorting algorithm that counts the occurrences of each element in the list. It then uses this count to place the elements in the correct position in the sorted list.

    Time Complexity: O(n + k), where k is the range of the input
    Space Complexity: O(n + k)
    Stability: Stable

    Inputs:
        arr : unsorted array
        max_number: the maximum number in the array

    Returns:
        sorted array
    '''

    # Count the frequency of each number in the array
    counter = [0 for i in range(max_number+1)]

    for val in arr:
        counter[val]+=1


    # Fill the array with numbers in ascending order     
    i=0
    for val,cnt in enumerate(counter):
        arr[i:i+cnt] = [val]*cnt
        i=i+cnt

    return arr

if __name__=="__main__":
    arr = [0, 6, 1, 4, 1, 6, 0, 1, 2, 2, 1, 4, 2, 3, 4, 0, 3, 3, 3, 4]
    print(counting_sort(arr,max(arr)))


