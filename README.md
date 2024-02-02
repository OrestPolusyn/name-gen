# pynamelix

[![Supported Python versions](https://img.shields.io/pypi/pyversions/pynamelix)](https://pypi.org/project/pynamelix/)

Command line interface API and wrapper for [namelix.com](https://namelix.com).

This library and command line interface (CLI) program can be used to generate names of businesses, websites, and more to help and inspire you with your project!

Note: This repository was intended to update the pynamelix library with the updated options on [namelix.com](https://namelix.com). However, since I am unable to find the generation options provided by the server, apart from the previously documented options, I cannot continue developing this project.

![Demo gif](https://github.com/casychow/pynamelix/blob/master/ext/demo.gif)

# Table of Contents
- [Installation](#installation)
- [Available Commands](#available-commands)
- [Quick Start](#quick-start)
- [To Do](#to-do)

## Installation
From PyPi:
```
pip install pynamelix
```

From this repo:
```
git clone https://github.com/casychow/pynamelix
pip install .
```

From [original repo](https://github.com/axju/pynamelix):
```
git clone https://github.com/axju/pynamelix
pip install .
```

## Available Commands
```
usage: pynamelix [-h] [-V] [-v] [-p] [-s {multiword,brandable,language,wordmix,spelling,dictionary,rhyme,person}] [-l {short,medium,long}]
                 [-f FILENAME]
                 keywords [keywords ...]

positional arguments:
  keywords              A word or words to base the word generator on. Multiple words should be separated by a space (' ').

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         Show program version.
  -v, --verbose
  -p, --pypi
  -s {multiword,brandable,language,wordmix,spelling,dictionary,rhyme,person}, --styles {multiword,brandable,language,wordmix,spelling,dictionary,rhyme,person}
                        Select a preferred STYLE of your generated words.
  -l {short,medium,long}, --lengths {short,medium,long}
                        Select a preferred LENGTH of your generated words.
  -f FILENAME, --filename FILENAME
                        Write API output to a file.
```


[comment]: <> (New options available in 2024)
[comment]: <> (Name styles: auto, brandable names, evocative, short phrase, compound words, alternate spelling, non-english words, real words)
[comment]: <> (randomness: low, medium, high)
[comment]: <> (optional settings: blacklist words - Words, prefixes or suffixes that should not be generated - separate with commas)


## Quick Start
To display available commands:
```
python -m pynamelix -h
```

Example command to run the program using the `wordmix` option to create words of `medium` length based on the word `axju`:
```
python -m pynamelix -p -s wordmix -l medium python axju
```

## To Do
- [x] Insert print out of Available Commands/Options (-h)
- [ ] Update to include 2024 options (cannot be done)
- [x] Export API output to a file
- [ ] Recursively run API to produce outputs related to the number of styles and word length

[comment]: <> ()