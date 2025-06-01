




cs2370 Notes: 19 Palindromes · Classes with Prof. Nat Tuck






















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
5. [cs2370 Notes: 19 Palindromes](/classes/2024-01/cs2370/notes/19-palindromes/)/

cs2370 Notes: 19 Palindromes
============================

8 March 2024·129 words·1 min·





```
import gzip
import re
file = gzip.open("words.txt.gz", "rt")
words = list(map(lambda xx: xx.strip(), file))
file.close()
def reverse(xx):
    return ''.join(reversed(xx))
def normalize(xx):
    return re.sub(r'\s+', '', xx) 
def is_palindrome(st):
    return st == reverse(st)
def is_palindrome1(xx):
    for ii in range(0, len(xx)):
        if xx[ii] != xx[len(xx) - ii - 1]:
            return False
    return True
def is_palindrome2(xx):
    if len(xx) <= 1:
        return True
    if xx[0] != xx[-1]:
        return False
    return is_palindrome2(xx[1:-1])
    
#for w1 in words:
#    for w2 in words:
#        text = w1 + " " + w2
#        if is_palindrome(text):
#            print(text)
rwords = list(sorted(map(reverse, words)))
ii = 0
jj = 0
while ii < len(words) and jj < len(rwords):
    text = words[ii] + ' ' + reverse(rwords[jj])
    if is_palindrome(text):
        print(text)
    if words[ii] < rwords[jj]:
        ii += 1
    else:
        jj += 1

```


![Nat Tuck](/img/author_hu_995db18b97553af7.jpg)
Author

Nat Tuck











---


[←
→
cs2370 Notes: 17 Recursive Triangles
4 March 2024](/classes/2024-01/cs2370/notes/17-triangles/)

[cs2370 Notes: 20 Classes and Methods
14 March 2024


→
←](/classes/2024-01/cs2370/notes/20-classes-methods/)





[↑](#the-top "Scroll to top")

©
2025
Nat Tuck

Powered by [Hugo](https://gohugo.io/) & [Blowfish](https://blowfish.page/)













