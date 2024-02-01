# pynamelix

![Demo gif](https://github.com/casychow/pynamelix/blob/master/ext/demo.gif)

Command line interface API and wrapper for [namelix.com](https://namelix.com)

## Table of Contents
- [Install](#install)
- [Available Commands](#available-commands)
- [Quick Start](#quick-start)
- [To Do](#to-do)

## Install
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
- [ ] Insert Available Commands/Options (-h)
- [ ] Update options
- [ ] Export previous output to a file
