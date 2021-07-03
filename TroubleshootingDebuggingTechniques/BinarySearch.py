def binary_search(list, key):
    """Returns the position of key in the list if found, -1 otherwise.

    List must be sorted.
    """
    left = 0
    right = len(list) - 1
    while left <= right:
        middle = (left + right) // 2

        if list[middle] == key:
            return middle
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return -1


myList = [12,45,78,95,123,135,1458,45646,65477]
#Sorted!!!!!!!!!!!!!
keyIs = 45646
index = binary_search(myList,keyIs)

print("The index is:",index)