#!/usr/bin/python -m pytest -v
import pytest
from ppbtree import *

from month_one.week_three.solution_dictionary import *


@pytest.fixture
def my_dict():
    print("-------------- Empty Tree ---------------")
    return Dictionary()


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

    print_tree(dict.root, 'val', 'right', 'left')

    return dict


def test_exists(my_dict):
    assert isinstance(my_dict.root, Word)
    assert my_dict.root.val == ""


def test_get_root_returns_real_root(my_dict):
    root = my_dict.get_root()
    assert root is None

    my_dict.root.right = Word("test")
    root = my_dict.get_root()

    assert root is my_dict.root.right


def test_empty_no_insert(my_dict):
    assert my_dict.is_empty()


def test_not_empty_after_insert(my_dict):
    my_dict.insert("test")
    assert not my_dict.is_empty()


def test_insert_once(my_dict):
    my_dict.insert("test")
    assert isinstance(my_dict.get_root(), Word)


def test_insert_twice_increasing_order(my_dict):
    my_dict.insert("t")
    my_dict.insert("test")

    assert my_dict.get_root().val == "t"
    assert my_dict.get_root().right.val == "test"


def test_insert_twice_increasing_decreasing(my_dict):
    my_dict.insert("test")
    my_dict.insert("t")

    assert my_dict.get_root().val == "test"
    assert my_dict.get_root().left.val == "t"


def test_insert_root_left_right_right(my_dict):
    my_dict.insert("michael")
    my_dict.insert("are")
    my_dict.insert("quiet")
    my_dict.insert("zed")

    assert my_dict.get_root().val == "michael"
    assert my_dict.get_root().left.val == "are"
    assert my_dict.get_root().right.val == "quiet"
    assert my_dict.get_root().right.right.val == "zed"


def test_insert_root_left_left_right_left(my_dict):
    my_dict.insert("michael")
    my_dict.insert("luck")
    my_dict.insert("bear")
    my_dict.insert("quiet")
    my_dict.insert("are")

    assert my_dict.get_root().val == "michael"
    assert my_dict.get_root().left.val == "luck"
    assert my_dict.get_root().left.left.val == "bear"
    assert my_dict.get_root().left.left.left.val == "are"
    assert my_dict.get_root().right.val == "quiet"


def test_not_found_returns_none(full_dict):
    result = full_dict.find("asdfasdf")

    assert result is None


def test_find_single_node_tree(my_dict):
    my_dict.insert("first")
    node = my_dict.find("first")

    assert node is my_dict.get_root()


def test_find_node_strictly_greater(full_dict):
    result = full_dict.find("television")

    assert full_dict.get_root().right.right.right is result


def test_find_node_strictly_lesser(full_dict):
    result = full_dict.find("artist")

    assert full_dict.get_root().left.left.left is result


def test_find_node_nested_left_and_right(full_dict):
    result = full_dict.find("fireworks")

    assert full_dict.get_root().left.right is result