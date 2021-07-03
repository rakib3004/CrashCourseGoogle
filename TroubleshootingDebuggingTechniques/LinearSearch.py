def linear_search(list, key):
    """If key is in the list returns its position in the list,
       otherwise returns -1."""
    for i, item in enumerate(list):
        if item == key:
            return i
    return -1



myList=[1,5,15,54,7,8,15,45,4,5,454,8,4,84,84,854,8,748,46,56,12,8,7,32,2,361,54]

index=linear_search(myList,8)
print("Find value in",index,'position')