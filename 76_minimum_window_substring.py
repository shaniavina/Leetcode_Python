class Solution(object):
    def minWindow(self, string, target):
        """
        :type string: str
        :type target: str
        :rtype: str
        """
        # counter represents the number of chars of t to be found in s
        target_map = collections.Counter(target)

        count = len(target)
        start = end = head = 0
        min_substring_length = len(s) + 1
        # Move end to find a valid window.
        while end < len(string):
            #if character doesn't exist in map it returns 0
            if target_map[string[end]] > 0:
                count -= 1
            target_map[string[end]] -= 1
            end += 1
            # When we found a valid window, move start to find smaller window.
            while count == 0:
                if (end - start) < min_substring_length:
                    min_substring_length = end - start
                    head = start
                target_map[string[start]] += 1
                # When char exists in target, increase counter.
                if target_map[string[start]] >0:
                    count += 1

                start += 1
        return "" if min_substring_length == len(s) + 1 else string[head:head + min_substring_length]
