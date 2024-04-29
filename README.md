name-builder
===

name-builder is a simple username generator with the goal of providing a diversity of usernams based on list of common names, places, adjectives, and objects.

# Setup

```shell
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install poetry
poetry install
pre-commit install
```

# Usage

```shell
source venv/bin/activate
python -m src.name_builder
```

# Example Output

```text
❯ python -m src.name_builder
['noun:name_generated', 'literal:from', 'adjective:weather', 'noun:moon']
katelin-from-cloudy-caliban
```

# Build

```shell
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install --upgrade pip
$ pip install poetry
$ pip install -e .
$ poetry install
```

# How does it work?

It currently generates 1 username at a time.

First it selects a random form from `forms.csv`, for example.

| term1 | term 2 | term 3 | term 4 | ... |
| --- | --- | --- | --- | --- |
| noun:name_generated | literal:from | noun:city |
| noun:name_generated | literal:from | adjective:weather | noun:moon |

Alternate forms are in forms_unused.csv.  To use them, just move the desired line into forms.cvs.

TODO: Find a good way to select and deselect forms; probably CLI arguments.

Types of terms:

* literal means use the given word on the right side.
* parameter means use an input parameter from the CLI (TODO).
* noun - look up a noun from the list
* adjective - look up an adjective from the list.

noun:name_generated is a list of names, at this time hard coded to medievalish names.

"adjective:weather" means look up a random form of weather.  There's a list of lists, lists.csv which specifies which file to use.

There are numerous lists included.  Some may not even be included in forms, for example mythical_characters.

After resolving all terms, just join them together and print it.

# Testing

Since it uses randomness, it can also set a seed for testing.

# Contributions

Please install the git pre-commit hook.  Only commit if all tests pass.

If you add code, add a unit test.

No global variables.  Stay functional.
