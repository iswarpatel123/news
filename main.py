import urllib.request
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

def fetch_html(url):
    response = urllib.request.urlopen(url, context=ssl._create_unverified_context())
    return response.read()

# url = "https://newsfilter.io/"
url = "https://www.marketscreener.com/"
html = fetch_html(url)
print(html)