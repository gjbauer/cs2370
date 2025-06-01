




cs2370 Notes: 24 Introducing the Web · Classes with Prof. Nat Tuck






















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
5. [cs2370 Notes: 24 Introducing the Web](/classes/2024-01/cs2370/notes/24-the-web/)/

cs2370 Notes: 24 Introducing the Web
====================================

26 March 2024·300 words·2 mins·





What is the Web?

* A protocol: HTTP
* A set of standards for styled, interactive documents: HTML, CSS, JavaScript
  + Plus some standard media formats: gif, png, jpg, mp3, mp4, av1, etc.
* A standard way to specify the *address* of a document or resource: URLs
  + http[s]://host/path
* Concepts: Web page, Web site

What’s a web page?

* One HTML document and associated media

What’s a web site?

* Several HTML documents collected together, typically under a shared base URL
* <https://homework.quest/>
* <https://turing.plymouth.edu/~zshen/>

How does HTTP work?

```
$ cd sample-dir
$ python3 -m http.server

```
```
$ telnet localhost 8000

```

For https

```
openssl s_client -connect homework.quest:443
GET / HTTP/1.1
Host: homework.quest

```

Why did I type “homework.quest” twice?

* The “telnet” command connects to a network server.
* Network servers have numerical addresses.
* Since multiple DNS names can map to one IP, multiple web sites
  can be on one server. The host header allows different host names
  to show different sites.

HTML

[#](#html)
================

HTML is a markup language.

An HTML file is a plain text file that contains HTML tags. These tags
provide document structure and formatting.

```
<!doctype html>
<html>
  <head>
    <title>My Dog</title>
  </head>
  <body>
    <h1>My Dog</title>
    <p>This is my dog. She eats dog food, and human food, and legos, and bees.</p>
    <img src="dog.jpg">
  </body>
</html>

```

Stuff going on here:

* The doctype line specifies the version of HTML. In this case, modern html 5.
* Tags go in angle brackets and come in pairs - an opening tag < foo > is ended by
  a closign tag </ foo >.
* There’s a top level html tag.
* Inside that we have the head for metadata and the body for the
  document content.
* We can specify differnet types of text: headings, paragraphs.
* We can include media - in this case an image.

Dealing with HTML from code:

* Let’s build a tag class to *generate* HTML.

![Nat Tuck](/img/author_hu_995db18b97553af7.jpg)
Author

Nat Tuck











---


[←
→
cs2370 Notes: 23 More Classes and Scopes
24 March 2024](/classes/2024-01/cs2370/notes/23-classes-and-scopes/)

[cs2370 Notes: 25 Web Scraping
29 March 2024


→
←](/classes/2024-01/cs2370/notes/25-web-scraping/)





[↑](#the-top "Scroll to top")

©
2025
Nat Tuck

Powered by [Hugo](https://gohugo.io/) & [Blowfish](https://blowfish.page/)













