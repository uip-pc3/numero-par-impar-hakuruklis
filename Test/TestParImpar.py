from app.main import ParImpar
import unittest


class TestparImpar(unittest.TestCase):
    def TestParImpar(self):
        self.assertEquals(ParImpar(7),False)
        self.assertEquals(ParImpar(12),True)

if __name__ == '__main__':
    unittest.main()