/*
We have an array A of non-negative integers.

For every (contiguous) subarray B = [A[i], A[i+1], ..., A[j]] (with i <= j), we take the bitwise OR of all the elements in B, obtaining a result A[i] | A[i+1] | ... | A[j].

Return the number of possible results.  (Results that occur more than once are only counted once in the final answer.)

 

Example 1:

Input: [0]
Output: 1
Explanation: 
There is only one possible result: 0.
Example 2:

Input: [1,1,2]
Output: 3
Explanation: 
The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
These yield the results 1, 1, 2, 1, 3, 3.
There are 3 unique values, so the answer is 3.
Example 3:

Input: [1,2,4]
Output: 6
Explanation: 
The possible results are 1, 2, 3, 4, 6, and 7.
 

Note:

1 <= A.length <= 50000
0 <= A[i] <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bitwise-ors-of-subarrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/

class Solution
{
public:
    int subarrayBitwiseORs(vector<int> &A)
    {
        unordered_set<int> C;
        for (int i = 0; i < A.size(); i++)
        {
            C.insert(A[i]);
            for (int j = i - 1; j >= 0; --j)
            {
                // 因为非负，所以不再增加就没有必要继续了
                if ((A[j] | A[i]) == A[j])
                    break;
                A[j] |= A[i];
                C.insert(A[j]);
            }
        }

        return C.size();
    }
};

// // lettcode上大佬有自写数据结构，运行时间一骑绝尘，看不懂代码
// class Solution {
// public:
//     int subarrayBitwiseORs(vector<int>& A) {
//         if(A.size()<2)
//             return A.size();
//         unordered_set<int> ans;
//         unordered_set<int> cur;
//         unordered_set<int> pre;

//         for(auto x : A){
//             cur.insert(x);
//             for(auto y : pre)
//                 cur.insert(x | y);
//             cur.swap(pre);
//             cur.clear();
//             ans.insert(begin(pre), end(pre));
//         }

//         return ans.size();
//     }
// };

// 暴力解法加剪枝 O(n2) 通过
// class Solution {
// public:
//     int subarrayBitwiseORs(vector<int>& A) {
//         int n = A.size();
//         unordered_set<int> ans;
        
//         // 找出最大值
//         int max_num = 0;
//         for(int i=0;i<n;i++){
//             max_num |=A[i];
//         }
//         ans.insert(max_num);

//         for(int i=0; i<n; i++){
//             int cur = 0;
//             for(int j=i; j<n; j++){
//                 cur |= A[j];
//                 // 达到最大值，终止
//                 if(cur == max_num)
//                     break;
//                 ans.insert(cur);
//             }
//         }
//         return ans.size();
//     }
// };