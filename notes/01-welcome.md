




cs2370 Notes: 01 Welcome · Classes with Prof. Nat Tuck






















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
5. [cs2370 Notes: 01 Welcome](/classes/2024-01/cs2370/notes/01-welcome/)/

cs2370 Notes: 01 Welcome
========================

20 January 2024·341 words·2 mins·





Intro to programming first day

Hello

[#](#hello)
------------------

* Hello
* Programming
  + Computers are pretty useful
  + Computers run code that transforms data
  + Let’s figure out this code and data stuff
* Attendence

Syllabus

[#](#syllabus)
------------------------

* Attendence is strongly recommended.
  + Also, eating and sleeping.
* The lecture and lab are one course.
* Lab assignments are the largest grade component. You’ll work
  in pairs and write code.
* The final exams are on paper, and really will include writing code with
  a pencil.
* We’ll see an autograding example in lab tomorrow.
* There will be tutoring at some point.
* Please don’t cheat.

Introducing Python Code

[#](#introducing-python-code)
------------------------------------------------------

```
print("One")
print("Two")
print("Three")

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
* The print function prints something out.

```
print("Input x")
text = input("> ")
x = int(text)
print("x + 4 =", x + 4)

```

This example has a several new compliications:

* The “input” function reads a line of text from the user.
* Execution of the program stops until the user finishes typing and presses enter.
* We can store things in variables, giving them a name so we can refer to them later.
* We have two different types of value: strings and integers.
* Functions sometimes accept more than one argument, seperated by commas.

Interactive examples:

```
>>> 3 + 2
>>> a = 3
>>> a + 2

>>> "3" + 2
>>> int("3")
>>> '3'
>>> str(3)
>>> 2 + int("3")
>>> "2" + str(3)

>>> print("hi")
>>> print("a", "b")
>>> print("a", 3, "b")
>>> type('hi')
>>> type(3)
>>> type(3 / 2)

```

![Nat Tuck](/img/author_hu_995db18b97553af7.jpg)
Author

Nat Tuck











---


[←
→
CS 2370 Spring 2024: Syllabus
8 January 2024](/classes/2024-01/cs2370/syllabus/)

[cs2370 Notes: Lab 01 - Introducing our Tools
22 January 2024


→
←](/classes/2024-01/cs2370/notes/lab01-tools/)





[↑](#the-top "Scroll to top")

©
2025
Nat Tuck

Powered by [Hugo](https://gohugo.io/) & [Blowfish](https://blowfish.page/)













