"""
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

示例:

输入: 3
输出: [1,3,3,1]
"""
class Solution:
    """
     二项式定理
     https://www.cnblogs.com/henry-1202/p/about_combinatorial_number.html
    """
    def getRow(self, rowIndex: int):
        # https://www.cnblogs.com/henry-1202/p/about_combinatorial_number.html
        result = [1 for _ in range(rowIndex + 1)]
        for i in range(1,rowIndex):
            # print(rowIndex - i + 1, i-1)
            result[i] = (rowIndex - i + 1) * result[i-1] // i
        return result

if __name__ == '__main__':
    rowIndex = 3
    test = Solution()
    print(test.getRow(rowIndex))