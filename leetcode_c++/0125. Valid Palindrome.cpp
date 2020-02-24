/*
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/


// 双指针
class Solution {
public:
    bool isPalindrome(string s) {
        int i = 0;
        int j = s.size() - 1;
        while(i < j){
            // 跳过非字母数字字符
            if(!isalpha(s[i]) && !isdigit(s[i])){
                i++;
                continue;
            }
            if(!isalpha(s[j]) && !isdigit(s[j])){
                j--;
                continue;
            }
            if(tolower(s[i]) != tolower(s[j])){
                return false;
            } else {
                i++;
                j--;
            }
        }
        return true;
    }
};
