#!/bin/python -mpytest
import pytest
from editor import Editor, Actions, DLList


def count_list(root: DLList) -> int:
    length = 0
    p = root.head.next
    while p is not root.tail:
        length += 1
        p = p.next

    return length


def print_list(root: DLList) -> None:
    p = root.head.next
    while p is not root.tail:
        print(f"{p.val}", end="->" if p.next is not root.tail else "\n")
        p = p.next


class TestDLList:
    @pytest.fixture
    def empty_dllist(self):
        return DLList()

    def test_dllistialize(self, empty_dllist: DLList):
        assert type(empty_dllist.tail) == DLList.DLNode
        assert type(empty_dllist.head) == DLList.DLNode

        assert empty_dllist.head.next is empty_dllist.tail
        assert empty_dllist.tail.prev is empty_dllist.head

    def test_append_returns_node(self, empty_dllist: DLList):
        return_val = empty_dllist.append(1)

        assert type(return_val) != None
        assert type(return_val) == DLList.DLNode
        assert return_val.val == 1

    def test_append_once(self, empty_dllist: DLList):
        node_87 = empty_dllist.append(87)
        assert empty_dllist.head.next is node_87
        assert empty_dllist.tail.prev is node_87

        assert node_87.prev is empty_dllist.head
        assert node_87.next is empty_dllist.tail

        assert node_87.val == 87

    def test_append_three_times(self, empty_dllist: DLList):
        node_1 = empty_dllist.append(1)
        node_2 = empty_dllist.append(2)
        node_3 = empty_dllist.append(3)

        assert empty_dllist.head.next == node_1
        assert empty_dllist.head.next.next == node_2
        assert empty_dllist.tail.prev == node_3

        assert node_1.prev == empty_dllist.head
        assert node_1.next == node_2
        assert node_2.prev == node_1
        assert node_2.next == node_3
        assert node_3.prev == node_2
        assert node_3.next == empty_dllist.tail

    def test_replace_None_ptr(self, empty_dllist: DLList):
        assert empty_dllist.replace(1, None) == None

    def test_replace_head_ptr(self, empty_dllist: DLList):
        assert empty_dllist.replace(2, empty_dllist.head) == None

    def test_replace_tail_ptr(self, empty_dllist: DLList):
        one = empty_dllist.append(1)
        ten = empty_dllist.replace(10, empty_dllist.tail)

        assert empty_dllist.head.next is one
        assert one.next is ten
        assert ten.prev is one
        assert ten.next is empty_dllist.tail
        assert empty_dllist.tail.prev is ten

    def test_replace_one_list(self, empty_dllist: DLList):
        one = empty_dllist.append(1)
        two = empty_dllist.replace(2, one)
        assert empty_dllist.head.next == two

    def test_replace_begin_two_list(self, empty_dllist: DLList):
        one = empty_dllist.append(1)
        empty_dllist.append(2)

        three = empty_dllist.replace(3, one)

        assert count_list(empty_dllist) == 1
        assert empty_dllist.head.next is three
        assert empty_dllist.head.next.val == 3

    def test_replace_end_two_list(self, empty_dllist: DLList):
        one = empty_dllist.append(1)
        two = empty_dllist.append(2)

        three = empty_dllist.replace(3, two)

        assert empty_dllist.tail.prev.val == 3
        assert empty_dllist.tail.prev is three
        assert empty_dllist.head.next == one
        assert count_list(empty_dllist) == 2


class TestEditor:
    @pytest.fixture
    def editor(self):
        return Editor()

    def test_empty_editor(self, editor: Editor):
        assert editor.curr is editor.actions.tail

    def test_empty_editor_undo(self, editor: Editor):
        editor.undo()
        assert editor.curr is editor.actions.tail

    def test_empty_editor_redo(self, editor: Editor):
        editor.redo()
        assert editor.curr is editor.actions.tail

    def test_editor_act_once(self, editor: Editor):
        editor.act(Actions.Type)
        assert editor.curr.prev.val == Actions.Type
        assert count_list(editor.actions) == 1

    def test_editor_act_twice(self, editor: Editor):
        editor.act(Actions.Type)
        editor.act(Actions.Delete)
        assert editor.curr.prev.val == Actions.Delete
        assert count_list(editor.actions) == 2

    def test_editor_act_once_undo(self, editor: Editor):
        editor.act(Actions.Type)
        editor.undo()
        assert editor.curr == editor.actions.head.next

    def test_editor_act_once_undo_twice(self, editor: Editor):
        act = editor.act(Actions.Delete)
        editor.undo()
        editor.undo()
        assert editor.curr == act

    def test_editor_act_twice_undo(self, editor: Editor):
        editor.act(Actions.Type)
        actD = editor.act(Actions.Delete)
        editor.undo()
        assert editor.curr is actD

    def test_editor_act_twice_undo_redo(self, editor: Editor):
        editor.act(Actions.Delete)
        editor.undo()
        editor.redo()
        assert editor.curr is editor.actions.tail

    def test_editor_act_once_redo(self, editor: Editor):
        editor.redo()
        assert editor.curr is editor.actions.tail

    def test_editor_act_once_undo_overwrite(self, editor: Editor):
        editor.act(Actions.Type)
        editor.undo()
        act2 = editor.act(Actions.Delete)
        assert count_list(editor.actions) == 1
        assert editor.curr is editor.actions.tail
        assert editor.actions.head.next is act2

    def test_editor_act_thrice_undo_twice_overwrite(self, editor: Editor):
        act1 = editor.act(Actions.Type)
        editor.act(Actions.Type)
        editor.act(Actions.Delete)
        editor.undo()
        editor.undo()
        act2 = editor.act(Actions.Delete)

        assert count_list(editor.actions) == 2
        assert editor.curr is editor.actions.tail
        assert editor.actions.head.next is act1
        assert editor.actions.tail.prev is act2
