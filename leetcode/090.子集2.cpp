/*
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/


class Solution {
public:
    void dfs(vector<int> &nums, int pos, vector<int> & list, vector<vector<int>>& result, vector<int> &visited){
        if(pos == nums.size()){
            result.push_back(list);
            return;
        }
        if(pos == 0 || nums[pos] != nums[pos-1] || visited[pos-1]){
            list.push_back(nums[pos]);
            visited[pos] = 1;
            dfs(nums, pos+1, list, result, visited);
            list.pop_back();
            visited[pos] = 0;
        }
        dfs(nums, pos+1, list, result, visited);
    }
    vector<vector<int>> subsetsWithDup(vector<int>& nums){
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        vector<int> list;  // 一次结果
        vector<int> visited(nums.size(), 0);
        dfs(nums, 0, list, result, visited);
        return result;
    }
};
