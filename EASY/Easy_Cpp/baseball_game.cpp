#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    int calPoints(vector<string>& operations) {
        stack<int> s;
        
        for (string op : operations) {
            if (op == "+") {
                int top = s.top(); s.pop();
                int newTop = top + s.top();
                s.push(top);
                s.push(newTop);
            }
            else if (op == "D") {
                s.push(2 * s.top());
            }
            else if (op == "C") {
                s.pop();
            }
            else {
                s.push(stoi(op));
            }
        }
        
        int sum = 0;
        while (!s.empty()) {
            sum += s.top();
            s.pop();
        }
        
        return sum;
    }
};

int main() {
    Solution solution;
    vector<string> operations {"5","2","C","D","+"};
    int result = solution.calPoints(operations);
    cout << "Result: " << result << endl;
    return 0;
}
