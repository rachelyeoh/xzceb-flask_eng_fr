"""
The purpose of this is to test the translator module
"""
import unittest

from translator import englishToFrench, frenchToEnglish


class TestMachineTranslation(unittest.TestCase):
    "This class is to test the translation functions"

    def test_en_to_fr_null(self):
        "This function tests for null input"
        self.assertNotEqual(englishToFrench(
            'Not null'), None, 'It is a null input')

    def test_en_to_fr(self):
        "This function tests for translation of 'Hello' and 'Bonjour'"
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

    def test_fr_to_en_null(self):
        "This function tests for null input"
        self.assertNotEqual(frenchToEnglish('Not null'), None,
                            'It is a null input')

    def test_fr_to_en(self):
        "This function tests for translation of 'Bonjour' and 'Hello'"
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')


if __name__ == '__main__':
    unittest.main()
