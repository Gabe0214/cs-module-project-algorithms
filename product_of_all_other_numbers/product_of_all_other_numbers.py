'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here
    #multiply all values from list execept the value on the current index

    result = []
    for i in range(0, len(arr)):
        prev = 1
        for j in range(0, len(arr)):
            if i != j:
                prev *= arr[j]



        result.append(prev)
    print(result)
    return result




# if __name__ == '__main__':
#     # Use the main function to test your implementation
#     # arr = [1, 2, 3, 4, 5]
#     arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]
#
#     print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

arr = [2,4,6,8]
product_of_all_other_numbers(arr)