import sys
import unittest


def cutter(array, bottom, upper):
    new_array = [bottom if x < bottom else upper if x > upper else x for x in array]
    return new_array


class CutterTestMethods(unittest.TestCase):

    def test_different(self):
        self.assertEqual(cutter([1, 2, 3, 4, 5, 6], 2, 5), [2, 2, 3, 4, 5, 5])

    def test_same(self):
        self.assertEqual(cutter([3, 3, 3, 3], 4, 5), [4, 4, 4, 4])

    def test_still(self):
        self.assertEqual(cutter([3, 4, 5, 6], 2, 7), [3, 4, 5, 6])


if __name__ == "__main__":
    try:
        input_array = [int(item) for item in input("Enter the list items: ").split()]
        input_bottom = int(input("Enter bottom border: "))
        input_upper = int(input("Enter upper border: "))
        result = cutter(input_array, input_bottom, input_upper)
        print(result)
    except Exception as e:
        print("Error:", e.with_traceback(sys.exc_info()[2]))

