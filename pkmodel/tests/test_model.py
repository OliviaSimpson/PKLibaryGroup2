import unittest
import pkmodel as pk


class ModelTest(unittest.TestCase):
    """
    Tests the :class:`Model` class.
    """
    def test_central(self):
        """
        Tests that model has a central compartment
        """
        model = pk.Model([[0, 1], [2, 4], [3, 5]])
        self.assert_(model.central)

    def test_peripherals(self):
        """
        Tests that model has correct number of peripherals
        """
        model = pk.Model([[0, 1], [2, 4], [3, 5]])
        self.assertEqual(len(model.peripherals), 2)