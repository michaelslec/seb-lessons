#!/usr/bin/env python

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