/*
Given a string, find the length of the longest substring T that contains at most 2 distinct characters.

For example, Given s = “eceba”,

T is "ece" which its length is 3.
————————————————
版权声明：本文为CSDN博主「sundawei2016」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/sundawei2016/article/details/75213638
*/


// 双指针
class Solution{
public:
    int lengthOfLongestSubstringTwoDistinct(string s){
        int k = 2; // 子串最多包含不同字符个数
        int result = 0;
        int i = 0;
        int j = 0;
        int nums = 0;  // 当前子串不同字符个数
        vector<int> count(128);
        int n = s.size();
        while(i < n && j < n){
            int cur = s['j'] - 'A';
            if(num <= k){
                if(count[cur] == 0){
                    num++;
                }
                count[cur]++;
                j++;
                result = max(result, j - i);
            } else if(count[cur] > 0){
                count[cur]++;
                j++;
                result = max(result, j-i);
            } else { // 不符合规则
                int prev = s[i] - 'A';
                count[prev]--;
                if(count[prev] == 0){
                    num--;
                }
                i++;
            }
        }
        return result;
    }
};
