#This is a merge sort algorith implementation in python.


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        # Recursively sort the left and right havlves

        merge_sort(left)
        merge_sort(right)

        # Merge the sorted havlves
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right [j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy remaining elements of left half if any
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Copy remaining elements of right half if any
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


# Example usage 
arr = [8, 3, 5, 9, 1, 4, 6, 7, 2]
print("Unsorted array: ", arr)
merge_sort(arr)
print("Sorted array: ", arr)

        
