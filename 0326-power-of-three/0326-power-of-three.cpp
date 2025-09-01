class Solution {
public:
    bool isPowerOfThree(int n) {
        long comp = 1;
        while(comp < n) comp = comp *3;
        if (comp == n) return true;
        else return false;
    }
};