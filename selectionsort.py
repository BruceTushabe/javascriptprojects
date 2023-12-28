def selectionSort(List):
    for i in range(len(List)):
        minimum = i
        for j in range(i + 1, len(List)):  # Compare i and i+1
            if(List[j] < List[minimum]):
                minimum = j
            if(minimum != i):
                List[i], List[minimum] = List[minimum], List[i]
        return List
    
if __name__ == "__main__":
    List = [4,6,5,7,2,3,8,9,1]
    print("Selected List: ", selectionSort(List))



# Selection Sort in Python
# Time complexity 0(n*2)
# Sorting by finding the minimum idex

def selectSort (array, size):

    for ind in range(size):
        minIndex = ind

        for j in range (ind + 1, size):

            # select the minimum element in every iteration

            if array[j] < array[minIndex]:
                minIndex = j

            # swapping the elements to sort the array
        (array[ind], array[minIndex]) = (array[minIndex], array[ind])

# Driver code to test above
        
arr = [4,6,5,7,2,3,8,9,1]
size = len(arr)
selectSort(arr, size)
print( " Sorted array is: ", arr)