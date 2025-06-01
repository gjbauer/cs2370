




 · Classes with Prof. Nat Tuck




















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
5. [classes](/classes/2024-01/cs2370/practice-exam/)/

1 January 0001·345 words·2 mins·





Practice Exam for CS2370 Spring 2024

[#](#practice-exam-for-cs2370-spring-2024)
================================================================================

Type your answers below the questions and submit the resulting file on
Inkfish.

Part 1. Write down a literal value of each of the following types:

[#](#part-1-write-down-a-literal-value-of-each-of-the-following-types)
------------------------------------------------------------------------------------------------------------------------------------------

**String**

**Integer**

**Float**

**List of Floats**

**Set of Integers**

**A Tuple of an Integer and a String**

Part 2. Design Recipe

[#](#part-2-design-recipe)
-------------------------------------------------

Consider the following code and answer the questions below.

```
def string_lengths(xs):
    ys = []
    for x in xs:
        ys.append(len(x)
    return ys
assert([3, 5] == string_lengths(["one", "seven"]))
# [Int] -> Int
# Sum all the even numbers in the list.
def sum_evens(xs):
    pass
assert(6 == sum_evens[1,2,3,4])

```

**What is the signature of `string_lengths`?**

**What is an appropriate purpose statement for `string_lengths`?**

**What is the standard pattern for `sum_evens`?**

**What is the complete code for `sum_evens`?**

Part 3: Classes and Scopes

[#](#part-3-classes-and-scopes)
===========================================================

Consider the following code and answer the questions below.

```
color = "blue"
rank = 2
class Bar:
    color = "red"
    rank = 6 
    def triple(self):
        return 3 * rank
def foo():
    color = "green"
    class Baz(Bar):
        def double(self):
            return 2 * self.rank
        def grape(self):
            global color
            return "My favorite color is " + color
    return Baz()
aa = foo()
bb = Bar()
print(aa.double())   # print #1
print(aa.triple())   # print #2
print(aa.grape())    # print #3
print(bb.triple())   # print #4

```

**What’s the output from print #1?**

**What’s the output from print #2?**

**What’s the output from print #3?**

**What’s the output from print #4?**

Part 4. Regular Expressions

[#](#part-4-regular-expressions)
-------------------------------------------------------------

Hints:

* `\d` is `[0-9]`
* `\w` is `[a-zA-Z0-9_]`
* `\s` is any whitespace character
* `.` is any character
* `+` means one or more
* mm[0] is the whole match
* mm[1] is the first group (set of parens)

Consider the following code and answer the questions below

```
import re
alice = "Alice Anderson"
bob = "Robert C. Boulette"
pat = r'^(\w+)\s+(\w\.)\s+(\w+)'
mm = re.search(pat, alice)
if mm:
    print(mm[1]) # Print #1
mm = re.search(pat, bob)
if mm:
    print(mm[1]) # Print #2

```

**Does the pattern match `alice`?**

**If so, what gets printed by print #1?**

**Does the pattern match `bob`?**

**If so, what gets printed by print #2?**


![Nat Tuck](/img/author_hu_995db18b97553af7.jpg)
Author

Nat Tuck











---


[1 January 0001


→
←](/classes/2024-01/cs2370/notes/code/images/readme/)





[↑](#the-top "Scroll to top")

©
2025
Nat Tuck

Powered by [Hugo](https://gohugo.io/) & [Blowfish](https://blowfish.page/)













