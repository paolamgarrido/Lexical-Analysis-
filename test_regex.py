import unittest
# Load the main code file.
from regex import test_regex  

# Import the function to be tested
class TestMatchesPattern(unittest.TestCase):
    def test_empty_string(self):
        self.assertFalse(test_regex(''))

    def test_valid_strings(self):
        self.assertTrue(test_regex('0'))
        self.assertTrue(test_regex('1'))
        self.assertTrue(test_regex('2'))
        self.assertTrue(test_regex('00'))
        self.assertTrue(test_regex('01'))
        self.assertTrue(test_regex('02'))
        self.assertTrue(test_regex('10'))
        self.assertTrue(test_regex('11'))
        self.assertTrue(test_regex('12'))
        self.assertTrue(test_regex('20'))
        self.assertTrue(test_regex('21'))
        self.assertTrue(test_regex('22'))
        self.assertTrue(test_regex('001'))
        self.assertTrue(test_regex('002'))
        self.assertTrue(test_regex('010'))
        self.assertTrue(test_regex('011'))
        self.assertTrue(test_regex('012'))
        self.assertTrue(test_regex('020'))
        self.assertTrue(test_regex('021'))
        self.assertTrue(test_regex('022'))
        self.assertTrue(test_regex('100'))
        self.assertTrue(test_regex('101'))
        self.assertTrue(test_regex('102'))
        self.assertTrue(test_regex('112'))
        self.assertTrue(test_regex('120'))
        self.assertTrue(test_regex('121'))
        self.assertTrue(test_regex('122'))
        self.assertTrue(test_regex('200'))
        self.assertTrue(test_regex('201'))
        self.assertTrue(test_regex('202'))
        self.assertTrue(test_regex('211'))
        self.assertTrue(test_regex('212'))
        self.assertTrue(test_regex('220'))
        self.assertTrue(test_regex('221'))
        self.assertTrue(test_regex('012212'))

    def test_invalid_strings(self):
        self.assertFalse(test_regex('111'))
        self.assertFalse(test_regex('110'))
        self.assertFalse(test_regex('222'))
        self.assertFalse(test_regex('210'))
        self.assertFalse(test_regex('221100'))
        self.assertFalse(test_regex('000'))
        self.assertFalse(test_regex('202110'))
        self.assertFalse(test_regex('012220'))
        self.assertFalse(test_regex('0110'))
        self.assertFalse(test_regex('0221100110'))

if __name__ == '__main__':
    unittest.main()