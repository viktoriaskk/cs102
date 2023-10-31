import unittest
import sys
sys.path.append(r'/Users/viktoriaskoblilova/Desktop/cs102')
from src.lab1.calculator import add, subtract, multiply, divide

class CalculatorTestCase(unittest.TestCase):

    # Тест для проверки работы, можно удалить
    def test_add(self):
        self.assertEquals(add(2, 2), 4)
    
    def test_subtract(self):
        self.assertEquals(subtract(5, 2), 3)

    def test_multiply(self):
        self.assertEquals(multiply(5, 2), 10)    

    def test_divide(self):
        self.assertEquals(divide(10, 2), 5)