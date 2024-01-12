def mergSot(arr):
    if len(arr) > 1:

       mid = len(arr)//2
       patArray1 = arr[:mid]
       patArray2 = arr[mid:]

       mergSot(patArray1)
       mergSot(patArray2)


       # 



