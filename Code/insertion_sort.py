#!/usr/bin/python3
# Created by Sam Ebison ( https://github.com/ebsa491 )
# If you have found any important bug or vulnerability,
# contact me pls ( email: ebsa491@gmail.com )

def main():

    array = [5, 7, 3, 9, 1, 2, 5]
    sorting(array)

    for element in array:
        print(f"{element}")

def sorting(array):
    """
    This function sorts the array (insertion sort).
    :param array: The array that you want to sort.
    """
    for i in range(1, len(array)):

        key = array[i]

        j = i - 1

        while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1

        array[j + 1] = key

if __name__ == '__main__':
    main()
  