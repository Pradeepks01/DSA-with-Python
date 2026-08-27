# Two sum

class solution:
    def twosum(self, nums ,target):
        l = 0
        r = len(nums) -1
        while l < r :
            sum = nums[l] + nums[r]
            if sum == target:
                return True
            elif sum < target:
                l += 1
            else:
                r -= 1
        return False




obj = solution()
nums = [2, 7, 11, 15]
target = -13
print(obj.twosum(nums , target))


# complixity
# time = O(n)
# space = O(1)
