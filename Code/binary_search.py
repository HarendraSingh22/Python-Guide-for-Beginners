import random

def binary_search(numbers, num_to_find):
    min_num = 0
    max_num = len(numbers) - 1
    not_found = True
    in_list = True

    while not_found and in_list:
        mid = (max_num + min_num) // 2
        if max_num < min_num:
            in_list = False
        elif num_to_find > numbers[mid]:
            min_num = mid + 1
        elif num_to_find < numbers[mid]:
            max_num = mid - 1
        else:
            not_found = False
    
    return None if not_found else (max_num + min_num) // 2

if __name__ == "__main__":
    list_size = int(input("How big do you want the list to be: "))
    numbers = random.sample(range(list_size*10), list_size)
    numbers.sort()
    
    print("List: {}".format(numbers))

    num_to_find = int(input("What number do you want to find: "))

    result = binary_search(numbers, num_to_find)

    if result != None:
        print("The number {} is at index {}".format(num_to_find, result))
    else:
        print("The number {} is not in the list.".format(num_to_find))