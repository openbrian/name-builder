"""The main entry point into this package when run as a script."""

# For more details, see also
# https://docs.python.org/3/library/runpy.html
# https://docs.python.org/3/reference/import.html#special-considerations-for-main

import os
import sys

from src.name_builder.name_builder import NameBuilder


def main() -> None:
    """Execute the standalone command-line tool."""
    print(NameBuilder.generate_name())


def init() -> None:
    if __name__ == "__main__":
        main()
        sys.exit(os.EX_OK)


init()
