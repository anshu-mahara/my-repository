nums = [5, -2, 3, 9, 0, 6, 10, 7]
# Here k is the number of indexes to be rotated to the right.
k= 3
n= len(nums)
k= k%n
nums[:]= nums[n-k: n] + nums[0:n-k]
print(nums)