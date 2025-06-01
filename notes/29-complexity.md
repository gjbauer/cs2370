




cs2370 Notes: 29 Program Complexity · Classes with Prof. Nat Tuck






















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
5. [cs2370 Notes: 29 Program Complexity](/classes/2024-01/cs2370/notes/29-complexity/)/

cs2370 Notes: 29 Program Complexity
===================================

11 April 2024·132 words·1 min·





**Homework is Up**

* The webserver assignment didn’t come out good enough,
  so you get reading and image manipulation.

**The Next Few Weeks**

* After today, there’s 4 weeks in the seemster
  + Bonus Topic 1
  + Bonus Topic 2
  + Last week: Redo and Review
  + Then Final Exam; there will be a sample final

**Today: Computational Complexity**

Last time: recursive Fibonacci

```
def fib(x):
    if x <= 1:
        return x
        
    return fib(x-1) + fib(x-2)

```
```
def fibCalls(x):
    if x <= 1:
        return (x, 1)
    
    (y1, c1) = fib(x-1)
    (y2, c1) = fib(x-2)
    return (y1 + y2, c1 + c2 + 1)

```

Bounds:

* `1, log n, n, n^2, 2^n`
* Compare bounds functions to fib

More strategies:

* Iteration
* Memoization
  + fib is “pure”
  + so memoFib can cheat

More tasks:

* Enumrating prime numbers
  + memo with array?
* Sorting
  + bogo-sort
  + insertion sort
  + merge sort

![Nat Tuck](/img/author_hu_995db18b97553af7.jpg)
Author

Nat Tuck











---


[←
→
cs2370 Notes: 28 More App Server
10 April 2024](/classes/2024-01/cs2370/notes/28-more-app-server/)

[cs2370 Notes: 31 Most Degrees
14 April 2024


→
←](/classes/2024-01/cs2370/notes/31-most-degrees/)





[↑](#the-top "Scroll to top")

©
2025
Nat Tuck

Powered by [Hugo](https://gohugo.io/) & [Blowfish](https://blowfish.page/)













