




cs2370 Notes: 09 Dictionaries · Classes with Prof. Nat Tuck






















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
5. [cs2370 Notes: 09 Dictionaries](/classes/2024-01/cs2370/notes/09-dictionaries/)/

cs2370 Notes: 09 Dictionaries
=============================

11 February 2024·222 words·2 mins·





Designing a function

[#](#designing-a-function)
------------------------------------------------

* Purpose statement
* Signature (e.g. int -> int)
* Examples
* Stub
* Standard pattern
* Write the body
* Asserts

New data type: Dictionaries

[#](#new-data-type-dictionaries)
-------------------------------------------------------------

```
legs = {
    'dog': 4,
    'chicken': 2,
    'cat': 4,
    'spider': 8,
}
print(legs['dog'])
legs.keys())
legs.values()
'dog' in legs
'giraffe' in legs
legs.get('giraffe', 4)
legs.get('lobster', 4)

```

Note: Dictionary keys may print in insertion order, but generally it’s
best to think of dictionaries as being unordered.

Not a new capacity:

```
legs_list = [
  ('dog', 4),
  ('chicken', 2),
  ('cat', 4),
  ('spider', 8),
]
def get(xs, key):
    for (kk, vv) in xs:
        if kk == key:
            return vv
    raise Exception("key not found")
print(get(legs_list, 'dog'))

```

How many steps does it take to look up a key in the list?

Dictionaries give us two benefits over association lists:

* Nicer syntax
* Faster (can lookup in 1 step rather than having to loop)

Repeats

[#](#repeats)
----------------------

Design a method that takes a list of numbers and returns a list of how
many times the number in that position appeared in the lsit.

Example: [7, 7, 1, 7, 2, 2, 7, 1, 3] -> [4, 4, 2, 4, 2, 2, 4, 2, 1]

* version 1: nested loop
* version 2: two loops and a dictionary

How many times through a loop in each case?

Next example:

* Calculate a recipt total for a list of (item, count, price each) tuples.

![Nat Tuck](/img/author_hu_995db18b97553af7.jpg)
Author

Nat Tuck











---


[←
→
cs2370 Notes: 07 More Lists
4 February 2024](/classes/2024-01/cs2370/notes/07-more-lists/)

[Design Recipe
15 February 2024


→
←](/classes/2024-01/cs2370/design-recipe/)





[↑](#the-top "Scroll to top")

©
2025
Nat Tuck

Powered by [Hugo](https://gohugo.io/) & [Blowfish](https://blowfish.page/)













