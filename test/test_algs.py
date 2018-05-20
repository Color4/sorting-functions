# quick sort and bubble sort implementation hw
# jan 2018
# author <christa.caggiano@ucsf.edu>

from sorting import quick_sort, bubble_sort


# test bubble sort
class TestBubbleSort(object):

    def test_empty(self):  # test empty list
        x = []
        assert bubble_sort.quick_sort(x) == []

    def test_one_item(self):  # test one item list
        x = [1]
        assert bubble_sort.bubble_sort(x) == [1]

    def test_many_items(self):  # list with many items and negative items
        x = [1, 2, 10, 0, 1, -1, 4, 8]
        assert bubble_sort.bubble_sort(x) == [-1, 0, 1, 1, 2, 4, 8, 10]

    def test_in_order(self):  # test an ordered list
        x = [1, 2, 3, 4, 5]
        assert bubble_sort.bubble_sort(x) == [1, 2, 3, 4, 5]

    def test_reverse_order(self):  # test a list completely out of order
        x = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        assert bubble_sort.bubble_sort(x) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# test quick sort  with same tests as above
class TestQuickSort(object):

    def test_empty(self):
        x = []
        assert quick_sort.quick_sort(x) == []

    def test_one_item(self):
        x = [1]
        assert quick_sort.quick_sort(x) == [1]

    def test_many_items(self):
        x = [1, 2, 10, 0, 1, -1, 4, 8]
        assert quick_sort.quick_sort(x) == [-1, 0, 1, 1, 2, 4, 8, 10]

    def test_in_order(self):
        x = [1, 2, 3, 4, 5]
        assert quick_sort.quick_sort(x) == [1, 2, 3, 4, 5]

    def test_reverse_order(self):
        x = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        assert quick_sort.quick_sort(x) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
