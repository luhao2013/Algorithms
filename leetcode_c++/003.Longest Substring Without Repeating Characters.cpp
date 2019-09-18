/**
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
**/
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // 1.使用集合

        # 2.使用数组来模拟哈希，ASCII字符256个
        int array[256] = {0};
        int max_len = 0;
        int left_index = 0;
        for(int i=0; i<s.length(); i++)
        {
            if(array[s[i]] != 0 && array[s[i]] >= left_index )  //如果s[i]重复出现且s[i]第一次出现的位置在s[left,i]之间
                left_index = array[s[i]];
            else  //否则更新mlen
                max_len = max(max_len, i-left_index+1);
            array[s[i]] = i + 1;  //更新left坐标

        }
        return max_len;
        
    }
};