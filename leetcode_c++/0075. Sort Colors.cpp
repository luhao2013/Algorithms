/*
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-colors
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/


class Solution {
public:
    void swap(vector<int>& nums, int i, int j){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
    void sortColors(vector<int>& nums) {
        int i = 0;
        int j = 0;
        int n = nums.size();
        while(i < n && j < n){
            while(i < n && nums[i] == 0){
                i++;
            }
            j = max(i, j);
            while(j < n && nums[j] != 0){
                j++;
            }
            if(i < n && j < n){
                swap(nums, i, j);
            }
        }

        i = n - 1;
        j = n - 1;
        while(i >= 0 && j >= 0){
            while(i >= 0 && nums[i] == 2){
                i--;
            }
            j = min(i, j);
            while(j >= 0 && nums[j] != 2){
                j--;
            }
            if(i >= 0 && j >= 0){
                swap(nums, i, j);
            }
        }
    }
};
