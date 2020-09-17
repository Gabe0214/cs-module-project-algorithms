'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    if k > len(nums):
        return max(nums)
    start = 0
    position_i = k
    results= []

    while start < len(nums):
        if len(nums[start:position_i]) == k:
            results.append(max(nums[start:position_i]))
            start += 1
            position_i += 1
        else:
            break
    return results


# if __name__ == '__main__':
#     # Use the main function here to test out your implementation
#     arr = [1, 3, -1, -3, 5, 3, 6, 7]
#     k = 3
#
#     print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

# sliding_window_max([1,2], 1)

arry1 = [1, 2, 13, 4, 21]
k = 5
position_i = k
start = 0
results = []
# while start < len(arry1):
#     if len(arry1[start:position_i]) == k:
#         results.append(max(arry1[start:position_i]))
#         start += 1
#         position_i += 1
#     else:
#         print(results)
#         break



sliding_window_max([1, 2, 13, 4, 21], 3)
