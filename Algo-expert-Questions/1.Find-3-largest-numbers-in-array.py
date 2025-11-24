# Find the three largest numbers in an array of numbers
# Binary search
"""
Array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
Answer = [18, 141, 541]

keep track and store the 3 largest numbers... as you traverse through the array...
Declare empty array of len=3
[_ , _, 141 ]
[_, 1, 141 ]
[1, 17, 141 ]
[17, 18, 141 ]
[18, 141, 541 ] ..... (for example...)
Time = 0(n) -> size of array
Space = 0(1) -> constant space
"""

def find_three_largest_numbers(array):
    three_largest_numbers = [None, None, None]
    for num in array:
        update_largest(three_largest_numbers, num)
    return three_largest_numbers

#compare the current number to the 3rd value - replace the largest number...
def update_largest(three_largest_numbers, num):
    if three_largest_numbers[2] is None or num > three_largest_numbers[2]:
        shift_and_update(three_largest_numbers, num, 2)
    elif three_largest_numbers[1] is None or num > three_largest_numbers[1]:
        shift_and_update(three_largest_numbers, num, 1)
    elif three_largest_numbers[0] is None or num > three_largest_numbers[0]:
        shift_and_update(three_largest_numbers, num, 0)

def shift_and_update(array, num, idx):
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i + 1]

array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
print(find_three_largest_numbers(array))
