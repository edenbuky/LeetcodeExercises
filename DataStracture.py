import sys
class DataStracture(object):
    def containsDuplicate(nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

    def maxSubArray(nums):
        max_sum = 0
        maximum = max(nums)
        if maximum <= 0:
            return maximum
        for i in range(len(nums)):
            max_sum = max(max_sum, max_sum + nums[i])
            if max_sum < 0:
                max_sum = 0
        return max_sum

def tester():
    print(DataStracture.containsDuplicate([1,2,3,1]))
    print("expected: true")
    print(DataStracture.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print("expected: 6")

