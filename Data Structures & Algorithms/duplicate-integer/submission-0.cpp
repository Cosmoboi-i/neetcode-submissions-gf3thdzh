#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        map<int, int> freqTable;

        for (int i = 0; i < nums.size(); i++) {
            if (freqTable[nums[i]] >= 1) {
                return true;
            }
            freqTable[nums[i]]++;
        }

        return false;
    }
};
