#Linear search function in python
#This function will look for an item in a list

def linearSearch(item, listItem):
    found = False
    position = 0
    while position < len(listItem) and not found:
        if listItem[position] == item:
            found = True
        position = position + 1
    return found
    
if __name__ == "__main__":
    shopping = ["apples", "bananas", "chocolate", "pasta"]
    item = raw_input("What item do you want to find? ")
    isFound = linearSearch(item, shopping)
    if isFound:
        print("Your item is in the list!")
    else:
        print("Your item is not in the list!")
    