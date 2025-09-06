/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    if (headA == NULL) return NULL;
    if (headB == NULL) return NULL;
    struct ListNode* l1 = headA;
    struct ListNode* l2 = headB;
    int a = 0, b = 0;
    while (l1 != NULL || l2 != NULL){
        if (l1 != NULL) {a++; l1 = l1->next;}
        if (l2 != NULL) {b++; l2 = l2->next;}
    }

    l1 = headA;
    l2 = headB;

    if (a > b){
        while (a != b) {l1 = l1->next; a--;}
    } if (b > a){
        while (b != a) {l2 = l2->next; b--;}
    }
    
    while (l1 != NULL){
        if (l1 == l2) break;
        l1 = l1->next;
        l2 = l2 ->next;
    }
    return l1;
}