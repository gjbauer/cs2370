




cs2370 Notes: 38 Semester Review · Classes with Prof. Nat Tuck






















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
5. [cs2370 Notes: 38 Semester Review](/classes/2024-01/cs2370/notes/38-semester-review/)/

cs2370 Notes: 38 Semester Review
================================

2 May 2024·451 words·3 mins·





“Intro to Programming”

* Programming is writing computer programs
* A computer program is typically text written in a programming
  language.
* This semester we’ve written code in Python.

Example 1:

[#](#example-1)
===========================

```
print("Input x")
text = input("> ")
x = int(text)
print("x + 4 =", x + 4)

```

* Write the code in IDLE
* We need to save it before we can run it.
* That means we care about local files and directories.
* This is a plain text file.
  + We can open it in Windows Notepad
  + A program like Microsoft Word won’t work.
* We can run it by:
  + Clicking “run” in the run menu.
  + Pressing F5.
  + Opening up a command line window and running it with the python command.
* A Python program is a series of statements (think “commands”)
* The Python interpreter (a program called “python”) executes the
  program in such a way that it looks like the statements run in
  order.

Flow control

[#](#flow-control)
================================

```
print("Input x")
x = 10
while x > 0:
    text = input("> ")
    x = int(text)
    if x % 2 == 0:
        print("x + 4 =", x + 4)

```

Data types:

[#](#data-types)
=============================

* Numbers: int, float
* Strings
* Collections: list, tuple, dict, set

Functions

[#](#functions)
==========================

```
def add2(xx):
    return xx + 2

```

We spent most of the semester designing functions, but writing code
has the same basic problem as writing prose: It’s hard to know where
to start.

So this semester we used a design recipe:

* Purpose statement
* Signature (e.g. int -> int)
* Tests
* Stub
* Standard pattern
* Write the body

Design with lists

[#](#design-with-lists)
==========================================

Insertion sort:

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

Design with Dictionaries

[#](#design-with-dictionaries)
========================================================

Design a method that takes a list of numbers and returns a list of how
many times the number in that position appeared in the lsit.

Example: [7, 7, 1, 7, 2, 2, 7, 1, 3] -> [4, 4, 2, 4, 2, 2, 4, 2, 1]

```
version 1: nested loop
version 2: two loops and a dictionary

```

How many times through a loop in each case?

Directory Trees and Recursion

[#](#directory-trees-and-recursion)
==================================================================

```
from pathlib import Path
def search(path):
    for item in path.iterdir():
        if item.is_dir():
            search(item)
        else:
            print(item)
wd = Path.cwd()
search(wd)

```

Web Scraping

[#](#web-scraping)
================================

* Vault example
* Show latest versions

ConsList / Binary Trees

[#](#conslist--binary-trees)
=====================================================

* Recursive data

AI, Word Game

[#](#ai-word-game)
=================================

* Generating pictures was fun.
* The Intermediate Programing are done, so now it’s time
  to beat them. The highest real name on the leaderboard
  is Job Bonestoppel…

![Nat Tuck](/img/author_hu_995db18b97553af7.jpg)
Author

Nat Tuck











---


[←
→
cs2370 Notes: 37 Practice Exam
30 April 2024](/classes/2024-01/cs2370/notes/37-practice-exam/)






[↑](#the-top "Scroll to top")

©
2025
Nat Tuck

Powered by [Hugo](https://gohugo.io/) & [Blowfish](https://blowfish.page/)













