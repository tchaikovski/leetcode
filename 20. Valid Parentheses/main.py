class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1: return False
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []
        for char in s:
            if char not in mapping:
                stack.append(char)
            elif not stack or mapping[char] != stack.pop(): return False
        return len(stack) == 0


tt = Solution()
s = "(}{)"
strings = ("[", "([)", "()", "{((}", "()[]{}", "{[]}", "(){}}{", "((){})[]", "(}{)", "[({(())}[()])]")
# strings = ("[](([[]]){}{[]}([]))",)
for s in strings:
    # tt.isValid(s)
    print(s)
    print(tt.isValid(s))
