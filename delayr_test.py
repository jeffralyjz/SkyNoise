import unittest
import delayr
import numpy as np

class TestDelay(unittest.TestCase):
    def test_delay(self):
        n1 = np.random.randn(100)
        for i in range(99):    
            n1d=delayr.delay(n1,i)
            if i ==0:
                self.assertTrue(np.all(n1==n1d))
            else:
                self.assertTrue(np.all(n1[:-i]==n1d[i:]))
                if i == 10:
                    print np.all(n1[:-i]==n1d[i:])

if __name__ == '__main__':
    unittest.main()
