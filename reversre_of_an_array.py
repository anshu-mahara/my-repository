nums = [5, 7, 3, 2, 6, 1, 5, 7]
#Two pointer
n= len(nums)
def reverseArr(arr):
    low= 0
    high= n-1
    while low<high:
        arr[low],arr[high]= arr[high],arr[low]
        low+=1
        high-=1
    return arr
print(reverseArr(nums))