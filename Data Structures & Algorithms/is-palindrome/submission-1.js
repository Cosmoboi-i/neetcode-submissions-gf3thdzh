class Solution {
    /**
     * @param {string} s
     * @return {string}
     */
    toAlphaNum(s) {
        const stringWithoutSpace = s.replace(/[^a-zA-Z0-9]/g, '');
        const lowerCaseString = stringWithoutSpace.toLowerCase();
        return lowerCaseString;
    }

    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        const anStr = this.toAlphaNum(s);

        const n = anStr.length;
        let a = 0;
        let b = n - 1;

        while (a < b) {
            if (anStr[a] !== anStr[b]) {
                return false
            }
            a++;
            b--;
        }

        return true;
    }

    
}
