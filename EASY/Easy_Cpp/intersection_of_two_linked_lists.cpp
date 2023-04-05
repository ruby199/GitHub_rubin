class Solution {
public:
    ListNode *get intersectionNode(ListNode *headA, ListNode *headB){
        ListNode *l1 = headA;
        ListNode *l2 = headB;
        while (l1 != l2){
            l1 = l1 ? l1->next : headB;
            l2 = l2 ? l2->next : headA;
        }
        return l1;
    }
};