class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # build two maps 
        # for each string, map character to occurences
        # return early if theyre not the same length
        # check maps. see that m1[char] exists and that m2[char] == m1[char]

        if len(s) != len(t):
            return False
        s_map = {}
        t_map = {}
        for i in range(len(s)):
            s_curr = s[i]
            t_curr = t[i]
            if s_curr in s_map:
                s_map[s_curr] +=1
            else:
                s_map[s_curr] = 1
            
            if t_curr in t_map:
                t_map[t_curr] +=1
            else:
                t_map[t_curr] = 1

        for elem in s_map:
            if elem not in t_map or t_map[elem] != s_map[elem]:
                return False
        return True



        