import unittest
from Lesson17.logic import Task


class WordTestCase(unittest.TestCase):
    def test_remove_negative_num(self):
        list_num = Task.number_list([1, 2, 3, 4, -10])
        pos_list = Task.choose_func(list_num, Task.square_nums, Task.remove_negatives)
        self.assertEqual(pos_list(), [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
