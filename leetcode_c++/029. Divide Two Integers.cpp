/**
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/divide-two-integers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/

class Solution {
public:
    int divide(int dividend, int divisor) {
        // 特判
        if (divisor == 0)
            return 0;
        if (divisor == 1)
            return dividend;
        if (dividend == INT_MIN && divisor == -1)
            return INT_MAX;
        
        int signdiff = (dividend > 0) ^ (divisor >0);
        
        long t = abs((long)dividend);
        long d = abs((long)divisor);
        int result = 0;
        
        for (int i = 31; i >= 0; i --){
            if ((t >> i) >= d){
                result += 1 << i;
                t -= d << i;
            }
        }
        return signdiff ? -result : result;
    }
};
