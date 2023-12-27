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
