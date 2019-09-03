# Algorithms
基础算法实现

***

###  一、 排序算法
1. [冒泡排序](https://github.com/luhao2013/Algorithms/blob/master/sort_algorithm/bubble_sort.py)
2. [选择排序](https://github.com/luhao2013/Algorithms/blob/master/sort_algorithm/selection_sort.py)
3. [插入排序](https://github.com/luhao2013/Algorithms/blob/master/sort_algorithm/insert_sort.py)
4. [快速排序](https://github.com/luhao2013/Algorithms/blob/master/sort_algorithm/quick_sort.py)
5. [归并排序](https://github.com/luhao2013/Algorithms/blob/master/sort_algorithm/merge_sort.py)

### 二、Leetcode

##### 数组和链表

- 逻辑简单，注重实现
002 [两数相加 中等](https://github.com/luhao2013/Algorithms/blob/master/leetcode/002.%E4%B8%A4%E6%95%B0%E7%9B%B8%E5%8A%A0.py)

024 [两两交换链表中的节点 中等](https://github.com/luhao2013/Algorithms/blob/master/leetcode/024.%E4%B8%A4%E4%B8%A4%E4%BA%A4%E6%8D%A2%E9%93%BE%E8%A1%A8%E4%B8%AD%E7%9A%84%E8%8A%82%E7%82%B9.py)

025 [K个一组反转列表 困难](https://github.com/luhao2013/Algorithms/blob/master/leetcode/025.K%E4%B8%AA%E4%B8%80%E7%BB%84%E5%8F%8D%E8%BD%AC%E5%88%97%E8%A1%A8.py) 解决方法：尾插法

141 [环形链表 简单](<https://github.com/luhao2013/Algorithms/blob/master/leetcode/141.%E7%8E%AF%E5%BD%A2%E9%93%BE%E8%A1%A8.py>) 解决方法：集合，即哈希表；快慢指针

142 [环形链表2 中等](<https://github.com/luhao2013/Algorithms/blob/master/leetcode/142.%E7%8E%AF%E5%BD%A2%E9%93%BE%E8%A1%A82.py>)

206  [反转链表 简单](<https://github.com/luhao2013/Algorithms/blob/master/leetcode/206.%E5%8F%8D%E8%BD%AC%E9%93%BE%E8%A1%A8.py>) 解决方法：迭代：双指针；递归

##### 堆栈
 020 [有效的括号 简单](https://github.com/luhao2013/Algorithms/blob/master/leetcode/020.%E6%9C%89%E6%95%88%E7%9A%84%E6%8B%AC%E5%8F%B7.py)

##### 优先队列

- Heap(eg. Binary, Binomial, Fibonacci)
- Binary Serach Tree

239 [滑动窗口最大值 困难](https://github.com/luhao2013/Algorithms/blob/master/leetcode/239.%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E6%9C%80%E5%A4%A7%E5%80%BC.py) 解决方法：双端队列

703 [数据流中第k大元素 简单](https://github.com/luhao2013/Algorithms/blob/master/leetcode/703.%E6%95%B0%E6%8D%AE%E6%B5%81%E4%B8%AD%E7%9A%84%E7%AC%ACK%E5%A4%A7%E5%85%83%E7%B4%A0.py) 解决方法：最小堆

##### 哈希表
001 [两数之和 简单](https://github.com/luhao2013/Algorithms/blob/master/leetcode/001.%E4%B8%A4%E6%95%B0%E4%B9%8B%E5%92%8C.py)

015 [三数之和 中等](https://github.com/luhao2013/Algorithms/blob/master/leetcode/015.%E4%B8%89%E6%95%B0%E4%B9%8B%E5%92%8C.py)

018 [四数之和 中等](https://github.com/luhao2013/Algorithms/blob/master/leetcode/018.%E5%9B%9B%E6%95%B0%E4%B9%8B%E5%92%8C.py)

242 [有效的字母异位词 简单](https://github.com/luhao2013/Algorithms/blob/master/leetcode/242.%E6%9C%89%E6%95%88%E7%9A%84%E5%AD%97%E6%AF%8D%E5%BC%82%E4%BD%8D%E8%AF%8D.py)

##### 树、二叉树和二叉搜索树
- 二叉树是链表有两个next指针，称为左右孩子
- 完全二叉树是每个非叶子节点都有两个孩子
- next节点都指回去的是图
- 链表是特殊化的树，树是特殊化的图
- 二叉搜索树（有序二叉树，排序二叉树）是指一颗空树或具有下列性质的二叉树 
    1. 左子树上所有节点均小于它的根节点的值
    2. 右子树上所有节点均大于它的根节点的值
    3. 递归地，左右子树也分别为二叉搜索树
- 二叉搜索树平均搜索复杂度是O(logN),退化的只有左子树的复杂度为O(N)

- 二叉树的遍历
> 这里一定要理解递归的思想，这里的递归都是根右左三者先后顺序的嵌套,就是要将左子树右子树看成一个整体，这样才能理解递归的嵌套关系

144 [二叉树的前序遍历 中等](https://github.com/luhao2013/Algorithms/blob/master/leetcode/144.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%89%8D%E5%BA%8F%E9%81%8D%E5%8E%86.py)

145 [二叉树的后序遍历 困难](https://github.com/luhao2013/Algorithms/blob/master/leetcode/145.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%90%8E%E5%BA%8F%E9%81%8D%E5%8E%86.py)

094 [二叉树的中序遍历 中等](https://github.com/luhao2013/Algorithms/blob/master/leetcode/094.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E4%B8%AD%E5%BA%8F%E9%81%8D%E5%8E%86.py)


098 [验证二叉搜索树 中等](https://github.com/luhao2013/Algorithms/blob/master/leetcode/098.%E9%AA%8C%E8%AF%81%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.py) 解决办法：中序遍历，升序；递归，左子树的最大值，右子树的最小值；

235 [二叉搜索树的最近公共祖先 简单](https://github.com/luhao2013/Algorithms/blob/master/leetcode/235.%20%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88.py)

236 [二叉树的最近公共祖先 中等](https://github.com/luhao2013/Algorithms/blob/master/leetcode/236.%20%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88.py)

105 [从前序与中序遍历序列构造二叉树 中等](https://github.com/luhao2013/Algorithms/blob/master/leetcode/152.%E4%B9%98%E7%A7%AF%E6%9C%80%E5%A4%A7%E5%AD%90%E5%BA%8F%E5%88%97.py) 解决方法：递归；迭代需补充
##### 递归 & 分治
050 [Pow(x,y) 中等](https://github.com/luhao2013/Algorithms/blob/master/leetcode/050.Pow(x%2Cn).py) 解决方法：很有意思

169 [求众数 简单](https://github.com/luhao2013/Algorithms/blob/master/leetcode/169.%20%E6%B1%82%E4%BC%97%E6%95%B0%20%E7%AE%80%E5%8D%95.py)

##### DFS & BFS
102 [二叉树的层次遍历 中等](https://github.com/luhao2013/Algorithms/blob/master/leetcode/102.%20%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%B1%82%E6%AC%A1%E9%81%8D%E5%8E%86.py)

104 [二叉树的最大深度 简单](https://github.com/luhao2013/Algorithms/blob/master/leetcode/104.%20%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E5%A4%A7%E6%B7%B1%E5%BA%A6.py) 解决方法：用BFS时，第一个遇到遇到的叶子节点是最小深度，最后到达叶子节点是最大深度

111 [二叉树的最小深度 简单](https://github.com/luhao2013/Algorithms/blob/master/leetcode/111.%20%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E5%B0%8F%E6%B7%B1%E5%BA%A6.py)

022 [括号生成 中等](https://github.com/luhao2013/Algorithms/blob/master/leetcode/022.%E6%8B%AC%E5%8F%B7%E7%94%9F%E6%88%90.py) 解决方法：动态规划；递归回溯剪枝

##### 回溯法(剪枝)
- 通过搜索状态空间树来求问题的可行解或最优解的方法，搜索方法如DFS和BFS
- 回溯法使用约束函数和限界函数统称为剪枝函数来压缩实际需要生成的状态空间树的节点数
- 回溯法是比贪心法和动态规划更一般的方法
- 使用剪枝函数的深度优先生成状态空间树中结点的求解方法称为回溯法
- 广度优先生成结点，并使用剪枝函数的方法称为分支限界法

036 [有效的数独 中等]()

037 [解数独 困难]()

051 [N皇后 困难](https://github.com/luhao2013/Algorithms/blob/master/leetcode/051.N%E7%9A%87%E5%90%8E.py)

052 [N皇后II 困难]()

##### 二分查找

069 [x的平方根 简单](https://github.com/luhao2013/Algorithms/blob/master/leetcode/069.x%E7%9A%84%E5%B9%B3%E6%96%B9%E6%A0%B9.py) 解决方法：二分法；牛顿迭代法

##### Trie树
- 即字典树，又称单词查找树或链树，是一种树形结构，是一种哈希树的变种。
- 典型的应用是用于统计和排序大量的字符串（但不仅限于字符串），所以经常被搜索引擎系统用于文本词频统计。
- 优点是：最大限度地减少无谓地字符串比较，查询效率比哈希表高。
- 核心思想是空间换时间。利用字符串地公共前缀来降低查询时间的开销以达到提高效率的目的。
- 边代表单词，节点代表前缀。

208 [实现Trie(前缀树) 中等](https://github.com/luhao2013/Algorithms/blob/master/leetcode/208.%E5%AE%9E%E7%8E%B0%20Trie%20(%E5%89%8D%E7%BC%80%E6%A0%91).py)

097 [单词搜索 中等](https://github.com/luhao2013/Algorithms/blob/master/leetcode/097.%E5%8D%95%E8%AF%8D%E6%90%9C%E7%B4%A2.py) 解决方法：DFS+回溯

212 [单词搜索2 困难](https://github.com/luhao2013/Algorithms/blob/master/leetcode/212.%E5%8D%95%E8%AF%8D%E6%90%9C%E7%B4%A22.py)

##### 位运算
- 由于位运算直接对内存数据进行操作，不需要转成十进制，因此处理速度非常快

191 [位1的个数 简单](https://github.com/luhao2013/Algorithms/blob/master/leetcode/191.%E4%BD%8D1%E7%9A%84%E4%B8%AA%E6%95%B0.py)

231 [2的幂 简单](https://github.com/luhao2013/Algorithms/blob/master/leetcode/231.2%E7%9A%84%E5%B9%82.py)

338 [比特位计数 中等](https://github.com/luhao2013/Algorithms/blob/master/leetcode/338.%E6%AF%94%E7%89%B9%E4%BD%8D%E8%AE%A1%E6%95%B0.py)

052 [N皇后2 困难](https://github.com/luhao2013/Algorithms/blob/master/leetcode/052.N%E7%9A%87%E5%90%8E2.py)

##### 动态规划
- Dynamic Programming 这里的Programming规划就是递推
1. 递推 (递归 + 记忆化)
2. 状态的定义
3. 状态转移方程
4. 最优子结构

- DP vs 回溯 vs 贪心
1. 回溯（递归）-重复计算，没有最优子结构的时候，所有的可能不存在重复计算时候回溯就是最优的
2. 贪心-永远局部最优
3. DP-记录局部子结构/多种记录值，集上述两者之大成

509 [斐波那契数 简单](https://github.com/luhao2013/Algorithms/blob/master/leetcode/509.%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0.py)

070 [爬楼梯 简单](https://github.com/luhao2013/Algorithms/blob/master/leetcode/070.%E7%88%AC%E6%A5%BC%E6%A2%AF.py)

120 [三角形最小路径和 中等](https://github.com/luhao2013/Algorithms/blob/master/leetcode/120.%E4%B8%89%E8%A7%92%E5%BD%A2%E6%9C%80%E5%B0%8F%E8%B7%AF%E5%BE%84%E5%92%8C.py)

152 [乘积最大子序列 中等](https://github.com/luhao2013/Algorithms/blob/master/leetcode/152.%E4%B9%98%E7%A7%AF%E6%9C%80%E5%A4%A7%E5%AD%90%E5%BA%8F%E5%88%97.py)

[股票解法总结](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/solution/yi-ge-tong-yong-fang-fa-tuan-mie-6-dao-gu-piao-wen/)

123 [买卖股票的最佳时机3 困难](https://github.com/luhao2013/Algorithms/blob/master/leetcode/123.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BA3.py)

300 [最长上升子序列 中等](https://github.com/luhao2013/Algorithms/blob/master/leetcode/300.%E6%9C%80%E9%95%BF%E4%B8%8A%E5%8D%87%E5%AD%90%E5%BA%8F%E5%88%97.py)

322 [零钱兑换 中等](https://github.com/luhao2013/Algorithms/blob/master/leetcode/322.%E9%9B%B6%E9%92%B1%E5%85%91%E6%8D%A2.py)解决方法：考虑成上台阶问题

72 [编辑距离 困难](https://github.com/luhao2013/Algorithms/blob/master/leetcode/072.%E7%BC%96%E8%BE%91%E8%B7%9D%E7%A6%BB.py)

##### 并查集
- 一般并查集用数组来实现，数组的初始值指向自己的下标，然后开始合并

### 三、剑指offer
03 [二维数组中的查找](https://github.com/luhao2013/Algorithms/blob/master/offer/03.%E4%BA%8C%E7%BB%B4%E6%95%B0%E7%BB%84%E4%B8%AD%E7%9A%84%E6%9F%A5%E6%89%BE.py)

04 [替换空格](https://github.com/luhao2013/Algorithms/blob/master/offer/04.%E6%9B%BF%E6%8D%A2%E7%A9%BA%E6%A0%BC.py)解决方法：前后指针

05 [从尾到头打印链表](https://github.com/luhao2013/Algorithms/blob/master/offer/05.%E4%BB%8E%E5%B0%BE%E5%88%B0%E5%A4%B4%E6%89%93%E5%8D%B0%E9%93%BE%E8%A1%A8.py):不改变链表结构

06 [重建二叉树](https://github.com/luhao2013/Algorithms/blob/master/offer/06.%E9%87%8D%E5%BB%BA%E4%BA%8C%E5%8F%89%E6%A0%91.py)

07 [用两个栈实现一个队列](https://github.com/luhao2013/Algorithms/blob/master/offer/07.%E7%94%A8%E4%B8%A4%E4%B8%AA%E6%A0%88%E5%AE%9E%E7%8E%B0%E9%98%9F%E5%88%97.py)解决方法：用两个栈，删除时栈2不为空直接删除，否则，将栈1元素压入栈2再删除。
用两个队列实现栈：保证一个队列尾空，需要删除时，将n-1各元素转移到另一个队列中，就可以删除最后入栈的元素了。

08 [旋转数组的最小数字](https://github.com/luhao2013/Algorithms/blob/master/offer/08.%E6%97%8B%E8%BD%AC%E6%95%B0%E7%BB%84%E7%9A%84%E6%9C%80%E5%B0%8F%E6%95%B0%E5%AD%97.py)解决方法:二分查找，无法解决的顺序查找

10 [二进制中1的个数](https://github.com/luhao2013/Algorithms/blob/master/offer/10.%E4%BA%8C%E8%BF%9B%E5%88%B6%E4%B8%AD1%E7%9A%84%E4%B8%AA%E6%95%B0.py)

11 [数值的整数次方](https://github.com/luhao2013/Algorithms/blob/master/offer/11.%E6%95%B0%E5%80%BC%E7%9A%84%E6%95%B4%E6%95%B0%E6%AC%A1%E6%96%B9.py)解决方法：考虑到负指数和0指数；可以使用二分法思想的递归

12 [打印1到最大的n位数](https://github.com/luhao2013/Algorithms/blob/master/offer/12.%E6%89%93%E5%8D%B01%E5%88%B0%E6%9C%80%E5%A4%A7%E7%9A%84n%E4%BD%8D%E6%95%B0.py)

13 [在O(1)时间删除链表结点](https://github.com/luhao2013/Algorithms/blob/master/offer/13.%E5%9C%A8O(1)%E6%97%B6%E9%97%B4%E5%88%A0%E9%99%A4%E9%93%BE%E8%A1%A8%E7%BB%93%E7%82%B9.py)

14 [调整数组顺序使奇数位于偶数前面](https://github.com/luhao2013/Algorithms/blob/master/offer/14.%E8%B0%83%E6%95%B4%E6%95%B0%E7%BB%84%E9%A1%BA%E5%BA%8F%E4%BD%BF%E5%A5%87%E6%95%B0%E4%BD%8D%E4%BA%8E%E5%81%B6%E6%95%B0%E5%89%8D%E9%9D%A2.py)解决方法：双指针

15 [链表中倒数第k个结点](https://github.com/luhao2013/Algorithms/blob/master/offer/15.%E9%93%BE%E8%A1%A8%E4%B8%AD%E5%80%92%E6%95%B0%E7%AC%ACk%E4%B8%AA%E7%BB%93%E7%82%B9.py)解决方法：快慢指针
- 相关题目：求链表的中间结点。定义快慢指针，快指针一次走两步，慢指针一次走一步，走的快的走到链表末尾时，慢指针正好在链表的中间。
- 相关题目：判断链表是否有环。快指针追上慢指针，链表时环形。快指针走到末尾，不是环形。

16 [反转链表](https://github.com/luhao2013/Algorithms/blob/master/offer/16.%E5%8F%8D%E8%BD%AC%E9%93%BE%E8%A1%A8.py)

17 [合并两个排序的链表](https://github.com/luhao2013/Algorithms/blob/master/offer/17.%E5%90%88%E5%B9%B6%E4%B8%A4%E4%B8%AA%E6%8E%92%E5%BA%8F%E7%9A%84%E9%93%BE%E8%A1%A8.py)

18 [树的子结构](https://github.com/luhao2013/Algorithms/blob/master/offer/18.%E6%A0%91%E7%9A%84%E5%AD%90%E7%BB%93%E6%9E%84.py)

19 [二叉树的镜像](https://github.com/luhao2013/Algorithms/blob/master/offer/19.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E9%95%9C%E5%83%8F.py)

20 [顺时针打印矩阵](https://github.com/luhao2013/Algorithms/blob/master/offer/20.%E9%A1%BA%E6%97%B6%E9%92%88%E6%89%93%E5%8D%B0%E7%9F%A9%E9%98%B5.py)

21 [包含min函数的栈](https://github.com/luhao2013/Algorithms/blob/master/offer/21.%E5%8C%85%E5%90%ABmin%E5%87%BD%E6%95%B0%E7%9A%84%E6%A0%88.py)

22 [栈的压入和弹出序列](https://github.com/luhao2013/Algorithms/blob/master/offer/22.%E6%A0%88%E7%9A%84%E5%8E%8B%E5%85%A5%E5%92%8C%E5%BC%B9%E5%87%BA%E5%BA%8F%E5%88%97.py)

23 [从上往下打印二叉树](https://github.com/luhao2013/Algorithms/blob/master/offer/23.%E4%BB%8E%E4%B8%8A%E5%BE%80%E4%B8%8B%E6%89%93%E5%8D%B0%E4%BA%8C%E5%8F%89%E6%A0%91.py)

24 [二叉搜索树的后序遍历序列](https://github.com/luhao2013/Algorithms/blob/master/offer/24.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E5%90%8E%E5%BA%8F%E9%81%8D%E5%8E%86%E5%BA%8F%E5%88%97.py)

25 [二叉树中和为某一值的路径](https://github.com/luhao2013/Algorithms/blob/master/offer/25.%E4%BA%8C%E5%8F%89%E6%A0%91%E4%B8%AD%E5%92%8C%E4%B8%BA%E6%9F%90%E4%B8%80%E5%80%BC%E7%9A%84%E8%B7%AF%E5%BE%84.py)

26 [复杂链表的复制](https://github.com/luhao2013/Algorithms/blob/master/offer/26.%E5%A4%8D%E6%9D%82%E9%93%BE%E8%A1%A8%E7%9A%84%E5%A4%8D%E5%88%B6.py)

27 [二叉搜索树与双向链表](https://github.com/luhao2013/Algorithms/blob/master/offer/27.二叉搜索树与双向链表.py)

28 [字符串的全排列](https://github.com/luhao2013/Algorithms/blob/master/offer/28.%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%9A%84%E5%85%A8%E6%8E%92%E5%88%97.py)

29 [数组中出现次数超过一半的数字](https://github.com/luhao2013/Algorithms/blob/master/offer/29.数组中出现次数超过一半的数字.py)

30 []()

31 [连续子数组的最大和](https://github.com/luhao2013/Algorithms/blob/master/offer/31.连续子数组的最大和.py)

32 [从1到n整数中1出现的次数](https://github.com/luhao2013/Algorithms/blob/master/offer/32.%E4%BB%8E1%E5%88%B0n%E6%95%B4%E6%95%B0%E4%B8%AD1%E5%87%BA%E7%8E%B0%E7%9A%84%E6%AC%A1%E6%95%B0.py)

33 [把数组排成最小数](https://github.com/luhao2013/Algorithms/blob/master/offer/33.把数组排成最小数.py)

34 [丑数](https://github.com/luhao2013/Algorithms/blob/master/offer/34.丑数.py)

35 [第一个只出现一次的字符](https://github.com/luhao2013/Algorithms/blob/master/offer/35.%E7%AC%AC%E4%B8%80%E4%B8%AA%E5%8F%AA%E5%87%BA%E7%8E%B0%E4%B8%80%E6%AC%A1%E7%9A%84%E5%AD%97%E7%AC%A6.py)

36 [数组中的逆序对](https://github.com/luhao2013/Algorithms/blob/master/offer/36.数组中的逆序对.py) 解决方法：归并排序 **

37 [两个链表的第一个公共节点](https://github.com/luhao2013/Algorithms/blob/master/offer/37.两个链表的第一个公共节点.py)

38 [数字在排序数组中出现的次数](https://github.com/luhao2013/Algorithms/blob/master/offer/38.数字在排序数组中出现的次数.py) 解决方法：二分搜索

39 [二叉树的深度](https://github.com/luhao2013/Algorithms/blob/master/offer/39.二叉树的深度.py)

39 [平衡二叉树](https://github.com/luhao2013/Algorithms/blob/master/offer/39.平衡二叉树.py)

40 [数组中只出现一次的数字](https://github.com/luhao2013/Algorithms/blob/master/offer/40.数组中只出现一次的数字.py) **

41 [和为S的连续正数序列](https://github.com/luhao2013/Algorithms/blob/master/offer/41.和为s的连续正数序列.py)

41 [和为S的两个数字](https://github.com/luhao2013/Algorithms/blob/master/offer/41.和为S的两个数字.py)

44 [扑克牌的顺子](https://github.com/luhao2013/Algorithms/blob/master/offer/44.扑克牌的顺子.py)

45 [圆圈中最后剩下的数字](https://github.com/luhao2013/Algorithms/blob/master/offer/45.圆圈中最后剩下的数字.py) 用递推可以简单理解，但还是有些费解

46 [求1到n的和](https://github.com/luhao2013/Algorithms/blob/master/offer/46.%E6%B1%821%E5%88%B0n%E7%9A%84%E5%92%8C.py)

47 [不用加减乘除做加法](https://github.com/luhao2013/Algorithms/blob/master/offer/47.%E4%B8%8D%E7%94%A8%E5%8A%A0%E5%87%8F%E4%B9%98%E9%99%A4%E5%81%9A%E5%8A%A0%E6%B3%95.py) python做需要考虑不会溢出的问题

49 [把字符串转换成整数](https://github.com/luhao2013/Algorithms/blob/master/offer/49.%E6%8A%8A%E5%AD%97%E7%AC%A6%E4%B8%B2%E8%BD%AC%E6%8D%A2%E6%88%90%E6%95%B4%E6%95%B0.py)

51 [数组中重复的数字](https://github.com/luhao2013/Algorithms/blob/master/offer/51.数组中重复的数字.py)

52 [构建乘积数组](https://github.com/luhao2013/Algorithms/blob/master/offer/52.%E6%9E%84%E5%BB%BA%E4%B9%98%E7%A7%AF%E6%95%B0%E7%BB%84.py)

54 [表示数值的字符串](https://github.com/luhao2013/Algorithms/blob/master/offer/54.%E8%A1%A8%E7%A4%BA%E6%95%B0%E5%80%BC%E7%9A%84%E5%AD%97%E7%AC%A6%E4%B8%B2.py)

55 [字符流中第一个不重复的字符](https://github.com/luhao2013/Algorithms/blob/master/offer/55.%E5%AD%97%E7%AC%A6%E6%B5%81%E4%B8%AD%E7%AC%AC%E4%B8%80%E4%B8%AA%E4%B8%8D%E9%87%8D%E5%A4%8D%E7%9A%84%E5%AD%97%E7%AC%A6.py)
