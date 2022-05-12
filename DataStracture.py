import sys
class DataStracture(object):
# day 1:
    def containsDuplicate(nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

    def maxSubArray(nums):
        """
                :type nums: List[int]
                :rtype: int
                """
        max_sum = 0
        sums = [0 for i in range(len(nums))]
        maximum = max(nums)
        if maximum <= 0:
            return maximum
        for i in range(len(nums)):
            max_sum += nums[i]
            if max_sum < 0:
                max_sum = 0
            sums[i] = max_sum
        return max(sums)
# day 2:
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        m = len(nums1) - len(nums2)
        for i in range(m, len(nums1)):
            nums1[i] = nums2[i - m]
        return nums1.sort()

# day 3:
    def intersect(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            temp = nums1
            nums1 = nums2
            nums2 = temp
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        while (i < len(nums1)):
            if nums1[i] == nums2[j]:
                nums2.pop(j)
                i += 1
                j = 0
            elif j >= len(nums2) - 1 and i < len(nums1):
                nums1.pop(i)
                j = 0
            else:
                j += 1
        return nums1

    def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy, sell = 0, 1
        max_profit = 0
        while (sell < len(prices)):
            if prices[buy] < prices[sell]:
                max_profit = max(max_profit, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1
        return max_profit
#day 4

    def matrixReshape(mat, r, c):
        """
         :type mat: List[List[int]]
         :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        if (m * n != r * c) or (m == r and n == c):
            return mat
        output = [[0 for i in range(c)] for i in range(r)]
        i = 0
        j = 0
        s = 0
        k = 0
        while (i < m and j < n):
            output[s][k] = mat[i][j]
            j += 1
            k += 1
            if k >= c:
                s += 1
                k = 0
            if j >= n:
                i += 1
                j = 0

        return output

    def generate(numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        output = []
        output.append([1])
        output.append([1, 1])
        for i in range(2, numRows):
            row = [1]
            for j in range(1, i):
                num = output[i - 1][j] + output[i - 1][j - 1]
                row.append(num)
            row.append(1)
            output.append(row)
        return output
#day 5

def tester():
    #day 1
    print("Contains Duplicate: " , DataStracture.containsDuplicate([1, 2, 3, 1]))
    print("expected: true")
    print("Max SubArray: " , DataStracture.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print("expected: 6")
    #day 3
    print("Intersect: " , DataStracture.intersect([4, 9, 5], [9, 4, 9, 8, 4]))
    print("expected: [4,9]")
    print("Best Time to Buy and Sell Stock: ", DataStracture.maxProfit([7,6,4,3,1]))
    print("expected: 0")
    #day 4
    print("Matrix Reshape: " , DataStracture.matrixReshape([[1,2],[3,4]],1,4))
    print("expected: [[1,2,3,4]]")
    print("Pascal's Triangle: " , DataStracture.generate(5))
    print("expected: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]")
tester()


