/*
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/


class Solution {
public:
    void dfs(vector<int> &nums, int pos, vector<int> &list, vector<vector<int>> &result, vector<int> &visited){
        if(pos == nums.size()){
            result.push_back(list);
        }
        for(int i = 0; i < nums.size(); i++){
            if(!visited[i]){
                list.push_back(nums[i]);
                visited[i] = 1;
                dfs(nums, pos+1, list, result, visited);
                visited[i] = 0;
                list.pop_back();
            }
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> list;
        vector<int> visited(nums.size(), 0);
        dfs(nums, 0, list, result, visited);
        return result;
    }
};
