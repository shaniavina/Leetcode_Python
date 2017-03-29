class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a.split('+')
        b = b.split('+')
        first = int(a[0]) * int(b[0]) - int(a[1][:-1]) * int(b[1][:-1])
        second = int(a[0]) * int(b[1][:-1]) + int(b[0]) * int(a[1][:-1])
        return str(first) + '+' + str(second) + 'i'
