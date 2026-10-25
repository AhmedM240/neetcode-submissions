class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        t_count, window_count = {},{}

        res, resL = [-1,-1], float('inf')

        for char in t:
            t_count[char] = t_count.get(char, 0) + 1
        
        have, need = 0, len(t_count)

        l = 0


        for r in range(len(s)):
            window_count[s[r]] = window_count.get(s[r], 0) + 1

            if s[r] in t_count and window_count[s[r]] == t_count[s[r]]:
                have += 1
            
            while have == need:
                if((r - l + 1) < resL):
                    res = [l,r]
                    resL = (r - l + 1)

                window_count[s[l]] -= 1

                if s[l] in t_count and window_count[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
        l,r = res
        return s[l : r + 1] if resL != float('inf') else ""