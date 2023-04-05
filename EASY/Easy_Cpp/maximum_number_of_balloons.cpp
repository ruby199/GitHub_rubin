#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxNumberOfBalloons(string text) {
        unordered_map<char, int> countText;
        for (char c : text){
            countText[c]++;
        }

        unordered_map<char, int> balloon = {{'b', 1}, {'a', 1}, {'l', 2}, {'o', 2}, {'n', 1}};

        int res = INT_MAX;

        for (auto [c, count] : balloon) {
            if (countText.find(c) == countText.end()){
                return 0;
            }
            res = min(res, countText[c] / count);
        }
        return res;
    }
};