




cs2370 Notes: 33 Binary Tree · Classes with Prof. Nat Tuck






















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
5. [cs2370 Notes: 33 Binary Tree](/classes/2024-01/cs2370/notes/33-binary-tree/)/

cs2370 Notes: 33 Binary Tree
============================

22 April 2024·187 words·1 min·





**Make Up Opportunities**

Next week’s lab will be an opportunity to resubmit a previous lab.

Next week’s homework will be the opportunity to resubmit a previous
homework.

If you have a bunch of bad homework grades, you can resubmit some
extra homeworks - not to exceed 1 in 3 homeworks that have scores
below 50%.

**ConsList**

```
class Leaf():
    # ConsList -> String
    def __str__(self):
        return "()"
    # ConsList -> boolean
    def isLeaf(self):
        return True
leaf = Empty()
class Branch:
    # constructor
    def __init__(self, left, data, right):
        self.left = left
        self.data = data
        self.right = right
    # ConsList -> String
    def __str__(self):
        return f"({self.left} {self.data} {self.right})"
    # ConsList -> boolean
    def isEmpty(self):
        return False
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
cs2370 Notes: 32 ConsList
18 April 2024](/classes/2024-01/cs2370/notes/32-cons-list/)

[cs2370 Notes: 35 Jupyter Notebook
23 April 2024


→
←](/classes/2024-01/cs2370/notes/35-jupyter/)





[↑](#the-top "Scroll to top")

©
2025
Nat Tuck

Powered by [Hugo](https://gohugo.io/) & [Blowfish](https://blowfish.page/)













