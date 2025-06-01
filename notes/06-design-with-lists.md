




cs2370 Notes: 06 Design With Lists · Classes with Prof. Nat Tuck






















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
5. [cs2370 Notes: 06 Design With Lists](/classes/2024-01/cs2370/notes/06-design-with-lists/)/

cs2370 Notes: 06 Design With Lists
==================================

1 February 2024·280 words·2 mins·





Designing a function:

[#](#designing-a-function)
-------------------------------------------------

* Purpose statement
* Signature (e.g. int -> int)
* Examples
* Stub
* Standard pattern
* Write the body
* Asserts

**Designing a None function**

Print a square of a given size with “+-|” characters.

Signature: int -> None

```
# Print a square with interior size as provided
def print_square(size):
    print "+" + (size * "-") + "+"
    for ii in range(0, size):
        print "|" + (size * " ") + "|"
    print "+" + (size * "-") + "+"

```

**Lists**

A list in Python is the standard way of handling a sequence of 0 or
more items.

Basic operations:

* for / in loop
* Indexing
* Slicing
* .append
* concat with +

**max\_val**

Design a function that finds the maximum value in a list.

Standard pattern:

```
# [number] -> number
def max_val(xs):
    y = 0
    
    for x in xs:
        pass
        
    return y

```

Problem: Negative numbers, solution: xs[0]

Problem: Empty list, solutions:

* None
* Throw

**contains**

Design a function that determines if an integer appears in a list.

Standard pattern:

```
# [int], int -> bool
def contains(xs, y):
    for x in xs:
        ... something with y... 
    return True # or False

```

**add1\_to\_all**

```
# [number] -> [number]
def add1_to_all(xs):
    ys = []
    for x in xs:
        ys.append(x + 1)
    return ys

```
```
# [number] -> None
def add1_to_each(xs):
    for ii in range(0, len(xs)):
        xs[ii] = 

```

**insertion sort**

Pattern gives us:

```
# [number] -> [number]
def sort(xs):
    ys = []
    
    for x in xs:
        ys = insert(ys, x)
    return ys
# We need a helper
# [number], number -> [number]
def insert(xs, y):
    lt = []
    gt = []
   
    for x in xs:
        if x <= y:
            lt.append(x)
        elif x > y:
            gt.append(x)
    
    return lt + [y] + gt

```


![Nat Tuck](/img/author_hu_995db18b97553af7.jpg)
Author

Nat Tuck











---


[←
→
cs2370 Notes: 05 Functions
31 January 2024](/classes/2024-01/cs2370/notes/05-functions/)

[cs2370 Notes: 08 Exploding Bugs
4 February 2024


→
←](/classes/2024-01/cs2370/notes/08-exploding-bugs/)





[↑](#the-top "Scroll to top")

©
2025
Nat Tuck

Powered by [Hugo](https://gohugo.io/) & [Blowfish](https://blowfish.page/)













