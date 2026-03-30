class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> indexMap;

        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            if (indexMap.count(diff)) {
                return {indexMap[diff], i};
            }
            indexMap[nums[i]] = i;
        }
    }
};
