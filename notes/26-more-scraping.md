




cs2370 Notes: 26 More Scraping · Classes with Prof. Nat Tuck






















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
5. [cs2370 Notes: 26 More Scraping](/classes/2024-01/cs2370/notes/26-more-scraping/)/

cs2370 Notes: 26 More Scraping
==============================

30 March 2024·139 words·1 min·





HTML Attributes

* Each tag has attributes.
* These are key-value pairs, so it’s a dictionary.
* Two are especially important.
* The “id” is a unique string that indentifies that tag.
* The “class” is a space-separated collection of non-unique strings.

```
import requests
import bs4
resp = requests.get("https://homework.quest/")
resp.status_code
resp.raise_for_status()
resp.text
tree = bs4.BeautifulSoup(resp.text, 'html.parser')
xs = tree.select('p.ball__number')
for x in xs: print("[", x, "]")

```

* ‘#foo’
* ‘.foo’
* soup.select(‘input[type=“button”]’)
* spanElem.get(‘id’)

The Lottery

[#](#the-lottery)
------------------------------

<https://nhlottery.com/Winning-Numbers>

* There’s a class for each game.
* There’s a class for numbers.
* Print out numbers.

Introducing Selenium

[#](#introducing-selenium)
------------------------------------------------

Sometimes it’s useful to just do the HTTP request, get the result, and
process it.

Sometimes you want an actual web browser that will do things like running
JavaScript.

```
$ python -m pip install selenium

```
```
browser = webdriver.Firefox()
browser.get("https://vault.homework.quest")

```

We’re going to explore the textbook to figure out how to hack the vault.


![Nat Tuck](/img/author_hu_995db18b97553af7.jpg)
Author

Nat Tuck











---


[←
→
cs2370 Notes: 25 Web Scraping
29 March 2024](/classes/2024-01/cs2370/notes/25-web-scraping/)

[cs2370 Notes: 27 Web App Server
4 April 2024


→
←](/classes/2024-01/cs2370/notes/27-app-server/)





[↑](#the-top "Scroll to top")

©
2025
Nat Tuck

Powered by [Hugo](https://gohugo.io/) & [Blowfish](https://blowfish.page/)













