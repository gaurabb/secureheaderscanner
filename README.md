# HTTP Secure Header Scanner
Basic Python module that provides methods that accept url(s) and return a summary of security centric HTTP response headers that the server sets.

## Installation
Install the extension with using pip. [Pypi Link](https://pypi.python.org/pypi/secureheaderscanner)
```bash
$ pip install secureheaderscanner
```

## Headers scanned
Header Name
| --- |
[Content-Security-Policy (CSP)](http://www.w3.org/TR/CSP2/)
[X-Frame-Options](https://tools.ietf.org/html/draft-ietf-websec-x-frame-options-02) 
[X-XSS-Protection](http://msdn.microsoft.com/en-us/library/dd565647(v=vs.85).aspx) 
[X-Content-Type-Options](http://msdn.microsoft.com/en-us/library/ie/gg622941(v=vs.85).aspx)
[Strict-Transport-Security (HSTS)](https://tools.ietf.org/html/rfc6797)
[X-Download-Options](http://msdn.microsoft.com/en-us/library/ie/jj542450(v=vs.85).aspx)
[X-Permitted-Cross-Domain-Policies](https://www.adobe.com/devnet/adobe-media-server/articles/cross-domain-xml-for-streaming.html)
