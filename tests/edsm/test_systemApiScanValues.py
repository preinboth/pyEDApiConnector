import unittest

from src.connector.edsm.systemApi import scan_values


class test_systemScanValues(unittest.TestCase):
    def test_get_estimated_value(self):
        json = scan_values.getEstimatedValue("Sol")
        # system data
        self.assertEqual(27, json['id'])
        self.assertEqual("Sol", json['name'])

    def test_get_estimated_value_by_id(self):
        json = scan_values.getEstimatedValueById(27)
        # system data
        self.assertEqual(27, json['id'])
        self.assertEqual("Sol", json['name'])


if __name__ == '__main__':
    unittest.main()
