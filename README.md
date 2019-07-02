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

024 [两两交换链表中的节点 中等](https://github.com/luhao2013/Algorithms/blob/master/leetcode/24.%E4%B8%A4%E4%B8%A4%E4%BA%A4%E6%8D%A2%E9%93%BE%E8%A1%A8%E4%B8%AD%E7%9A%84%E8%8A%82%E7%82%B9.py)

025 [K个一组反转列表 困难](https://github.com/luhao2013/Algorithms/blob/master/leetcode/25.K%E4%B8%AA%E4%B8%80%E7%BB%84%E5%8F%8D%E8%BD%AC%E5%88%97%E8%A1%A8.py) 解决方法：尾插法

141 [环形链表 简单](<https://github.com/luhao2013/Algorithms/blob/master/leetcode/141.%E7%8E%AF%E5%BD%A2%E9%93%BE%E8%A1%A8.py>) 解决方法：集合，即哈希表；快慢指针

142 [环形链表2 中等](<https://github.com/luhao2013/Algorithms/blob/master/leetcode/142.%E7%8E%AF%E5%BD%A2%E9%93%BE%E8%A1%A82.py>)

206  [反转链表 简单](<https://github.com/luhao2013/Algorithms/blob/master/leetcode/206.%E5%8F%8D%E8%BD%AC%E9%93%BE%E8%A1%A8.py>) 解决方法：迭代：双指针；递归

##### 堆栈
 020 [有效的括号 简单](https://github.com/luhao2013/Algorithms/blob/master/leetcode/20.%E6%9C%89%E6%95%88%E7%9A%84%E6%8B%AC%E5%8F%B7.py)

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

098 [验证二叉搜索树 中等](https://github.com/luhao2013/Algorithms/blob/master/leetcode/098.%E9%AA%8C%E8%AF%81%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.py) 解决办法：中序遍历，升序；递归，左子树的最大值，右子树的最小值；

235 [二叉搜索树的最近公共祖先 简单](https://github.com/luhao2013/Algorithms/blob/master/leetcode/235.%20%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88.py)

236 [二叉树的最近公共祖先 中等](https://github.com/luhao2013/Algorithms/blob/master/leetcode/236.%20%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88.py)

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
