class Codec:
    
    def __init__(self):
        self.__random_length = 6
        self.__tiny_url = 'http://tinyurl.com/'
        self.__alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.__lookup = {}
    
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        def getRand():
            rand = []
            for _ in xrange(self.__random_length):
                rand += self.__alphabet[random.randint(0, len(self.__alphabet) - 1)]   #####weird that .append() always doesnt work
            return ''.join(rand)
            
        key = getRand()
        self.__lookup[key] = longUrl
        return self.__tiny_url + key
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.__lookup[shortUrl[len(self.__tiny_url):]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
