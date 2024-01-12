def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        partArray1 = arr[:mid]
        partArray2 = arr[mid:]

        mergeSort(partArray1)
        mergeSort(partArray2)

        i = j = k = 0

        while i < len(partArray1) and j < len(partArray2):
            if partArray1[i] < partArray2[j]:
                

