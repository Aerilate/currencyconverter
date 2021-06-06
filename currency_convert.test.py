import unittest
import imp

currency_convert = imp.load_source('currency_convert', 'currency_convert') # workaround since main file doesn't end with .py

class TestStringMethods(unittest.TestCase):

    def test_parseCSV(self):
        input = '''Feed Name,Price Per Month,Source Name,Last Update,Remote Name,Local Name
newsmonster,74.23,News Monster,1483820220,/mirror/nm/newsmonster.tgz,/r/nm.tgz
microtech,55.12,MicroTech Industries(TODO: Inc.? LLC?),1483820232,/dl/mtech.tar.gz,/r/mt.tgz'''

        expected = [['Feed Name','Price Per Month','Source Name','Last Update','Remote Name','Local Name'],
        ['newsmonster','74.23','News Monster','1483820220','/mirror/nm/newsmonster.tgz','/r/nm.tgz'],
        ['microtech','55.12','MicroTech Industries(TODO: Inc.? LLC?)','1483820232','/dl/mtech.tar.gz','/r/mt.tgz']]

        self.assertEqual(currency_convert.parseCSV(input), expected)

if __name__ == '__main__':
    unittest.main()
