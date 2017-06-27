import unittest
import delay
import numpy as np

class TestDelay(unittest.TestCase):
    def test_delay(self):
        n1 = np.random.randn(1000)
        n1d = delay.delay(n1, 0)
        self.assertTrue(np.all(n1 == n1d))
        n1d = delay.delay(n1, 1)
        self.assertTrue(np.all(n1[:-1] == n1d[1:]))

if __name__ == '__main__':
    unittest.main()
