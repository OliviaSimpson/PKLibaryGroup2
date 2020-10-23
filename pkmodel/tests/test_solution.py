import unittest
import pytest
import pkmodel as pk

class Dummymodel:
    q_p1 = 1.0
    q

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

        