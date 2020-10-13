import unittest
from name_function import get_formatted_name


class NameTestCse(unittest.TestCase):
    """Test for name_function"""

    def test_first_last_name(self):
        formatted_name = get_formatted_name('pierina', 'moreno')
        self.assertEqual(formatted_name, 'Pierina Moreno')



    def test_first_last_middle_name(self):
        """do names like 'Leda Benavides Isabel' works fine?"""
        formatted_name = get_formatted_name('leda', 'isabel', 'benavides')
        self.assertEqual(formatted_name, 'Leda Benavides Isabel')


if __name__ == '__main__':
    unittest.main()
