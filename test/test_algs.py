import numpy as np
from example import algs


class TestBubbleSort(object):

    def test_empty(self):
        x = []
        assert algs.bubble_sort(x) == []

    def test_one_item(self):
        x = [1]
        assert algs.bubble_sort(x) == [1]

    def test_many_items(self):
        x = [1, 2, 10, 0, 1, -1, 4, 8]
        assert algs.bubble_sort(x) == [-1, 0, 1, 1, 2, 4, 8, 10]

    def test_in_order(self):
        x = [1, 2, 3, 4, 5]
        assert algs.bubble_sort(x) == [1, 2, 3, 4, 5]

    def test_reverse_order(self):
        x = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        assert algs.bubble_sort(x) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class TestQuickSort(object):

    def test_empty(self):
        x = []
        assert algs.quick_sort(x) == []

    def test_one_item(self):
        x = [1]
        assert algs.quick_sort(x) == [1]

    def test_many_items(self):
        x = [1, 2, 10, 0, 1, -1, 4, 8]
        assert algs.quick_sort(x) == [-1, 0, 1, 1, 2, 4, 8, 10]

    def test_in_order(self):
        x = [1, 2, 3, 4, 5]
        assert algs.quick_sort(x) == [1, 2, 3, 4, 5]

    def test_reverse_order(self):
        x = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        assert algs.quick_sort(x) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
