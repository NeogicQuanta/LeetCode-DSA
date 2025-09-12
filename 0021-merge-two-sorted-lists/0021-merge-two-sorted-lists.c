/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    if (list1 == NULL) return list2;
    if (list2 == NULL) return list1;

    struct ListNode* l1 = list1;
    struct ListNode* l2 = list2;
    struct ListNode* prev = l1;

    if (list1->val > list2->val){
        l2 = list1;
        l1 = list2;
        prev = l1;
        list1 = list2;
    }

    while (l1 != NULL && l2 != NULL){
        l1 = l1->next;
        if (l1) {
            while (l2 && prev->val <= l2->val && l1->val > l2->val) {
                prev->next = l2;
                prev = l2;
                l2 = l2->next;
                prev->next = l1;
            }
        } else {
            prev->next = l2;
            return list1;
        }
        prev = l1;
    }
    return list1;

    
}