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
#d is fct delay to index delay
        d = (3.14/(4*np.pi))*1000
        dsine1= delay.delay(sine, d)
        dif1 = np.abs(sine + dsine1)

#Due to slight uncertainty of data when transformed, 
#the values will be tested to be within a certain tolerance
        for i in range(a.size):
            if dif[i]>.01:
                print 'Failed on dif index: ' , i
                self.assertTrue(dif[i]<.01)
            if dif1[i]>.1:
                print 'Failed on dif1 index: ' , i
                self.assertTrue(dif1[i]<.1)

        print 'checked FFT'


if __name__ == '__main__':
    unittest.main()
