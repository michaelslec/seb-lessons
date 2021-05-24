#!/usr/bin/python -m pytest -v
import pytest
from ppbtree import *

from month_one.week_three.solution_dictionary import *


def display(tree: Dictionary, header="RESULT"):
    print(f"===== {header} =====\n")
    if tree.get_root() is None:
        print("~EMPTY~")
    else:
        print_tree(tree.get_root(), 'val', 'right', 'left')


@pytest.fixture
def my_dict():
    print("====== SETUP - EMPTY ======\n")
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
    dict.insert("oasis")
    dict.insert("obituary")
    dict.insert("right")
    dict.insert("television")

    display(dict, "SETUP - ORIGINAL")

    return dict


def test_exists(my_dict):
    assert isinstance(my_dict.root, Word)
    assert my_dict.root.val == ""


def test_get_root_returns_real_root(my_dict):
    root = my_dict.get_root()
    assert root is None

    my_dict.root.right = Word("test")
    display(my_dict)
    root = my_dict.get_root()

    assert root is my_dict.root.right


def test_empty_no_insert(my_dict):
    assert my_dict.is_empty()


def test_not_empty_after_insert(my_dict):
    my_dict.insert("test")
    assert not my_dict.is_empty()


def test_insert_once(my_dict):
    my_dict.insert("test")
    display(my_dict)
    assert isinstance(my_dict.get_root(), Word)


def test_insert_twice_increasing_order(my_dict):
    my_dict.insert("t")
    my_dict.insert("test")
    display(my_dict)

    assert my_dict.get_root().val == "t"
    assert my_dict.get_root().right.val == "test"


def test_insert_twice_increasing_decreasing(my_dict):
    my_dict.insert("test")
    my_dict.insert("t")
    display(my_dict)

    assert my_dict.get_root().val == "test"
    assert my_dict.get_root().left.val == "t"


def test_insert_root_left_right_right(my_dict):
    my_dict.insert("michael")
    my_dict.insert("are")
    my_dict.insert("quiet")
    my_dict.insert("zed")
    display(my_dict)

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
    display(my_dict)

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


def test_remove_on_empty_tree_returns_false(my_dict):
    assert my_dict.remove("test") == False


def test_remove_non_existing_node_returns_false(full_dict: Dictionary):
    assert full_dict.remove("asdf") == False


def test_remove_only_node_in_tree_returns_true(my_dict: Dictionary):
    my_dict.insert("root")
    assert my_dict.remove("root") == True
    display(my_dict)
    assert my_dict.find("root") is None


def test_remove_child_leaf_node_left_only(full_dict: Dictionary):
    assert full_dict.remove("artist") == True
    display(full_dict)
    assert full_dict.find("artist") is None


def test_remove_child_leaf_node_right_only(full_dict: Dictionary):
    assert full_dict.remove("television") == True
    display(full_dict)
    assert full_dict.find("television") is None


def test_remove_child_node_with_right_child(full_dict: Dictionary):
    assert full_dict.remove("right") == True
    display(full_dict)
    assert full_dict.find("right") is None
    assert full_dict.get_root().right.right.val == "television"


def test_remove_child_node_with_left_child(full_dict: Dictionary):
    assert full_dict.remove("bear") == True
    display(full_dict)
    assert full_dict.find("bear") is None
    assert full_dict.get_root().left.left.val == "artist"


def test_remove_child_with_both_children_and_right_is_single(full_dict: Dictionary):
    assert full_dict.remove("dog") == True
    display(full_dict)
    assert full_dict.find("dog") is None
    assert full_dict.get_root().left.val == "fireworks"


def test_remove_child_with_both_children_and_right_has_right(full_dict: Dictionary):
    assert full_dict.remove("quiet") == True
    display(full_dict)
    assert full_dict.find("quiet") is None
    assert full_dict.get_root().right.val == "right"
    assert full_dict.get_root().right.right.val == "television"


def test_remove_child_with_both_children_and_right_has_many(full_dict: Dictionary):
    assert full_dict.remove("magic") == True
    display(full_dict)
    assert full_dict.find("magic") is None
    assert full_dict.get_root().val == "oasis"
    assert full_dict.get_root().right.right.val == "right"
