class Solution {
public:
    bool isSubsequence(string s, string t) {
        int p1 = 0;
        int p2 = 0;
        int l1 = s.length();
        int l2 = t.length();

        while(p1 < l1 && p2 < l2){
            if(s[p1] == t[p2]){
                p1++;
            }
            p2++;
        }
        return p1==l1;
    }
};