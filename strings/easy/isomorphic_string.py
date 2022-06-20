class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        mem_s_t = {}
        mem_t_s = {}
        for c1, c2 in zip(s, t):

            # if
            if (c1 not in mem_s_t) and (c2 not in mem_t_s):
                mem_s_t[c1] = c2
                mem_t_s[c2] = c1
            else:
                if c1 in mem_s_t:
                    if mem_s_t[c1] != c2:
                        return False
                if c2 in mem_t_s:
                    if mem_t_s[c2] != c1:
                        return False
        return True
