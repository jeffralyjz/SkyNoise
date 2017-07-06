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
        a = np.linspace(-1*2*np.pi,2*np.pi, 1000)
#Small delay in sine function
        sine = np.sin(a)
        dsine = delay.delay(sine,.5)
        dif = np.abs(sine-dsine)
#Total destructive interference
        d1 = 250.
        d2 = -250.
        dsine1= delay.delay(sine, d1)
        dif1 = np.abs(sine + dsine1)
        dsine2 = delay.delay(sine, d2) 
        dif2 = np.abs(sine + dsine2)       
        tolerance = .01

        for i in range(a.size):
            if dif[i] > tolerance:
                print 'Failed on dif[' , i, ']'
                self.assertTrue(dif[i] < tolerance)
            if dif1[i] > tolerance:
                print 'Failed on dif1[' , i, ']'
                self.assertTrue(dif1[i] < tolerance)
            if dif2[i] > tolerance:
                print 'Failed on dif[' ,i,']'
                self.assertTrue(dif2[i] < tolerance)
        print 'Checked FFT'


if __name__ == '__main__':
    unittest.main()
