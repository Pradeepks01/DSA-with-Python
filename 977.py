# Squares of a Sorted Array
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        l , r, result = 0, len(nums)-1, []
        while l<=r:
            if (nums[l]*nums[l] > nums[r]*nums[r]):
                result.append(nums[l]*nums[l])
                l += 1
            else:
                result.append(nums[r]*nums[r])
                r -= 1
        return result[::-1]


obj = Solution()
nums= [-4,-1,0,3,10]
print(obj.sortedSquares(nums))