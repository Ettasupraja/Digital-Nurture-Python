import hashlib

class URLShortener:
    def __init__(self):
        self.urls = {}

    def shorten(self, url):
        short_code = hashlib.md5(url.encode()).hexdigest()[:6]
        self.urls[short_code] = url
        return short_code

    def retrieve(self, short_code):
        return self.urls.get(short_code, "URL not found")

shortener = URLShortener()

url = "https://www.google.com"
code = shortener.shorten(url)

print("Short Code:", code)
print("Original URL:", shortener.retrieve(code))
