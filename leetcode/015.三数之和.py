"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 1.暴力 超时 O(N^3)
        # triple = []
        # for a in range(len(nums)):
        #     for b in range(len(nums)):
        #         for c in range(len(nums)):
        #             if a !=  b and a != c and b != c and nums[a]+nums[b]+nums[c]==0:
        #                 if sorted([nums[a], nums[b], nums[c]]) not in triple:
        #                     triple.append(sorted([nums[a], nums[b], nums[c]]))
        # return triple

        # 2. a+b+c=0, 枚举完a和b之后，只要查询-(a+b)是否在set里面就行，这样就相当于两重循环
        # O(N^2)

        # 3. 先进行快排O(NlogN), 确定a，b与c从两边向中间夹
        # a+b+c>0, c左移；a+b+c<0, b右移
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, a in enumerate(nums[:-2]):
            if i >= 1 and a == nums[i - 1]:  # 判断第一个元素是否重复，和先前重复就没有价值了
                continue
            d = {}
            for c in nums[i + 1:]:
                if c not in d:  # 假设c存在
                    d[-a - c] = 1  # c的预期值
                else:  # 那现在的c就是要找的
                    res.add((a, -a - c, c))
        return map(list, res)

        # # 4. 一层枚举，空间复杂度更小
        # # 存储结果列表
        # res_list = []
        # # 对nums列表进行排序，无返回值，排序直接改变nums顺序
        # nums.sort()
        # for i in range(len(nums)):
        #     # 如果排序后第一个数都大于0，则跳出循环，不可能有为0的三数之和
        #     if nums[i] > 0:
        #         break
        #     # 排序后相邻两数如果相等，则跳出当前循环继续下一次循环，相同的数只需要计算一次
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue
        #     # 记录i的下一个位置
        #     j = i + 1
        #     # 最后一个元素的位置
        #     k = len(nums) - 1
        #     while j < k:
        #         # 判断三数之和是否为0
        #         if nums[j] + nums[k] == -nums[i]:
        #             # 把结果加入数组中
        #             res_list.append([nums[i], nums[j], nums[k]])
        #             # 判断j相邻元素是否相等，有的话跳过这个
        #             while j < k and nums[j] == nums[j+1]: j += 1
        #             # 判断后面k的相邻元素是否相等，是的话跳过
        #             while j < k and nums[k] == nums[k-1]: k -= 1
        #             # 没有相等则j+1，k-1，缩小范围
        #             j += 1
        #             k -= 1
        #         # 小于-nums[i]的话还能往后取
        #         elif nums[j] + nums[k] < -nums[i]:
        #             j += 1
        #         else:
        #             k -= 1
        # return res_list
