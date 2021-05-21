#!/usr/bin/python -m pytest -v
import pytest

from month_one.week_three.solution_dictionary import *


@pytest.fixture
def my_dict():
    return Dictionary()


def test_exists(my_dict):
    assert isinstance(my_dict.root, Word)
    assert my_dict.root.val == ""


def test_empty_no_insert(my_dict):
    assert my_dict.is_empty()


def test_not_empty_after_insert(my_dict):
    my_dict.insert("test")
    assert not my_dict.is_empty()


def test_insert_once(my_dict):
    my_dict.insert("test")
    assert isinstance(my_dict.root.right, Word)


def test_insert_twice_increasing_order(my_dict):
    my_dict.insert("t")
    my_dict.insert("test")

    assert my_dict.root.right.val == "t"
    assert my_dict.root.right.right.val == "test"

def test_insert_twice_increasing_decreasing(my_dict):
    my_dict.insert("test")
    my_dict.insert("t")

    assert my_dict.root.right.val == "test"
    assert my_dict.root.right.left.val == "t"

def test_insert_root_left_right_right(my_dict):
    my_dict.insert("michael")
    my_dict.insert("are")
    my_dict.insert("quiet")
    my_dict.insert("zed")

    assert my_dict.root.right.val == "michael"
    assert my_dict.root.right.left.val == "are"
    assert my_dict.root.right.right.val == "quiet"
    assert my_dict.root.right.right.right.val == "zed"