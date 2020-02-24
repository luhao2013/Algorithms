/*
Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
Example 1:
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-triangle-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/


// 三指针
class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        if (nums.size() < 3)
        {
            return 0;
        }
        // 优化点
        sort(nums.begin(), nums.end());
        int result = 0;
        int n = nums.size();
        for(int i = 0; i < n-2; i++){
            for(int j = i + 1; j < n -1; j++){
                int k = n - 1;
                while(j < k){
                    // 优化点
                    if(nums[i] + nums[j] > nums[k]){
                        result += k -j;
                        break;
                    } else {
                        --k;
                    }
                }
            }
        }
        return result;
    }
};
