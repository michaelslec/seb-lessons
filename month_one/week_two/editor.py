#!/bin/env python3
import enum

"""

Seb,

Below I have provided a couple of skeleton classes for implementation. This
file is accompanied by a screen recording of the assignment. As usual, there
is a file that holds all the tests. When all the tests pass, the assignment
is finished. Talk soon!

Testing:
    Install:
    > pip install pytest

    EITHER:
    > pytest
    OR
    > python -m pytest

"""


class Actions(enum.Enum):
    Type = 0
    Delete = 1


class DLList():
    """A Doubly linked list with head and tail pointers.

    Attributes:
        head (DLNode): Sentinel node who's next is the first node in the list.
        tail (DLNode): Sentinel node who's prev is the last node in the list.
    """
    class DLNode():
        def __init__(self, val):
            self.val = val
            self.next = None
            self.prev = None
        
        def __repr__(self):
            return f"DLNode({self.val})"

    def __init__(self):
        self.head = self.DLNode(0)
        self.tail = self.DLNode(0)

    def append(self):
        """Appends node to end of list (tail).

        Args:
            val (T): Value of new node to append to list.

        Returns:
            DLNode: The node that was appended.
        """
        pass

    def replace(self, val, ptr: DLNode):
        """Replaces `ptr` and following nodes with node of value `val`.

        Examples:
            >>> self = DLList()
            ... self.append(1)
            ... node2 = self.append(2)
            ... self.replace(3, node2)
            ... self.print()
            '1->3'

            >>> self = DLList()
            ... node1 = self.append(1)
            ... self.append(2)
            ... self.replace(3, node1)
            ... self.print()
            '3'


        Args:
            ptr (DLNode): Node to replace.
            val (int): Value of new node insert into list

        Returns:
            DLNode: The node that was append.
        """
        pass

    def count(self) -> int:
        """Returns length of list."""
        length = 0
        p = self.head.next
        while p is not self.tail:
            length += 1
            p = p.next

        return length

    def print(self) -> None:
        """Prints list."""
        p = self.head.next
        while p is not self.tail:
            print(f"{p.val}", end="->" if p.next is not self.tail else "\n")
            p = p.next


class Editor:
    """Simple editor class which can act, undo, and redo.

    Attributes:
        actions (DLList): A doubly linked list of all actions performed.
        curr (DLNode): A pointer to the current node (Follows undo and redo).
    """

    def __init__(self):
        pass

    def act(self):
        """Inserts or Appends an Action to the actions list.

        If `curr` is pointing to something other than tail, act will instead
        replace the current node that `curr` is pointing to.

        Args:
            action (Actions): Action to be inserted onto list.

        Examples:
            >>> self = Editor()
            ... self.act(Actions.Type)
            ... self.act(Actions.Type)
            ... self.actions.print()
            'Actions.Type->Actions.Type'

            >>> self = Editor()
            ... self.act(Actions.Type)
            ... self.act(Actions.Type)
            ... self.act(Actions.Delete)
            ... self.undo()
            ... self.undo()
            ... self.act(Actions.Delete)
            ... self.actions.print()
            'Actions.Type->Actions.Delete'


        Returns:
            DLNode: The newly inserted/appended Node.
        """
        pass

    def undo(self):
        """Moves curr back."""
        pass

    def redo(self):
        """Moves curr forward."""
        pass
