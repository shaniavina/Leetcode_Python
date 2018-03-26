class Solution:
    def adjustThisLine(self, words, count, length, maxWidth):
        
        left_spaces = maxWidth - length
        if count == 1:
            self.res.append(words[0] + ' ' * left_spaces)
            return
        short = left_spaces // (count - 1)
        longer_count = left_spaces % (count - 1)
        temp = ''
        for i in range(len(words)):
            if i == len(words) - 1:
                temp += words[i]
            elif longer_count:
                temp += words[i] + ' ' * (short + 2)
                longer_count -= 1
            else:
                temp += words[i] + ' ' * (short + 1)
        
        self.res.append(temp)
        
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if not words:
            return []
        count_of_words_this_line = 0
        length_this_line = 0
        words_of_this_line = []
        self.res = []
        for word in words:
            length_next_line = length_this_line + len(word)
            
            if length_this_line > 0:
                length_next_line += 1
            if length_next_line > maxWidth:
                self.adjustThisLine(words_of_this_line, count_of_words_this_line, length_this_line, maxWidth)
                words_of_this_line = [word]
                length_this_line = len(word)
                count_of_words_this_line = 1
            else:
                words_of_this_line.append(word)
                length_this_line = length_next_line
                count_of_words_this_line += 1
        #self.adjustLastLine(words_of_this_line, count_of_words_this_line, length_this_line, maxWidth)
        last_line = ' '.join(words_of_this_line) + ' ' * (maxWidth - length_this_line)
        self.res.append(last_line)
        return self.res

