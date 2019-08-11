class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        numeral_map = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
        key_set, res = sorted(numeral_map.keys(), reverse = True), ''
        while num > 0:
            for key in key_set:
                while num / key > 0:
                    num -= key
                    res += numeral_map[key]
        return res
