#!/usr/bin/env python
import os
DICTIONARY_FILE = os.path.abspath("month_one/week_three/dict.txt")


class Word:
    def __init__(self, val: str, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return self.val


class Dictionary:
    def __init__(self):
        self.root = Word("")

    def get_root(self) -> Word:
        pass

    def is_empty(self) -> bool:
        pass

    def insert(self, val: str) -> Word:
        pass

    def find(self, val: str) -> Word:
        pass

    def remove(self, val: str) -> bool:
        pass


def main():
    dictionary = Dictionary()
    # Write code here

    assert dictionary.find("missionary") is not None
    assert dictionary.find("place") is not None
    assert dictionary.find("such") is not None
    assert dictionary.find("fatal") is not None
    assert dictionary.find("again") is not None
    assert dictionary.find("few") is not None
    assert dictionary.find("against") is not None
    assert dictionary.find("transmission") is not None
    assert dictionary.find("vendor") is not None
    assert dictionary.find("epidemic") is not None
    assert dictionary.find("await") is not None
    assert dictionary.find("thrive") is not None
    assert dictionary.find("pad") is not None


if __name__ == "__main__":
    main()
