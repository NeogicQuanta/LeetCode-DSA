/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool checker(struct TreeNode* root1, struct TreeNode* root2) {
    if (!root1 && !root2) return true;
    else if ((root1 && !root2) || (!root1 && root2)) return false;
    
    else if (root1->val == root2->val){
        return checker(root1->right, root2->right) && checker(root1->left, root2->left);
    }
    return false;
}
bool isSameTree(struct TreeNode* p, struct TreeNode* q) {
    return checker(p,q);
}