




cs2370 Notes: 25 Web Scraping · Classes with Prof. Nat Tuck






















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
5. [cs2370 Notes: 25 Web Scraping](/classes/2024-01/cs2370/notes/25-web-scraping/)/

cs2370 Notes: 25 Web Scraping
=============================

29 March 2024·44 words·1 min·





```
import requests
resp = requests.get("https://homework.quest/")
resp.status_code
resp.raise_for_status()
resp.text

```

Scraping Wikipedia:

* Trying to use regex
* main

```
import requests
import bs4
resp = requests.get("https://homework.quest/")
resp.status_code
resp.raise_for_status()
resp.text
tree = bs4.BeautifulSoup(resp.text, 'html.parser')
xs = tree.select('a')
for x in xs: print("[", x, "]")

```

* ‘#foo’
* ‘.foo’
* soup.select(‘input[type=“button”]’)
* spanElem.get(‘id’)
* <https://en.wikipedia.org/wiki/List_of_Pok%C3%A9mon>

![Nat Tuck](/img/author_hu_995db18b97553af7.jpg)
Author

Nat Tuck











---


[←
→
cs2370 Notes: 24 Introducing the Web
26 March 2024](/classes/2024-01/cs2370/notes/24-the-web/)

[cs2370 Notes: 26 More Scraping
30 March 2024


→
←](/classes/2024-01/cs2370/notes/26-more-scraping/)





[↑](#the-top "Scroll to top")

©
2025
Nat Tuck

Powered by [Hugo](https://gohugo.io/) & [Blowfish](https://blowfish.page/)













