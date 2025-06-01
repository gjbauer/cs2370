




cs2370 Notes: 27 Web App Server · Classes with Prof. Nat Tuck






















[↓Skip to main content](#main-content)

[Classes with Prof. Nat Tuck](/)

[Home](/)
[cs2370](/classes/2025-01/cs2370/)
[cs2470](/classes/2025-01/cs2470/)
[cs4310](/classes/2025-01/cs4310/)
[Inkfish](https://inkfish.homework.quest/)









* [Home](/)
* [cs2370](/classes/2025-01/cs2370/)
* [cs2470](/classes/2025-01/cs2470/)
* [cs4310](/classes/2025-01/cs4310/)
* [Inkfish](https://inkfish.homework.quest/)





1. </>/
2. [/classes](/classes/)/
3. [Classes, Spring 2024](/classes/2024-01/)/
4. [CS 2370 Spring 2024: Course Site](/classes/2024-01/cs2370/)/
5. [cs2370 Notes: 27 Web App Server](/classes/2024-01/cs2370/notes/27-app-server/)/

cs2370 Notes: 27 Web App Server
===============================

4 April 2024·124 words·1 min·





```
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
class Page:
    def html(self):
        return f'''
        <!doctype html>
        <html>
          <head>
            <title>{self.title}</title>
          </head>
          <body>
            <h1>{self.title}</h1>
            {self.body}
          </body>
        </html>
        '''
    def bytes(self):
        return self.html().encode('utf-8')
class Welcome(Page):
    title = "Welcome!"
    body = '''
    <p>Welcome to our web site.</p>
    <p>We have <a href="/page2">another page</a>.</p>
    '''
class Page2(Page):
    title = "Page 2"
    body = '''
    <p>This is the second page.</p>
    <p>Back to the <a href="/">welcome</a> page?</p>
    '''
    
class Handler(BaseHTTPRequestHandler):
    routes = {
        "/": Welcome,
        "/page2": Page2,
    }
    
    def do_HEAD(self):
        if self.path in self.routes:
            self.send_response(200)
        else:
            self.send_response(404)
    
    def do_GET(self):
        if not self.path in self.routes:
            self.send_response(404)
            return
        
        self.close_connection = True        
        print("path =", self.path)
        self.send_response(200)
        self.send_header("content-type", "text/html; charset=UTF-8")
        self.end_headers()
        page = self.routes[self.path]()
        self.wfile.write(page.bytes())
if __name__ == '__main__':
    server = HTTPServer(('', 8081), Handler)
    server.serve_forever()

```


![Nat Tuck](/img/author_hu_995db18b97553af7.jpg)
Author

Nat Tuck











---


[←
→
cs2370 Notes: 26 More Scraping
30 March 2024](/classes/2024-01/cs2370/notes/26-more-scraping/)

[cs2370 Notes: 28 More App Server
10 April 2024


→
←](/classes/2024-01/cs2370/notes/28-more-app-server/)





[↑](#the-top "Scroll to top")

©
2025
Nat Tuck

Powered by [Hugo](https://gohugo.io/) & [Blowfish](https://blowfish.page/)













