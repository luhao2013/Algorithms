/**
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
**/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2)
    {
        ListNode* dummyhead = new ListNode(0);
        ListNode* cur = dummyhead;
        int carry = 0;
        int count = 0;
        while(l1 || l2)
        {
            int x = 0;
            int y = 0;
            if(l1)
            {
                x = l1->val;
                l1 = l1->next;                
            }

            if(l2)
            {
                y = l2->val;
                l2 = l2->next;                
            }

            count = x + y + carry;

            cur->next = new ListNode(count%10);
            cur = cur -> next;
            carry = count / 10;

        }
        if(carry)
            cur->next = new ListNode(carry);
        return dummyhead->next;               
        
    }
};