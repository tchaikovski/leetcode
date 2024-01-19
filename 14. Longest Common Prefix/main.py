from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_string = min(strs, key=len)
        n = len(shortest_string)
        while n > 0:
            check = []
            for i in strs:
                if i.startswith(shortest_string[:n]):
                    check.append(True)
                else:
                    check.append(False)
            if False in check:
                n -= 1
            else:
                return shortest_string[:n]
        return ''
