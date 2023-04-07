class Solution {
public:
    bool isPerfectSqiare(int num){
        // O(log n) binary search
        int l = 1, r = num;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (mid * mid > num) {
                r = mid - 1
            } else if (mid * mid < num) {
                l = mid + 1
            } else {
                return true;
            }

        }
        return false;
    }
};