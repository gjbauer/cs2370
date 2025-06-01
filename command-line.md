




Command Line Cheat Sheet · Classes with Prof. Nat Tuck






















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
5. [Command Line Cheat Sheet](/classes/2024-01/cs2370/command-line/)/

Command Line Cheat Sheet
========================

28 January 2024·328 words·2 mins·





Anyone writing computer programs should be familiar with the command
line interface for their computer. Here’s a quick review of the
absolute basics.

Windows CMD.EXE

[#](#windows-cmdexe)
-------------------------------------

The default command line interface is CMD.EXE, descended from the old
MS DOS interface.

When you open a CMD window, you’ll see something like this:

```
C:\Users\nt1171>

```

There are three parts to that prompt:

* “C:” means this cmd window is currently looking at the C drive.
* “\Users\nt1171” means it’s looking at that directory (a user home directory).
* “>” is the end of the prompt, telling us to type a command.

Basic commands:

* `help` - List available commands
* `help (command)` - List usage info for (command)
* `dir` - List files in current directory.
* `cd (path)` - Change directory to path.
* `move (name) (path)` - Move (or rename) file (name) to (path).
* `copy (name) (path)` - Copy file (name) to (path).
* `python script.py arg1 arg2 ...` - Run a python script.

Path examples:

* `move apple.txt orange.txt` - Both files are in current directory.
* `move apple.txt \users\nt1171` - Desination is absolute path to directory.
* `move apple.txt ..\fruit` - “..” is the parent directory.

Example of some `cd` commands:

```
C:\Users\nt1171> cd Documents
C:\Users\nt1171\Documents> cd ..
C:\Users\nt1171> cd \
C:\>

```

Linux Shell (Mac is basically the same)

[#](#linux-shell-mac-is-basically-the-same)
------------------------------------------------------------------------------------

When you open a shell window you’ll see something like:

```
nat@mint:/home/nat$

```

Four parts to that prompt:

* Current user (nat)
* Current machine name (mint)
* Current path (/home/nat)
* $ prompt (% on Mac) tells you you can type a command. If this is an
  root (admin user) prompt, the last character will be ‘#’.

Linux and Mac use a traditional UNIX style set of commands.

* `man (command)` - View documentation for a command.
* `ls` - List current directory.
* `cd (path)` - Change directory to path.
* `mv (name) (path)` - Move or rename item.
* `cp (name) (path)` - Copy item.
* `python script.py arg1 arg2 ...` - Run a python script.

Example of some `cd` commands:

```
nat@mint:/home/nat$ cd Documents
nat@mint:/home/nat/Documents$ 
nat@mint:/home/nat$ cd /
nat@mint:/$ 

```


![Nat Tuck](/img/author_hu_995db18b97553af7.jpg)
Author

Nat Tuck











---


[←
→
cs2370 Notes: 03 Programming
25 January 2024](/classes/2024-01/cs2370/notes/03-programming/)

[cs2370 Notes: 05 Functions
31 January 2024


→
←](/classes/2024-01/cs2370/notes/05-functions/)





[↑](#the-top "Scroll to top")

©
2025
Nat Tuck

Powered by [Hugo](https://gohugo.io/) & [Blowfish](https://blowfish.page/)













