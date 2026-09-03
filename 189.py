# Rotate array

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        def reverse(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        
        x = len(nums)- (k%len(nums))
        reverse(nums, 0, x-1)
        reverse(nums, x, len(nums)-1)   
        reverse(nums, 0, len(nums)-1)

obj = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
obj.rotate(nums, k)
print(nums)