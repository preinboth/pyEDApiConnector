import unittest

from EDApiConnector.connector.edsm.statusApi import server_status


class TestEdsmServerStatus(unittest.TestCase):
    def test_get_elite_server_status(self):
        json = server_status.getEliteServerStatus()
        if not json:
            self.fail("Not Data found")


if __name__ == "__main__":
    unittest.main()
