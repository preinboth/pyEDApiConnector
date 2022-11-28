import unittest


class TestRoutePlanner(unittest.TestCase):
    def test_routePlanner(self):
        print(" Test running")
        # self.spansh_cntl = SpanshCntl()
        # route = self.spansh_cntl.routePlanner("HIP 117029", "Drojia YW-B d13-4", 1, 499)
        # for i in route:
        #     if i['jumps'] == 0:
        #         print(i['distance_left'])
        #         assert len(i['distance_left']) != 4377.93900300844
        #         break


if __name__ == "__main__":
    unittest.main()
