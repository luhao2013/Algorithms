/*
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/

class Solution {
public:
    void dfs(vector<int> &nums, int pos, vector<int> &list, vector<vector<int>> &result, vector<int> &visited){
        if(pos == nums.size()){
            result.push_back(list);
        }
        for(int i = 0; i < nums.size(); i++){
            if(!visited[i] && (i ==0 || nums[i] != nums[i-1] || visited[i-1])){
                list.push_back(nums[i]);
                visited[i] = 1;
                dfs(nums, pos+1, list, result, visited);
                visited[i] = 0;
                list.pop_back();
            }
        }
    }
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        vector<int> list;
        vector<int> visited(nums.size(), 0);
        dfs(nums, 0, list, result, visited);
        return result;

    }
};
