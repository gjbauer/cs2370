




cs2370 Notes: 14 Baby Names · Classes with Prof. Nat Tuck






















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
5. [cs2370 Notes: 14 Baby Names](/classes/2024-01/cs2370/notes/14-baby-names/)/

cs2370 Notes: 14 Baby Names
===========================

25 February 2024·199 words·1 min·





More with Strings

[#](#more-with-strings)
------------------------------------------

Starting with [a file of baby names](../images/baby-names-2002.txt)
from the Social Security Administration, let’s see what we can do.

How many names? Male, female, total?

Build a histogram per first letter.

Hints:

* split
* strip
* replace

Introducing Regular Expressions

[#](#introducing-regular-expressions)
----------------------------------------------------------------------

```
import re
text = "abc123"
re.match(r'a', text)
re.match(r'1', text)
re.match(r'[a-z]', text)
re.match(r'[a-z]+', text)
re.match(r'[a-z]*', text)
re.match(r'[0-9]+', text)
re.match(r'[0-9]*', text)
re.match(r'[a-z]+[0-9]+', text)
re.match(r'\D+\d+', text)
phone = '(603) 555-1212'
pat = r'\(\d{3}\)\s\d{3}-\d{4}'
# Does that look like a phone number?
re.match(pat, phone)
re.fullmatch(pat, phone)
tmpl = '''
Dear {name},
The warranty on your {year} {make} {model} is about to 
expire. This is your last chance to purchase extended
warantee coverage to avoid {disaster1} and {disaster2}.
Please call us at {phone} today!
{sender_name}
The Very Real Waranty Company.
'''
# Find the first template slot.
mm = re.search(r'{[a-z]+}', tmpl)
# That gives us a match object.
mm[0]   # Text of the match
# Group
mm = re.search(r'{([a-z]+)}', tmpl)
mm[0]   # Text of the match
mm[1]   # First group
re.findall(r'{[a-z]+}', tmpl)
re.findall(r'{\w+}', tmpl)
re.findall(r'{(\w+)}', tmpl)
for mm in re.finditer(r'{(\w+)}', tmpl:
    print(mm[0], mm[1])
text1 = re.sub(r'{\w+}', "BOOM", tmpl)
text1 = re.sub(r'{(\w+)}', r"[\1]", tmpl)
def cap(st):
    return st[1].capitalize()
text1 = re.sub(r'{(\w+)}', cap, tmpl)

```


![Nat Tuck](/img/author_hu_995db18b97553af7.jpg)
Author

Nat Tuck











---


[←
→
cs2370 Notes: 13 Bulls, and Pigs
23 February 2024](/classes/2024-01/cs2370/notes/13-pigs/)

[cs2370 Notes: 15 Files and Directories
27 February 2024


→
←](/classes/2024-01/cs2370/notes/15-files-dirs/)





[↑](#the-top "Scroll to top")

©
2025
Nat Tuck

Powered by [Hugo](https://gohugo.io/) & [Blowfish](https://blowfish.page/)













