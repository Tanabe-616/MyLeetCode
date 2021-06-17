s = "abcabcbb"
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        w = ""
        q = 0
        count = 0
        longest = 0
        for un in s:
            for ti in w:
                q += 1
                if ti == un:
                    if count >= longest:
                        longest = count
                    count -= q
                    w = w[q:]
            w += un
            count += 1
            q = 0
        if longest < count:
            longest = count
        return longest
            
a = Solution()
print(a.lengthOfLongestSubstring(s))