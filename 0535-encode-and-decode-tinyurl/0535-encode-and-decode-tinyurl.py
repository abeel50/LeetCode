class Codec:
    def __init__(self):
        self.urls= defaultdict(str)

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        h = str (hash(longUrl))
        self.urls[h] = longUrl
        return h
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.urls[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))