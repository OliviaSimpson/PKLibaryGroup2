import unittest
import pytest

import pkmodel as pk

class Dummymodel:
    k_a = 0
    

class SolutionTest(unittest.TestCase):
    """
    Tests the :class:`Solution` class.
    """
    def test_create(self):
        """
        Tests Solution creation.
        """
        model = pk.Solution()
        self.assertEqual(model.value, 44)

        