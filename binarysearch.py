Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def binary_search(ar, target):
...     
...     left=0
...     right=len(ar) - 1
...     
...     while left <= right:
...         mid = left + (right - left) // 2
...         
...         if arr[mid] == target:
...             return mid
...         
...         elif arr[mid] < target:
...             left = mid + 1
...             
...         else:
...             right = mid - 1
...     
...     return -1
... 
... 
... ar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
... target = 7
... 
... result = binary_search(arr, target)
... if result != -1:
...     print("Element found at index",str(ar))
... else:
...     print("Element not found in the array")
