class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        if not secret or not guess: 
            return '0A0B'
        
        bulls, cows, digits = 0, 0, [0 ] * 10
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                digits[int(secret[i])] += 1
 
        for i in range(len(secret)):
            if secret[i] != guess[i] and digits[int(guess[i])] != 0:
                cows += 1
                digits[int(guess[i])] -= 1
        return str(bulls) + 'A' + str(cows) + 'B'
