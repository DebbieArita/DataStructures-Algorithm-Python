"""
array = [7, 10, 12, 7, 9, 14]
maxSum = 7+12+14 = 33


"""
#Solution1 - 0(n) time / 0(n) space
def max_subset_sum_no_adjacent(arr):
    if not len(arr):
        return 0
    elif len(arr) == 1:
        return arr[0]
    maxSum = arr[:]
    maxSum[1] = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        maxSum[i] = max(maxSum[i-1], maxSum[i-2] + arr[i])
    return maxSum[-1]

#Solution2 - 0(n) time / 0(1) space
def max_subset_sum_no_adjacent(arr):
    if not len(arr):
        return
    elif len(arr) == 1:
        return arr[0]
    second = arr[0]
    first = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        current = max(first, second + arr[i])
        second = first
        first = current
    return first

#Solution3 - 0(n) time / 0(1) space
def max_subset_sum_no_adjacent(array):
    if not array:
        return 0
    if len(array) == 1:
        return array[0]

    # dp[i] = max sum up to index i without adjacent picks
    first = array[0]
    second = max(array[0], array[1])

    for i in range(2, len(array)):
        current = max(second, first + array[i])
        first = second
        second = current

    return second


array = [7, 10, 12, 7, 9, 14]
print(max_subset_sum_no_adjacent(array))
#print(max_subset_sum_no_adjacent(arr))