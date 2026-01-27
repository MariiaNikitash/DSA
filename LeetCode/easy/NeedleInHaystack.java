/* Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1. */

class Solution {
    int strStr(String haystack, String needle) {
        if (needle.length() == 0) {
            return 0;
        }

        for (int i=0; i <= haystack.length() - needle.length(); i++) {
            for  (int j=0; j < needle.length(); j++) {
                if (needle.charAt(j) != haystack.charAt(i + j)) {
                    break;
                }
                if (j == needle.length()-1) {
                    return i;
                }
            }
        
        }
        return -1;
    }
}

public class NeedleInHaystack {
    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.strStr("sadbutsad", "sad"));   // 0
        System.out.println(sol.strStr("leetcode", "leeto")); // -1
    }
}