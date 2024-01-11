def mergeSort(arr):

    if len(arr) > 1:
        mid = len(arr) // 2
        subarray1 = arr[:mid]
        subarray2 = arr[mid:]

        mergeSort(subarray1)
        mergeSort(subarray2)

        # pointers to start with

        i = j = k = 0

        while i < len(subarray1) and j < len(subarray2):
            if subarray1[i] < subarray2[j]:
                arr[k] = subarray1[i]
                i += 1

            else:
                arr[k] = subarray2[j]
                j += 1

            k += 1

        while i < len(subarray1):
            arr[k] = subarray1[i]
            i += 1
            k += 1

        while j < len(subarray2):
            arr[k] = subarray2[j]
            j += 1
            k += 1

        # Example usage
            
arr = [9,2,5,1,11,3,19,7,20,8,4,6]
mergeSort(arr)
print(arr)



