class Solution {
    public int getSum(int a, int b) {
        // bit-manipulation
        while (b != 0 ){ // while carry not zero
            int tmp = (a & b) << 1; // calculate carry
            a = a ^ b;  // sum without carry
            b = tmp;    // Assign carry for next iteration
        }
        return a;
    }
}