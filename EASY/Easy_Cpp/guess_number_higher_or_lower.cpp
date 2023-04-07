class Solution {
public:
    int guessNumber(int n) {
        //binary search algorithm
        int l = 1, r = n;

        while (l <= r){
            int m = l + (r - 1) / 2;
            int res = guess(m);
            if (res > 0) {
                l = m + 1;
            } else if (res < 0) {
                r = m - 1;
            } else {
                return m;
            }
        }

        return -1; // not found
    }
};