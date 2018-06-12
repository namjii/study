import unittest

from data_structure2.LinkedList import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_linkedlist(self):
        ll = LinkedList()
        assert ll.is_empty() is True, 'haha {}'.format(ll.is_empty())

        for i in range(1, 10):
            ll.append(i)
        assert ll.is_empty() is False
        ll.print()

        assert ll.size() == 9
        ll.remove(1)
        ll.print()
        assert ll.size() == 8
        ll.remove(5)
        ll.print()
        assert ll.size() == 7
        ll.remove(9)
        ll.print()
        assert ll.size() == 6

        assert ll.search(2) is not None
        assert ll.search(2).data == 2
        assert ll.search(5) is None


