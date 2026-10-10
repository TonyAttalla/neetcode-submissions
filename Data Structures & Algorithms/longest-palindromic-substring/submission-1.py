class Solution:
    def longestPalindrome(self, s: str) -> str:
        # for each character, keep expanding out left and right 
        # ababd # len = 5
        longest = 1
        longest_str = s[0]
        for i in range(len(s)): 
            # odd length
            current_length = 0
            l,r = i,i
           
            while l>=0 and r<len(s) and s[l] == s[r]:
                current_length = r-l + 1
                longest =  max(longest,current_length)
                if current_length >= longest:
                    longest_str = s[l:r+1]


                l = l-1
                r = r+1
        for j in range(len(s)): 
            # odd length
            current_length = 1
            l,r = j,j+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                current_length = r-l + 1
                longest =  max(longest,current_length)
                if current_length >= longest:
                    longest_str = s[l:r+1]
                l = l-1
                r = r+1   
        
        return longest_str

 
        