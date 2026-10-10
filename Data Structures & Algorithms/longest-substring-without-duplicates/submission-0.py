class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window approach? 
        # store p1 at beginning of substring and p2 and end of substring, iterate p2 while the characters are unique (store in a hashmap)
        # we are done when p2 reaches the end of the string
        # if we encounter a duplicate, move p1 up by 1
        # store longest substring

        # p1 = index of the beginning of the substring
        # p2 = index of the end of the substring

        beginning = 0
        end = 0 
        # pwwkew
        # cl = p
        # end = 1
        # ls = 1
        # {p}

        # cl = w
        # end = 2
        # map letter to if we've seen it before
        longest_substring = end - beginning
        letters_to_occurs = {}
        while end < len(s):
            current_letter = s[end]
            # we've not seen this character before
            if current_letter not in letters_to_occurs:
                end +=1
                letters_to_occurs[current_letter] = 1
                if end - beginning > longest_substring:
                    longest_substring = end - beginning
            # it's already in the longest substring
            else:
                letters_to_occurs.pop(s[beginning])
                beginning +=1
                # end += 1
            
        return longest_substring










        