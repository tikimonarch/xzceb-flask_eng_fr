import unittest

from translator import englishToFrench, frenchToEnglish


class TestMachineTranslation(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench("Hello"),"Bonjour")
        self.assertNotEqual(englishToFrench("Bye"),"Bonjour")

    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")
        self.assertNotEqual(englishToFrench("Bonjour"),"Bye")

if __name__=='__main__':
    unittest.main()