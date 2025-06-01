




cs2370 Notes: 13 Bulls, and Pigs · Classes with Prof. Nat Tuck






















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
5. [cs2370 Notes: 13 Bulls, and Pigs](/classes/2024-01/cs2370/notes/13-pigs/)/

cs2370 Notes: 13 Bulls, and Pigs
================================

23 February 2024·234 words·2 mins·





Design a Game

[#](#design-a-game)
----------------------------------

Bulls and Pigs:

* The computer generates a random 4 digit secret.
* The user repeatedly guesses a random four digit sequence.
* After each guess, the computer scores the guess:
  + One bull for each digit in the guess that appears in the secret
    in the same position.
  + One pig for each digit in the guess that appears in the secret
    in a different position.
* When the user correctly guesses the secret, they win.
* The goal is to win in the fewest guesses.

```
import random
# Create a new 4 digit secret.
# None -> str
def new_secret():
    yy = ""
    for _ in range(0, 4):
        yy += str(random.randint(0,10))
    return yy
# Check if guess is valid.
# str -> bool
def valid_guess(gg):
    return len(gg) == 4 and gg.isdigit():
# str -> (int, int)
def score_guess(secret, gg):
    bulls = 0
    pigs = 0
    for ii in range(0, gg):
       pass 
    return (bulls, pigs)
# None -> None
def main():
    secret = new_secret()
    guess = ""
    while not guess == secret:
        print("")
        print("Guess a 4 digit number")
        guess = input("> ")
        if valid_guess(gg):
            print("Your guess:", guess)
            (bulls, pigs) = score_guess(secret, guess)
        else:
            print("Bad guess")
    print("You win!")
if __name__ == '__main__':
    main()

```

More with Strings

[#](#more-with-strings)
------------------------------------------

Starting with a file of baby names from the Social Security
Administration, let’s see what we can do.

How many names? Male, female, total?

Build a count-chart per first letter.


![Nat Tuck](/img/author_hu_995db18b97553af7.jpg)
Author

Nat Tuck











---


[←
→
cs2370 Notes: 12 Strings
20 February 2024](/classes/2024-01/cs2370/notes/12-strings/)

[cs2370 Notes: 14 Baby Names
25 February 2024


→
←](/classes/2024-01/cs2370/notes/14-baby-names/)





[↑](#the-top "Scroll to top")

©
2025
Nat Tuck

Powered by [Hugo](https://gohugo.io/) & [Blowfish](https://blowfish.page/)













