class Solution:
    def isValid(self, s: str) -> bool:
        # iterate through the string once
        # push each character to s1
        # we must check that at every step, the beginning of the array
        # and end of the array are the same, then remove them 
        # reverse the string and iterate again, pushing to s2

        # compare s1.pop() to s2.pop(), the values must be the corresponding open and close       brackets of the array 
        # and they must both be empty

        valid_chars = [ '(', ')', '{', '}', '[', ']']
        stack = []
        opposites = {}
        opposites['('] = ')'
        opposites[')'] = '('
        opposites['{'] = '}'
        opposites['}'] = '{'
        opposites['['] = ']'
        opposites[']'] = '['
        for elem in s:
            if elem in ['(', '{', '[']:
                stack.append(elem)
            elif elem in [')', '}', ']']:
                if len(stack) == 0:
                    return False
                opposite = stack.pop()
                if opposites[elem] != opposite:
                    return False
        if len(stack) == 0:
            return True
        return False


        
    



        