def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = list(map(int, input("Enter the array elements (comma-separated): ").split(',')))
target = int(input("Enter the target value: "))
result = binary_search(arr, target)
if result != -1:
    print("Element found at index", result)
else:
    print("Element not found in the array.")

arr.sort()
print("Sorted Array",arr)




# # Path: bubble_sort_algorithm.py
# # how  to work it ?
# 1. first input the array elements
# 2. then input the target value
# 3. then it will show the index of the target value
# 4. if the target value is not in the array then it will show "Element not found in the array."
# 5. if the target value is in the array then it will show "Element found at index", result
# 6. then it will show the sorted array 

