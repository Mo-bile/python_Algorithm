from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        output = 0

        s_count = Counter(s)
        is_alone = False

        for c in s_count.values():
            print(c)
            if (c % 2) == 0: # 짝수면
                output += c
            else : # 홀수면
                output += (c - 1)
                is_alone = True
        
        if is_alone == True:
            output += 1


        return output
        