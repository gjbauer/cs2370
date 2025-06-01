




cs2370 Notes: 18 Scopes and Debuggers · Classes with Prof. Nat Tuck






















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
5. [cs2370 Notes: 18 Scopes and Debuggers](/classes/2024-01/cs2370/notes/18-scopes-and-debuggers/)/

cs2370 Notes: 18 Scopes and Debuggers
=====================================

4 March 2024·271 words·2 mins·





First, let’s try to install the Mu editor.

<https://codewith.mu/>

What’s Mu?

* An alternative to IDLE
* Not installed by default with Python
* Comes with a bunch of packages
* The debugger does more of what I want today.

How do names work in Python?

[#](#how-do-names-work-in-python)
---------------------------------------------------------------

```
# global variable
color = "green"
def add1(xx):
    # xx is a parameter
    # yy is a local variable
    # parameters are just local variables that are created as
    # part of the function call process
    yy = xx + 1
    return yy
    
print(add1(5))

```

Globals are available in functions:

```
nn = 7
def add_nn(xx):
    return xx + nn
  
print(add_nn(3))
# >>> nn = 8
# >>> add_nn(3)

```

Assignment creates new local by default:

```
nn = 0
def set_nn_to_5():
    # global nn
    nn = 5
    print("new nn =", nn)

```

There are no block scopes:

```
def foo():
    if True:    # if False:
        x = 2
    
    print(x)
foo()

```

There are nested functions:

```
def nested_add1(xx):
    def add1():
        return xx + 1
    return add1()

```

Now let’s figure this example out:

```
def make_counter():
    count = 0
    
    def counter():
        nonlocal count
        count += 1
        return count
    return counter
aa = make_counter()
print(aa())
bb = make_counter()
print(aa())
print(bb())

```

So there are four scopes:

* local
* nonlocal
* global
* builtin - stuff like “print” that’s availble everywhere

In python there is only one kind of name. So all of:

* variables containing normal data
* functions
* modules
* classes (we’ll talk more about those later)

all share the same names

Functions to debug:

```
items = [[0, 1, 2, 3], 4, [5, 6, [7, 8]], 9]
def sum_nested(xs):
    sum = 0
    
    if type(xs) is list:
        for xx in xs:
            sum_nested(xs)
    else:
        return xs

```


![Nat Tuck](/img/author_hu_995db18b97553af7.jpg)
Author

Nat Tuck











---


[←
→
cs2370 Notes: 16 Directory Trees and Recursion
29 February 2024](/classes/2024-01/cs2370/notes/16-dir-trees-recursion/)

[cs2370 Notes: 17 Recursive Triangles
4 March 2024


→
←](/classes/2024-01/cs2370/notes/17-triangles/)





[↑](#the-top "Scroll to top")

©
2025
Nat Tuck

Powered by [Hugo](https://gohugo.io/) & [Blowfish](https://blowfish.page/)













