import unittest
import pkmodel as pk


class ProtocolTest(unittest.TestCase):
    """
    Tests the :class:`Protocol` class.
    """
    def test_continuous_int(self):
        """
        Tests continuous dosing protocol with int value.
        """
        model = pk.Protocol(1, 2)
        self.assertEqual(model.dose(2), 0.5)

    def test_continuous_float(self):
        """
        Tests continuous dosing protocol with float value.
        """
        model = pk.Protocol(9, 2.25)
        self.assertEqual(model.dose(3), 4)

    def test_discrete_list(self):
        """
        Tests discrete dosing protocol with list.
        """
        model = pk.Protocol(7, [1,2,3])
        self.assertEqual(round(model.dose(1), 2), 2.33)

    def test_discrete_tuple(self):
        """
        Tests discrete dosing protocol with tuple.
        """
        model = pk.Protocol(5, (2,3,4))
        self.assertEqual(round(model.dose(2), 2), 1.67)

    def test_type_error(self):
        """
        Tests that an invalid input type returns a type error.
        """
        model = pk.Protocol(5, 'error test')
        
        with self.assertRaises(TypeError):
            error_protocol = Protocol(7, 'error')
            error_expected = error_protocol.dose(3)
