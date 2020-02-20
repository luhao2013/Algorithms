/*
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/


class Solution {
public:
    void dfs(vector<int> &nums, int pos, vector<int> & list, vector<vector<int>>& result){
        if(pos == nums.size()){
            result.push_back(list);
            return;
        }
        list.push_back(nums[pos]);
        dfs(nums, pos+1, list, result);
        list.pop_back();
        dfs(nums, pos+1, list, result);
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> list;  // 一次结果
        dfs(nums, 0, list, result);
        return result;
    }
};
