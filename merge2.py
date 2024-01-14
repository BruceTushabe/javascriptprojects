def magi(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        magi(lefthalf)
        magi(righthalf)

        i = j = k = 0

    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            arr[k] = lefthalf[i]
            i += 1
            k += 1

    while i < len(righthalf):
        arr[k] = lefthalf[i]
        i += 1
        k += 1

        # Copy remaining elements of right half if any
    while j < len(righthalf):
      arr[k] = righthalf[j]
      j += 1
      k += 1


# Example usage 
arr = [8, 3, 5, 9, 1, 4, 6, 7, 2]
print("Unsorted array: ", arr)
magi(arr)
print("Sorted array: ", arr)

        

