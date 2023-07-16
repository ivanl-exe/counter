# Counter

> 1... 2... 3...

### List of contents:

1. [Brief Introduction](#brief-introduction)
2. [Installation](#installation)
3. [Execution](#execution)
4. [Flags](#flags)
5. [Combinations](#combinations)

## Brief Introductions
A (simple) directory and (plaintext) file counter, written in Python, for counting:
* Characters
* Words
* Lines
* Files
* Directories/folders

If the given path is a **directory**/folder, the **all** nested files and directories will also be included, until each possible edge (directory) has met an endpoint with no further directories within

##Installation
---

For execution python`>=3` needs to be installed, with the [standard library](https://docs.python.org/3/library/), with the additional packages found in `requirements.txt`. These can be installed using `pip` `install` with the `-r` flag - or simply by executing either:

### Powershell

``` shell
./install.ps1
```

### Bourne shell

(Linux, macOS)

``` shell
./install.sh
```

## Execution
---

### Windows

``` shell
python counter.py "path/to/wherever" --flags --go --here
```

### Unix-like

(Linux, macOS)

``` shell
python3 counter.py "path/to/wherever" --flags --go --here
```

## Flags
---

### Characters

For the number of characters, tag a `-c` flag, otherwise for a double-dash (literal) flag:
``` shell
--char
--chars
--character
--characters
```

*including special characters, for example `"\n"` and `"a"` are both 1 character*

### Words

For the number of words, tag a `-w` flag, otherwise for a double-dash (literal) flag:
``` shell
--term
--terms
--word
--words
```

*a word is either separated by spaces `U+0020` or newline `0x000A` (escape sequence `\n`)*

### Lines

For the number of lines, tag a `-l` flag, otherwise for a double-dash (literal) flag:
``` shell
--line
--lines
--newline
--newlines
```

*a line is separated by a newline `0x000A` (escape sequence `\n`), for unix-like systems (including modern Apple macOS) this works, and so too for Microsoft Windows - a newline of `\r\n`*

### Files

For the number of files, tag a `-f` flag, otherwise for a double-dash (literal) flag:
``` shell
--doc
--docs
--document
--documents
--file
--files
```

*determined by `not os.path.isdir(some_path)`, effectively the same as `os.path.isfile(some_path)`*

### Directories/folders

For the number of directories/folders, tag a `-f` flag, otherwise for a double-dash (literal) flag:
``` shell
--dir
--dirs
--directory
--directories
--folder
--folders
--album
--albums
```

*determined by `not os.path.isdir(some_path)`*

## Combinations
---

*flags are commutative, the returned integer is the same (for the same path), no matter the order of flags. For example (the return of) `-fd` is equal to `-df`*

### Single-dash

Following a single-dash `-`, tag on **single character** flags, for example `-fd` would return the **sum** of the number of **files** and **directories**/folders

### Double-dash

For each **literal** flag wanted, tag on, a double-dash `--` (prior), for example `--files --folders` would return the **sum** of the number of **files** and **directories**/folders

*refer above to [flags](#flags), for valid literal flags (subject to extension with updates)*