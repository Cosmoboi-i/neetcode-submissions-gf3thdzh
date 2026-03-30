class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> s_freqTable(26);
        vector<int> t_freqTable(26);

        for (int i = 0; i < s.size(); i++) {
            s_freqTable[s[i] - 'a']++;
        }

        for (int i = 0; i < t.size(); i++) {
            t_freqTable[t[i] - 'a']++;
        }

        for (int i = 0; i < 26; i++) {
            if (s_freqTable[i] != t_freqTable[i]) {
                return false;
            }
        }

        return true;
    }
};
