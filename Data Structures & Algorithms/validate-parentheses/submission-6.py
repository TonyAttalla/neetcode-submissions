class Solution:
    def isValid(self, s: str) -> bool:
        # create a stack
        # if we encounter a close, pop off the stack, check that its the       opposite 
        # we also need the stack to be empty at the end
        
        stack = []
        opposites = {}
        opposites[')'] = '('
        opposites['}'] = '{'
        opposites[']'] = '['

        for elem in s:
            if elem in ['{', '[', '(']:
                stack.append(elem)
            else:
                if not len(stack) or stack.pop() != opposites[elem]:
                    return False

        if len(stack) != 0:
            return False
        return True

     