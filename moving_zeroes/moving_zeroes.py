'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    zeros = []
    others= []
    for i in range(0, len(arr)):
        if arr[i] == 0:
            zeros.append(arr[i])
        else:
            others.append(arr[i])
    if len(zeros) == 0:
        return others

    result = others + zeros
    print(result)
    return result


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

arr1 = [0, 3, 1, 0, -2]
moving_zeroes(arr1)
