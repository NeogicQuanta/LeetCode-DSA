/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    if (!(head && head->next) )return head;

    struct ListNode* prev = head;
    struct ListNode* next = head->next;
    // struct ListNode*

    while (next) {
        while (next && prev->val == next->val) next = next->next;
        if (!(next)) {
            prev->next = next;
            return head;
        }
        prev->next = next;
        prev = next;
        next = next->next;
    }
    return head;
}