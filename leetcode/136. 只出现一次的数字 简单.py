"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4
"""


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums.sort()
        # i = 0
        # while i < len(nums)-1:
        #     if nums[i] == nums[i+1]:
        #         i += 2
        #     else:
        #         return nums[i]
        # return nums[i]

        # 因为数组中除了一个元素只出现一次之外，其它的元素都出现两次，
        # 如果把所有的数都异或，相同的数字异或为0，
        # 最后只剩下出现一次的数字，它和0异或，结果就是它本身。
        ret = 0
        for num in nums:
            ret ^= num
        return ret

if __name__ == "__main__":
    nums = [4,1,2,1,2]
    test = Solution()
    print(test.singleNumber(nums))