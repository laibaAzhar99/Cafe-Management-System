import unittest
from controller import Controller

class TestCafe(unittest.TestCase):

    def setUp(self):

        self.controller = Controller()

    def test_add_item(self):

        self.controller.add_item(
            "Coffee",
            5,
            300
        )

        items = self.controller.get_items()

        self.assertTrue(
            len(items) > 0
        )

    def test_invalid_price(self):

        with self.assertRaises(ValueError):

            self.controller.add_item(
                "Burger",
                2,
                -100
            )

if __name__ == "__main__":

    unittest.main()