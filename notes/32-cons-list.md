




cs2370 Notes: 32 ConsList · Classes with Prof. Nat Tuck






















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
5. [cs2370 Notes: 32 ConsList](/classes/2024-01/cs2370/notes/32-cons-list/)/

cs2370 Notes: 32 ConsList
=========================

18 April 2024·208 words·1 min·





**Make Up Opportunities**

Next week’s lab will be an opportunity to resubmit a previous lab.

Next week’s homework will be the opportunity to resubmit a previous
homework.

If you have a bunch of bad homework grades, you can resubmit some
extra homeworks - not to exceed 1 in 3 homeworks that have scores
below 50%.

**ConsList**

```
class Empty():
    # ConsList -> String
    def __str__(self):
        return "()"
    # ConsList -> boolean
    def isEmpty(self):
        return True
empty = Empty()
class Cons:
    # constructor
    def __init__(self, first, rest):
        self.first = first
        self.rest = rest
    # ConsList -> String
    def __str__(self):
        if self.rest.isEmpty():
            return f"({self.first})"
        else:
            rest = str(self.rest)[1:-1]
            return f"({self.first}, {rest})"
    # ConsList -> boolean
    def isEmpty(self):
        return False
# Any, Any, ... -> ConsList
def list(*items):
    if len(items) == 0:
        return empty
    else:
        return Cons(items[0], list(*items[1:]))
def add1_to_all(xs):
    if xs.isEmpty():
        return empty
    else:
        return Cons(2 * xs.first, add1_to_all(xs.rest))
# Map example
# Filter example
# Reduce example
# Map from reduce
    
# (ConsList of Number) -> Number
def sum(xs):
    if xs.isEmpty():
        return 0
    else:
        return xs.first + sum(xs.rest)
# ConsList -> Number
def length(xs):
    if xs.isEmpty():
        return 0
    else:
        return 1 + length(xs.rest)
if __name__ == '__main__':
    xs = Cons(1, Cons(2, Cons(3, empty)))
    ys = list(1, 2, 3)
    print(ys)
    print(sum(ys))

```


![Nat Tuck](/img/author_hu_995db18b97553af7.jpg)
Author

Nat Tuck











---


[←
→
cs2370 Notes: 30 Spreadsheets
14 April 2024](/classes/2024-01/cs2370/notes/30-spreadsheets/)

[cs2370 Notes: 33 Binary Tree
22 April 2024


→
←](/classes/2024-01/cs2370/notes/33-binary-tree/)





[↑](#the-top "Scroll to top")

©
2025
Nat Tuck

Powered by [Hugo](https://gohugo.io/) & [Blowfish](https://blowfish.page/)













