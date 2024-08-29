class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort() # kid
        s.sort() # cookie
        print(s)
        print(g)
        output = 0
        g_index = 0
        s_index = 0

        while g_index < len(g) and s_index < len(s):
            if s[s_index] >= g[g_index] :
                print(s_index)
                print(g_index)
                s_index += 1
                g_index += 1
                output += 1
            else :
                s_index += 1
        return output
        # for cookie in s :
        #     if g is None : return output
        #     for kid in g:
        #         if cookie >= kid :
        #             print(cookie)
        #             print(kid)
        #             output += 1
        #             g = g[1:]
        #             continue
        # return output
        