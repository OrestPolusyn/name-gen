# pynamelix

[![Supported Python versions](https://img.shields.io/pypi/pyversions/pynamelix)](https://pypi.org/project/pynamelix/)

Command line interface API and wrapper for [namelix.com](https://namelix.com).

This library and command line interface (CLI) program can be used to generate names of businesses, websites, and more to help and inspire you!

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
To be added

[comment]: <> (Name styles: auto, brandable names, evocative, short phrase, compound words, alternate spelling, non-english words, real wors)

[comment]: <> (randomness: low, medium, high)

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
- [ ] Insert print out of Available Commands/Options (-h)
- [ ] Update to include 2024 options
- [ ] Export API output to a file

[comment]: <> ()
