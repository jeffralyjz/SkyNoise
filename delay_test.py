import unittest
import delay
import numpy as np

class TestDelay(unittest.TestCase):
    def test_delay(self):
        n1 = np.random.randn(100)
        for i in range(99):    
            print i
            n1d=delay.delay(n1,i)
            if i ==0:
                self.assertTrue(np.all(n1==n1d))
            else:
                self.assertTrue(np.all(n1[:-i]==n1d[i:]))
        
        sine = np.sine
        for i in np.arange(0,2*np.pi,2*.31415):
            print i
            
            

if __name__ == '__main__':
    unittest.main()
