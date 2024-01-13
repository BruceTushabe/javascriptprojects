def mergSot(arr):
    if len(arr) > 1:

       mid = len(arr)//2
       patArray1 = arr[:mid]
       patArray2 = arr[mid:]

       mergSot(patArray1)
       mergSot(patArray2)


       # initial values for pointers

       i = j = k = 0
       
       while i < len(patArray1) and j < len(patArray2):
        if patArray1[i] < patArray2[j]:
            arr[k] = patArray1[i]
            i += 1
        else:
            arr[k] = patArray2[j]
            j += 1
        k += 1
           
    while i < len(patArray1):
        arr[k] = patArray1[i]
        i += 1
        k += 1
           
    while j < len(patArray2):
        arr[k] = patArray2[j]
        j += 1
        k += 1

# using
        
arr = [10, 9, 2, 4, 6, 13]
mergSot(arr)
print(arr)
           








