class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 1 + max(count(0,1), count(1,0))
        dp = {}
        # dp(i,j) represents the length of the LCS from text1[0:i] and text2[0:j]
        # crab  ca dp(1,3) = 2
        
        def count(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            # if i == 0 and j == 0 and text1[i] == text2[j]:
            #     return 1
            sum = 0 
            if i == -1 or j == -1:
                sum =  0
            # elif i == 0 or j == 0:
            #     return 0            
            else:
                # increment i or increment j
                if text1[i] == text2[j]:
                    sum =  1 + count(i-1,j-1)
                else:
                    sum = max(count(i-1,j), count(i,j-1))
            dp[(i,j)] = sum
            return sum
        return count(len(text1)-1, len(text2)-1)
        # 2,1
        # 1 + count(1,0)