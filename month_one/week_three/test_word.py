#!/usr/bin/python -m pytest -v
import pytest
from ppbtree import *

from month_one.week_three.solution_dictionary import *


@pytest.fixture
def full_dict():
    dict = Dictionary()

    dict.insert("magic")
    dict.insert("dog")
    dict.insert("bear")
    dict.insert("artist")
    dict.insert("fireworks")
    dict.insert("quiet")
    dict.insert("ostrich")
    dict.insert("right")
    dict.insert("television")

    print("===== ORIGINAL =====")
    print_tree(dict.get_root(), 'val', 'right', 'left')
    print("====================")

    return dict.get_root()


def test_get_min_node_no_left_is_node():
    tmp = Word("asdf")

    assert tmp.get_min_node() is tmp


def test_get_min_node_single_left(full_dict: Word):
    min_value = full_dict.right.get_min_node()
    assert min_value.val == "ostrich"


def test_get_min_node_many_left(full_dict: Word):
    assert full_dict.get_min_node().val == "artist"
