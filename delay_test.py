import unittest
import delay
import numpy as np

class TestDelay(unittest.TestCase):
    def test_delay(self):
        """Checking Concatenate"""
        n1 = np.random.randn(100)
        for i in range(10): 
            r = np.random.randint(100)
            n1d=delay.delay(n1,r)
            if r==0:
                self.assertTrue(np.all(n1==n1d))
            else:
                self.assertTrue(np.all(n1[:-r]==n1d[r:]))
            
            
        print 'Checked concatenate'        


        """Checking FFT"""
        sine = np.sin(np.linspace(0,2*np.pi, 1000))
        dsine = delay.delay(sine,.5)
        dif = np.abs(sine-dsine)

        for i in range(sine.size):
            self.assertTrue(dif[i]<.1)
        
        a = np.random.randn(100)
        rn = np.random.randint(31)*np.pi
        da = delay.delay(a, rn)
        dif = a-da

        for i in range(a.size):
            rand = np.random.randint(100)
            if dif[rand]<5 == False:
                print rand
                self.assertTrue(dif[rand]<5)
                

        print 'checked FFT'


if __name__ == '__main__':
    unittest.main()
