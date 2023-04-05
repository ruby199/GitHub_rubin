class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        //mark existing
        for (int n : nums){
            int i = abs(n) - 1;
            nums[i] = -1 * abs(nums[i]); // if the number exist mark it with (-1)
        }

        vector<int> res;
        for (int i = 0; i < nums.size(); i++){
            if (nums[i] > 0){ // if the number did not appear -> no marking thus positive
                res.push_back(i + 1);
            }
        }
        return res;
    }
};