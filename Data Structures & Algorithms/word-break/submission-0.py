class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] represents if s[0:i] can be segmented into dictionary words

        #dp[i] is true if dp[i - len(whatever word matches)] is true
        # and s[i-i - len(whatever word matches):i] is in dict
        # dp[i] represents if s[0:i] can be segmented into dictionary words
        dp = {}
        dp[0] = True
        for i in range(1,len(s)+1):
            dp[i] = False
            # check if s[i - len(this word):i] is a dictionary word AND dp[i-len(this word)] is True
            for word in wordDict:
                if i - len(word) >= 0:
                    # print("IN HERE")
                    # print(word)
                    # print(s[i-(len(word)):i])
                    # print(dp[i-(len(word))])
                    # we are at index 3 s[3]
                    if s[i-(len(word)):i] == word and dp[i-(len(word))] == True:
                        dp[i] = True
        print(dp)
        return dp[len(s)]

