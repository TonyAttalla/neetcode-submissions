class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().strip(" ")
        s = ''.join(ch for ch in s if ch.isalnum())
        print(s)
        end_pointer = len(s)-1
        beginning_pointer = 0

        # store beginning and end pointers
        # while beginning<=end, compare values at end and beginning, if those values
        # are equal, decrement end and increment beginning, else return False

        # return true
        while beginning_pointer <= end_pointer:
            val1 = s[beginning_pointer]
            val2 = s[end_pointer]
            if val1 != val2:
                return False
            beginning_pointer +=1
            end_pointer -=1 
        return True
        