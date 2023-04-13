class Solution {
public:
    void reverseString1(vector<char>& s) {
        // Using two pointers
        int left = 0, right = s.size() - 1;
        while (left < right){
            char temp = s[left];
            s[left] = s[right];
            s[right] = temp;
            left++;
            right--;
        }
    }

    void reverseString2(vector<char>& s) {
        // Using stack
        stack<char> stk;
        for (char c : s){
            stk.push(c);
        }
        int i = 0;
        while (!stk.empty()) {
            s[i] = stk.top();
            stk.pop();
            i++;
        }
    }

    void reverseString3(vector<char>& s, int left, int right) {
        // Recursive method
        if (left >= right) {
            return;
        }
        char temp = s[left];
        s[left] = s[right];
        s[right] = temp;
        reverseString3(s, left + 1, right - 1);
    }
};
