




cs2370 Notes: 03 Programming · Classes with Prof. Nat Tuck






















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
5. [cs2370 Notes: 03 Programming](/classes/2024-01/cs2370/notes/03-programming/)/

cs2370 Notes: 03 Programming
============================

25 January 2024·222 words·2 mins·





General Advice

[#](#general-advice)
------------------------------------

* Attendence is strongly recommended.
* Also, eating and sleeping.

Python: Parts of speech

[#](#python-parts-of-speech)
-----------------------------------------------------

* Literals:
  + int (`type(5)`)
  + float
  + string (in quotes)
  + boolean
* Variable names
  + (no quotes)
  + starts with a letter, numbers and “\_” allowed after
* Operators
  + 3 + 7
* Function calls
  + round(7.3555, 2)
* Expressions:
  + An expression has a value.
  + Literals
  + Operations
  + Some function calls
    - In other languages, “function” may be seperated from
      “procedure” or “subroutine”.

Arithmetic

[#](#arithmetic)
----------------------------

**Numbers**

```
>>> 1 + 2
>>> 2 - 4
>>> 3 * 7
>>> 5 / 3

>>> 5 // 3
>>> 5 % 3         # modulus, not remainder

```

**Strings**

```
>>> "zz" + "XX"
>>> "hello " * 3

```

Making choices

[#](#making-choices)
------------------------------------

Conditionals:

* if
* if / else

```
print("one")
if True:   # False:
    print("two")
#else:
#    print("three")
print("four")

```

Boolean Expressions:

```
>>> True and True
>>> True and False
>>> True or True
>>> True or False
>>> not True

```

* Write out the truth tables for those.

Example:

```
aa = int(input("aa = "))
bb = int(input("aa = "))

if aa > 10 and bb > 10:
   print("Both")

if aa > 10 or bb > 10:
   print("Either)
   
if aa <= 10 && bb <= 10:
    print("Neither")

```

Example 2:

```
word = input("enter word: ")

if word < "n":
    print(word.capitalize())
else:
    print(word)

```

While loops:

* while
* let’s write a script that left-pads strings to 40 chars in
  a loop

![Nat Tuck](/img/author_hu_995db18b97553af7.jpg)
Author

Nat Tuck











---


[←
→
cs2370 Notes: 04 Lists and Scripts
25 January 2024](/classes/2024-01/cs2370/notes/04-lists-and-scripts/)

[Command Line Cheat Sheet
28 January 2024


→
←](/classes/2024-01/cs2370/command-line/)





[↑](#the-top "Scroll to top")

©
2025
Nat Tuck

Powered by [Hugo](https://gohugo.io/) & [Blowfish](https://blowfish.page/)













