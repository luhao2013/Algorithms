"""
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口 k 内的数字。滑动窗口每次只向右移动一位。

返回滑动窗口最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
注意：

你可以假设 k 总是有效的，1 ≤ k ≤ 输入数组的大小，且输入数组不为空。

进阶：

你能在线性时间复杂度内解决此题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sliding-window-maximum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 1.优先队列 MaxHeap 最大的元素永远在堆得的最上面
        # a.维护堆Heap 删除离开的元素，加入新的元素 O(logK)
        # b.Max --> Top O(1)
        # 整体时间复杂度 O(N*logK)
        # 加速的方法，因为固定大小窗口，大的元素进来，之前的元素就不用管了 ----》 Queue

        # 2. Queue ---> deque 双端队列, 双端队列中的元素可以从两端弹出
        # a. 入队列
        # b. 维护 大的进来，前面的就全部出队列，最大值永远在最左面
        # 每个元素只操作一次，时间复杂度是O(N)
        if not nums:
            return []
        window, res = [], []  # window存储的下标
        for i, x in enumerate(nums):
            if i >= k and window[0] <= i - k:  # 下标超过左界就移出
                window.pop(0)
            while window and nums[window[-1]] <= x:
                window.pop()
            window.append(i)
            if i >= k - 1:
                res.append(nums[window[0]])
        return res
