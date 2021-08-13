# flake8-functions-names

[![PyPI version](https://badge.fury.io/py/flake8-functions-names.svg)](https://badge.fury.io/py/flake8-functions-names)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flake8-functions-names)

An extension for flake8 that validates functions names, decomposition and
conformity with annotations. The plugin also has some validations
of [deal](https://github.com/life4/deal) contracts.

This plugin helps to provide better naming for functions.
The validations are based on my articles:

- [Python functions naming: an algorithm](https://melevir.medium.com/python-functions-naming-the-algorithm-74320a18278d)
- [Python functions naming: 10 tips](https://melevir.medium.com/python-functions-naming-tips-376f12549f9)

`deal`-related validations are enabled only if `deal` is installed.
They are disabled otherwise.

## Installation

```terminal
pip install flake8-functions-names
```

## Example

```python
def is_user_banned(user: User) -> str:
    return 'is_banned' if user.id in BANNED_USERS else 'not_banned'

def save_user(user: User) -> None:
    user.save()
```

Usage:

```terminal
$ flake8 test.py
text.py:1:35: FNE001 Name of function says, that is should return bool, but it returns str
text.py:4:4: FNE003 Name of the function uses "save", but not uses "to"
```

Tested on Python 3.8+ and flake8 3.9+.

## Error codes

| Error code |                     Description          |
|:----------:|:----------------------------------------:|
|   FNE001   | Name of the function says, that is should return `bool`, but it returns *actual_type* |
|   FNE002   | The method has a `@property` decorator, but has a verb in it's name (*verb*) |
|   FNE003   | Name of the function uses `save`, but not uses `to` |
|   FNE004   | Name of the function uses `load`, but not uses `from` |
|   FNE005   | Return type of the function is bool, but the name doesn't show it |
|   FNE006   | Name of function says, that it works with data, so it should be pure, but it has no `@deal.pure()` |
|   FNE007   | `and` is not recommended in functions names |
|   FNE008   | Name of functions ends with it's first argument name |
