#include <vector>

using namespace std;

class Solution {
public:
    void moveZeros(vector<int>& nums) {
        int l = 0;
        for (int r = 0; r < nums.size(); r++) {
            if (nums[r]) {
                swap(nums[l], nums[r]);
                i++;
            }
        }
    }
};