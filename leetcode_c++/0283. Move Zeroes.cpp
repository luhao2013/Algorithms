/*
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/move-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/


// 双指针
// 一开始想的是一个指针从后往前，但这样不能保证顺序
class Solution {
public:
    void swap(vector<int>& nums, int i, int j){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
    void moveZeroes(vector<int>& nums) {
        int i = 0;
        int j = 0;
        int n = nums.size();
        while(i < n && j < n){
            while(i < n && nums[i] != 0){
                i++;
            }
            j = max(i, j);
            while(j < n && nums[j] == 0){
                j++;
            }
            if(i < n && j < n){
                swap(nums, i, j);
            }
        }

    }
};
