import unittest

from data_structure2.Queue import Queue


class TestQueue(unittest.TestCase):

    def test_queue(self):
        queue = Queue()
        assert queue.next(9) == 0
        assert queue.next(10) == 1
        assert queue.next(5) == 6

        assert queue.is_empty()

        for i in range(1, 11):
            queue.enqueue(i)
        assert queue.is_full()
        queue.enqueue(11)
        assert queue.size() == 9, queue.size()

        assert queue.dequeue() == 1
        while not queue.is_empty():
            queue.dequeue()
        assert queue.size() == 0, queue.size()
        assert queue.dequeue() is None



