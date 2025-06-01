




cs2370 Notes: 05 Functions · Classes with Prof. Nat Tuck






















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
5. [cs2370 Notes: 05 Functions](/classes/2024-01/cs2370/notes/05-functions/)/

cs2370 Notes: 05 Functions
==========================

31 January 2024·224 words·2 mins·





We’ve been using functions for a while, but where do they come from?

```
def add2(xx):
    return xx + 2

```

And that’s the whole story, any questions?

Maybe it’s a bit more complicated than that.

```
def square(xx):
    return xx * xx
def sqrt(xx):
    guess = 1
    while square(square(guess) - xx) > 0.01:
        guess = 0.5 * (guess + xx / guess)
    return round(guess, 1)

```

Two basic kinds of functions:

```
def say_hello(name):
    print("Hello,", name)
    # return None

```

* Functions that do stuff are said to have side effects.
* Functions that just compute and return a value are said to
  be pure.
* Functions that only exit for their side effects aren’t really
  “functions” - other languages might call them procedures or
  subroutines.

Designing a function:

[#](#designing-a-function)
-------------------------------------------------

* Purpose statement
* Signature (e.g. int -> int)
* Examples
* Stub
* Standard pattern
* Asserts

Design a function to:

* Convert Farenheight to Celsius
  + °C = (°F - 32) × 5/9
* Given a numeric grade and the syllabus, determine if
  we passed the class
* Reverse a string with a loop and an accumulator
  + Standard pattern: Single item or sequence?
  + For sequence, a for loop
* Given a numeric grade and the syllabus, determine the
  letter grade (just the letter part)
* Given two sports teams and their scores (t1, s1, t2, s2),
  determine which team won the game.
* Print a square of a given size with “+-|” characters.

![Nat Tuck](/img/author_hu_995db18b97553af7.jpg)
Author

Nat Tuck











---


[←
→
Command Line Cheat Sheet
28 January 2024](/classes/2024-01/cs2370/command-line/)

[cs2370 Notes: 06 Design With Lists
1 February 2024


→
←](/classes/2024-01/cs2370/notes/06-design-with-lists/)





[↑](#the-top "Scroll to top")

©
2025
Nat Tuck

Powered by [Hugo](https://gohugo.io/) & [Blowfish](https://blowfish.page/)













