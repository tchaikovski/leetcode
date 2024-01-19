class Solution:

    def romanToInt(self, s: str) -> int:
        rom_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        last = s[-1]
        for t in reversed(s):
            if t == 'C' and last in ['D', 'M']:
                result -= rom_dict[t]
            elif t == 'X' and last in ['L', 'C']:
                result -= rom_dict[t]
            elif t == 'I' and last in ['V', 'X']:
                result -= rom_dict[t]
            else:
                result += rom_dict[t]
            last = t
        return result